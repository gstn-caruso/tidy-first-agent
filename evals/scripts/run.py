#!/usr/bin/env python3
"""Run tidy-first-agent eval cases through `claude -p` and score them.

    python3 evals/scripts/run.py --cases A1,A2 --model sonnet --runs 2 \
        [--plugin-dir <repo>] [--baseline] [--agent-name tidy-first:tidier] \
        [--out evals/results/<label>] [--timeout-min 25] [--dry-run]

See evals/README.md for the full picture. This module is import-safe (no
top-level side effects) so evals/scripts/verify.py's `verify()` can be
exercised directly, and so tests can import parse_stream()/build_command()
without invoking `claude`.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import shutil
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parents[1]
CASES_DIR = REPO_ROOT / "evals" / "cases"
FIXTURES_DIR = REPO_ROOT / "evals" / "fixtures"

sys.path.insert(0, str(SCRIPTS_DIR))
import verify as verify_mod  # noqa: E402

DEFAULT_MAX_TURNS = 40
FIXTURE_SKIP = {"manifest.json", "target", ".git", "__pycache__"}


# --------------------------------------------------------------------------
# case / fixture loading
# --------------------------------------------------------------------------

def load_cases():
    cases = {}
    for path in sorted(CASES_DIR.glob("*.json")):
        case = json.loads(path.read_text())
        cases[case["id"]] = case
    return cases


def select_cases(tokens, cases):
    tokens = [t.strip() for t in tokens if t.strip()]
    selected = []
    for token in tokens:
        if token.lower() == "all":
            selected.extend(cases.values())
            continue
        matches = [c for cid, c in cases.items() if cid.startswith(token)]
        if not matches:
            print(f"warning: --cases token {token!r} matched no case", file=sys.stderr)
        selected.extend(matches)
    seen = set()
    ordered = []
    for c in selected:
        if c["id"] not in seen:
            seen.add(c["id"])
            ordered.append(c)
    return ordered


def load_manifest(fixture_name):
    manifest_path = FIXTURES_DIR / fixture_name / "manifest.json"
    if not manifest_path.exists():
        return None, manifest_path
    return json.loads(manifest_path.read_text()), manifest_path


# --------------------------------------------------------------------------
# workdir setup
# --------------------------------------------------------------------------

def copy_fixture(fixture_dir: Path, dest: Path):
    for root, dirs, files in os.walk(fixture_dir):
        dirs[:] = [d for d in dirs if d not in FIXTURE_SKIP]
        rel = Path(root).relative_to(fixture_dir)
        dest_root = dest / rel
        dest_root.mkdir(parents=True, exist_ok=True)
        for f in files:
            if rel == Path(".") and f in FIXTURE_SKIP:
                continue
            shutil.copy2(Path(root) / f, dest_root / f)


def _git(args, cwd, check=True, timeout=60):
    r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {cwd}: {r.stderr}")
    return r


def init_git_repo(workdir: Path):
    _git(["init", "-q"], cwd=workdir)
    _git(["add", "-A"], cwd=workdir)
    _git(["-c", "user.name=eval", "-c", "user.email=eval@local", "commit", "-q", "-m", "base"], cwd=workdir)
    _git(["tag", "base"], cwd=workdir)


def apply_prepare(workdir: Path, ops: list):
    for op in ops:
        kind = op["op"]
        if kind == "append":
            p = workdir / op["file"]
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "a") as fh:
                fh.write(op["text"])
        elif kind == "write":
            p = workdir / op["file"]
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w") as fh:
                fh.write(op["text"])
        elif kind == "remove":
            p = workdir / op["path"]
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            elif p.exists():
                p.unlink()
        elif kind == "commit":
            _git(["add", "-A"], cwd=workdir)
            _git(["-c", "user.name=eval", "-c", "user.email=eval@local", "commit", "-q", "-m", op["message"]], cwd=workdir)
        else:
            raise ValueError(f"unknown prepare op: {kind!r}")
    # Tag where prepare left off, whether or not it added commits. With an
    # empty prepare this is the same commit as `base`; with a prepare that
    # commits (A4, A5) it is not, and verify.py counts "new" commits from
    # here so setup commits aren't held to the tidier's message contract.
    _git(["tag", "-f", "agent-start"], cwd=workdir)


def setup_workdir(fixture_dir: Path, workdir: Path, case: dict):
    if workdir.exists():
        shutil.rmtree(workdir)
    workdir.mkdir(parents=True)
    copy_fixture(fixture_dir, workdir)
    init_git_repo(workdir)
    apply_prepare(workdir, case.get("prepare", []))


def run_warmup(workdir: Path, test_command: str, timeout_sec: int):
    if not test_command:
        return True, "no test_command in manifest, warmup skipped"
    try:
        r = subprocess.run(test_command, shell=True, cwd=str(workdir), capture_output=True, text=True, timeout=timeout_sec)
    except subprocess.TimeoutExpired:
        return False, "warmup test_command timed out"
    ok = r.returncode == 0
    return ok, "green" if ok else (r.stdout[-800:] + r.stderr[-800:])


# --------------------------------------------------------------------------
# command building
# --------------------------------------------------------------------------

def build_command(case: dict, model: str, plugin_dir: Path, agent_name: str, baseline: bool):
    cmd = ["claude", "-p"]
    if not baseline:
        cmd += ["--plugin-dir", str(plugin_dir)]
        if case["family"] == "A":
            cmd += ["--agent", agent_name]
    cmd += [
        "--model", model,
        "--max-turns", str(case.get("max_turns", DEFAULT_MAX_TURNS)),
        "--output-format", "stream-json",
        "--verbose",
        "--dangerously-skip-permissions",
        case["prompt"],
    ]
    return cmd


def build_env():
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)
    return env


# --------------------------------------------------------------------------
# stream-json parsing
# --------------------------------------------------------------------------

def parse_stream(text: str) -> dict:
    """Parse newline-delimited stream-json into tool_uses / assistant_texts /
    result_event. Defensive: unknown fields ignored, malformed lines skipped."""
    tool_uses = []
    assistant_texts = []
    result_event = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue
        etype = obj.get("type")
        if etype == "assistant":
            message = obj.get("message") or {}
            for block in message.get("content") or []:
                if not isinstance(block, dict):
                    continue
                btype = block.get("type")
                if btype == "tool_use":
                    tool_uses.append({"name": block.get("name"), "input": block.get("input")})
                elif btype == "text":
                    assistant_texts.append(block.get("text", ""))
        elif etype == "result":
            result_event = obj
    return {"tool_uses": tool_uses, "assistant_texts": assistant_texts, "result_event": result_event}


def _sum_or_none(*values):
    """Sum ints/floats, or None if any input is missing (e.g. a crashed run)."""
    if any(v is None for v in values):
        return None
    return sum(values)


def build_metrics(result_event, wall_ms):
    result_event = result_event or {}
    usage = result_event.get("usage") or {}
    input_tokens = usage.get("input_tokens")
    cache_read = usage.get("cache_read_input_tokens")
    cache_create = usage.get("cache_creation_input_tokens")
    return {
        "cost_usd": result_event.get("total_cost_usd"),
        "input_tokens": input_tokens,
        "output_tokens": usage.get("output_tokens"),
        "cache_read": cache_read,
        "cache_create": cache_create,
        # Prompt caching means most "input" on a run is cache reads, not
        # fresh input tokens — this is the number that reflects what the
        # agent actually had in context: input + cache writes + cache reads.
        "context_tokens": _sum_or_none(input_tokens, cache_create, cache_read),
        "num_turns": result_event.get("num_turns"),
        "duration_ms": result_event.get("duration_ms"),
        "wall_ms": wall_ms,
    }


# --------------------------------------------------------------------------
# one case x model x run
# --------------------------------------------------------------------------

def execute_claude(cmd, cwd, env, timeout_sec):
    proc = subprocess.Popen(cmd, cwd=str(cwd), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    start = time.monotonic()
    try:
        stdout, stderr = proc.communicate(timeout=timeout_sec)
        timed_out = False
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
        timed_out = True
    wall_ms = int((time.monotonic() - start) * 1000)
    return stdout, stderr, timed_out, wall_ms


def run_one(case, model, n, args, out_dir: Path):
    label = f"{case['id']}-{model}-{n}"
    fixture_dir = FIXTURES_DIR / case["fixture"]
    manifest, manifest_path = load_manifest(case["fixture"])

    if not fixture_dir.exists() or manifest is None:
        record = {
            "case": case["id"], "model": model, "run": n, "command": None,
            "metrics": {}, "tool_use_counts": {}, "tool_uses": [], "checks": {},
            "passed": False, "result_text": "",
            "crashed": f"fixture not found: {fixture_dir} (manifest missing)",
        }
        (out_dir / f"{label}.json").write_text(json.dumps(record, indent=2))
        print(f"[{label}] SKIP - fixture '{case['fixture']}' not found")
        return record

    workdir = out_dir / "workdir" / label
    setup_workdir(fixture_dir, workdir, case)

    plugin_dir = Path(args.plugin_dir) if args.plugin_dir else REPO_ROOT
    if args.warmup:
        ok, evidence = run_warmup(workdir, manifest.get("test_command", ""), manifest.get("test_timeout_sec", 300))
        if not ok:
            record = {
                "case": case["id"], "model": model, "run": n, "command": None,
                "metrics": {}, "tool_use_counts": {}, "tool_uses": [], "checks": {},
                "passed": False, "result_text": "",
                "crashed": f"warmup red: {evidence[-500:]}",
            }
            (out_dir / f"{label}.json").write_text(json.dumps(record, indent=2))
            print(f"[{label}] ABORT - warmup red")
            return record

    cmd = build_command(case, model, plugin_dir, args.agent_name, args.baseline)
    env = build_env()

    stdout, stderr, timed_out, wall_ms = execute_claude(cmd, workdir, env, args.timeout_min * 60)
    (out_dir / f"{label}.stream.jsonl").write_text(stdout)
    (out_dir / f"{label}.stderr.log").write_text(stderr)

    parsed = parse_stream(stdout)
    result_event = parsed["result_event"]
    crashed = False
    if result_event is None:
        crashed = f"timeout after {args.timeout_min}min" if timed_out else "stream ended without a result event"
        crashed += "; stderr tail: " + stderr[-1000:]

    result_text = (result_event or {}).get("result", "") or ""
    run_record = {
        "case": case["id"], "model": model, "run": n,
        "tool_uses": parsed["tool_uses"],
        "result_text": result_text,
    }

    checks = {}
    if not crashed:
        try:
            checks = verify_mod.verify(workdir, case, manifest, run_record, repo_root=REPO_ROOT)
        except Exception as e:  # noqa: BLE001
            checks = {"verify_error": {"passed": False, "evidence": f"{type(e).__name__}: {e}"}}

    passed = (not crashed) and all(c["passed"] for c in checks.values())

    record = {
        "case": case["id"], "model": model, "run": n,
        "command": cmd,
        "metrics": build_metrics(result_event, wall_ms),
        "tool_use_counts": dict(Counter(t["name"] for t in parsed["tool_uses"])),
        "tool_uses": parsed["tool_uses"],
        "checks": checks,
        "passed": passed,
        "result_text": result_text,
        "crashed": crashed,
    }
    (out_dir / f"{label}.json").write_text(json.dumps(record, indent=2))

    status = "CRASH" if crashed else ("PASS" if passed else "FAIL")
    cost = record["metrics"].get("cost_usd")
    turns = record["metrics"].get("num_turns")
    print(f"[{label}] {status} cost=${cost} turns={turns} wall={wall_ms}ms")
    return record


def dry_run_one(case, model, n, args, out_dir: Path):
    label = f"{case['id']}-{model}-{n}"
    fixture_dir = FIXTURES_DIR / case["fixture"]
    manifest, _ = load_manifest(case["fixture"])
    plugin_dir = Path(args.plugin_dir) if args.plugin_dir else REPO_ROOT
    cmd = build_command(case, model, plugin_dir, args.agent_name, args.baseline)

    workdir = out_dir / "workdir" / label
    if fixture_dir.exists() and manifest is not None:
        setup_workdir(fixture_dir, workdir, case)
        note = ""
    else:
        note = f"  [fixture '{case['fixture']}' not found at {fixture_dir} - workdir not set up]"

    print(f"[{label}] cwd={workdir}{note}")
    print("  " + " ".join(_shell_quote(c) for c in cmd))


def _shell_quote(s: str) -> str:
    if s and all(c not in s for c in ' \t\n"\'$`\\'):
        return s
    return "'" + s.replace("'", "'\\''") + "'"


# --------------------------------------------------------------------------
# summary
# --------------------------------------------------------------------------

def _mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def build_summary(records):
    by_case_model = {}
    for r in records:
        by_case_model.setdefault(r["case"], {}).setdefault(r["model"], []).append(r)

    cases_summary = {}
    for case_id, by_model in by_case_model.items():
        cases_summary[case_id] = {}
        for model, runs in by_model.items():
            failing = Counter()
            for r in runs:
                for name, c in r.get("checks", {}).items():
                    if not c.get("passed"):
                        failing[name] += 1
                if r.get("crashed"):
                    failing["crashed"] += 1
            cases_summary[case_id][model] = {
                "runs": len(runs),
                "pass_rate": sum(1 for r in runs if r["passed"]) / len(runs) if runs else None,
                "mean_cost_usd": _mean([r["metrics"].get("cost_usd") for r in runs]),
                "mean_context_tokens": _mean([r["metrics"].get("context_tokens") for r in runs]),
                "mean_output_tokens": _mean([r["metrics"].get("output_tokens") for r in runs]),
                "mean_cache_read": _mean([r["metrics"].get("cache_read") for r in runs]),
                "mean_turns": _mean([r["metrics"].get("num_turns") for r in runs]),
                "mean_duration_ms": _mean([r["metrics"].get("duration_ms") for r in runs]),
                "failing_checks": dict(failing.most_common()),
            }

    run_rows = []
    for r in records:
        failed = [name for name, c in r.get("checks", {}).items() if not c.get("passed")]
        if r.get("crashed"):
            failed = ["crashed"] + failed
        run_rows.append({
            "case": r["case"], "model": r["model"], "run": r["run"],
            "passed": r["passed"], "failed_checks": failed,
        })

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cases": cases_summary,
        "runs": run_rows,
    }


def render_summary_md(summary: dict) -> str:
    lines = ["# Eval run summary", "", f"Generated: {summary['generated_at']}", ""]

    lines.append("## Case x model")
    lines.append("")
    lines.append("| case | model | runs | pass rate | mean cost | mean input (incl. cache) | mean cache read | mean out tok | mean turns | mean duration |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for case_id in sorted(summary["cases"]):
        for model in sorted(summary["cases"][case_id]):
            s = summary["cases"][case_id][model]
            pr = f"{s['pass_rate']*100:.0f}%" if s["pass_rate"] is not None else "n/a"
            cost = f"${s['mean_cost_usd']:.3f}" if s["mean_cost_usd"] is not None else "n/a"
            ctx_tok = f"{s['mean_context_tokens']:.0f}" if s["mean_context_tokens"] is not None else "n/a"
            cache_read = f"{s['mean_cache_read']:.0f}" if s["mean_cache_read"] is not None else "n/a"
            out_tok = f"{s['mean_output_tokens']:.0f}" if s["mean_output_tokens"] is not None else "n/a"
            turns = f"{s['mean_turns']:.1f}" if s["mean_turns"] is not None else "n/a"
            dur = f"{s['mean_duration_ms']:.0f}ms" if s["mean_duration_ms"] is not None else "n/a"
            lines.append(f"| {case_id} | {model} | {s['runs']} | {pr} | {cost} | {ctx_tok} | {cache_read} | {out_tok} | {turns} | {dur} |")

    lines += ["", "## Most frequent failing checks per case", ""]
    for case_id in sorted(summary["cases"]):
        combined = Counter()
        for model in summary["cases"][case_id]:
            combined.update(summary["cases"][case_id][model]["failing_checks"])
        if combined:
            top = ", ".join(f"{name} ({n})" for name, n in combined.most_common())
            lines.append(f"- **{case_id}**: {top}")
        else:
            lines.append(f"- **{case_id}**: no failures")

    lines += ["", "## Per-run results", "", "| case | model | run | passed | failed checks |", "|---|---|---|---|---|"]
    for row in summary["runs"]:
        checks_str = ", ".join(row["failed_checks"]) or "-"
        lines.append(f"| {row['case']} | {row['model']} | {row['run']} | {'yes' if row['passed'] else 'no'} | {checks_str} |")

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# reverify: redo verify() over an existing --out dir without calling claude
# --------------------------------------------------------------------------

def reverify(out_dir: Path):
    """Re-run verify() over every `<case>-<model>-<n>.json` already in
    out_dir, using each record's stored `result_text` and `tool_uses`
    against its still-present workdir, then rewrite that record's
    `checks`/`passed` and the batch summaries. Useful after a verify.py fix
    so a past run doesn't need a fresh (costly) `claude -p` pass."""
    all_cases = load_cases()
    manifest_cache = {}
    records = []
    updated = 0
    skipped = 0

    for path in sorted(out_dir.glob("*.json")):
        if path.name in ("summary.json",):
            continue
        try:
            record = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        if not {"case", "model", "run"} <= record.keys():
            continue  # not a per-run record

        label = f"{record['case']}-{record['model']}-{record['run']}"
        case = all_cases.get(record["case"])
        if case is None:
            print(f"[reverify] SKIP {label} - unknown case id (not in evals/cases)")
            skipped += 1
            records.append(record)
            continue

        fixture = case["fixture"]
        if fixture not in manifest_cache:
            manifest_cache[fixture] = load_manifest(fixture)[0]
        manifest = manifest_cache[fixture]

        workdir = out_dir / "workdir" / label
        if manifest is None or not workdir.exists():
            print(f"[reverify] SKIP {label} - manifest or workdir no longer available")
            skipped += 1
            records.append(record)
            continue

        run_record = {
            "case": record["case"], "model": record["model"], "run": record["run"],
            "tool_uses": record.get("tool_uses", []),
            "result_text": record.get("result_text", ""),
        }
        try:
            checks = verify_mod.verify(workdir, case, manifest, run_record, repo_root=REPO_ROOT)
        except Exception as e:  # noqa: BLE001
            checks = {"verify_error": {"passed": False, "evidence": f"{type(e).__name__}: {e}"}}

        record["checks"] = checks
        record["passed"] = (not record.get("crashed")) and all(c["passed"] for c in checks.values())
        path.write_text(json.dumps(record, indent=2))
        print(f"[reverify] {label}: {'PASS' if record['passed'] else 'FAIL'}")
        updated += 1
        records.append(record)

    summary = build_summary(records)
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    (out_dir / "summary.md").write_text(render_summary_md(summary))
    print(f"[reverify] {updated} record(s) re-verified, {skipped} skipped; summary rewritten")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def parse_args(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=None, help="comma list of case-id prefixes, or all/A/B/C (required unless --reverify)")
    ap.add_argument("--model", default="sonnet", help="comma list of models")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--plugin-dir", default=None)
    ap.add_argument("--baseline", action="store_true", help="ablation: drop --plugin-dir and --agent")
    ap.add_argument("--agent-name", default="tidy-first:tidier")
    ap.add_argument("--out", default=None)
    ap.add_argument("--timeout-min", type=float, default=25)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reverify", action="store_true",
                     help="re-run verify() over an existing --out dir's per-run JSON + workdirs, "
                          "without calling claude, and rewrite checks/passed and the summaries")
    warmup = ap.add_mutually_exclusive_group()
    warmup.add_argument("--warmup", dest="warmup", action="store_true")
    warmup.add_argument("--no-warmup", dest="warmup", action="store_false")
    ap.set_defaults(warmup=True)
    args = ap.parse_args(argv)
    if not args.reverify and not args.cases:
        ap.error("--cases is required unless --reverify")
    if args.reverify and not args.out:
        ap.error("--reverify requires --out <dir>")
    return args


def main(argv=None):
    args = parse_args(argv)

    if args.reverify:
        out_dir = Path(args.out)
        if not out_dir.exists():
            print(f"--reverify: --out {out_dir} does not exist", file=sys.stderr)
            return 1
        return reverify(out_dir)

    if args.out:
        out_dir = Path(args.out)
    else:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        out_dir = REPO_ROOT / "evals" / "results" / f"run-{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "workdir").mkdir(parents=True, exist_ok=True)

    all_cases = load_cases()
    cases = select_cases(args.cases.split(","), all_cases)
    if not cases:
        print(f"no cases matched --cases {args.cases!r} (known: {', '.join(sorted(all_cases))})", file=sys.stderr)
        return 1

    models = [m.strip() for m in args.model.split(",") if m.strip()]

    records = []
    total = len(cases) * len(models) * args.runs
    done = 0
    for case in cases:
        for model in models:
            for n in range(1, args.runs + 1):
                done += 1
                print(f"[{done}/{total}] ", end="")
                if args.dry_run:
                    dry_run_one(case, model, n, args, out_dir)
                else:
                    records.append(run_one(case, model, n, args, out_dir))

    if args.dry_run:
        print(f"dry-run: {total} command(s) printed, no claude invocations made")
        return 0

    summary = build_summary(records)
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    (out_dir / "summary.md").write_text(render_summary_md(summary))
    print(f"summary written to {out_dir / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
