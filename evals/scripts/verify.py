#!/usr/bin/env python3
"""Deterministic checks over a repo the tidier agent has (or hasn't) worked on.

verify(workdir, case, manifest, run_record) -> {check_name: {"passed": bool, "evidence": str}}

Only the checks whose expect-key is present in case["expect"] run, plus a
handful of "implied" checks (commit_subjects, pages_match_catalog,
test_files_untouched) that always run for family A once there is a commit
range to look at — these encode the tidier's own contract, not something a
case author should have to opt into every time.

Commits are counted from the `agent-start` tag if the workdir has one
(run.py creates it right after `prepare` is applied, before `claude -p`
runs), falling back to `base`. This matters for cases whose `prepare` makes
its own commit (e.g. "chore: drop tests"): that commit is setup, not
something the agent wrote, so it must not be held to the
`refactor(tidy): ...` subject contract. With an empty `prepare`,
`agent-start` and `base` are the same commit, so nothing changes for the
common case.

Every check function may raise; verify() catches and reports
{"passed": False, "evidence": "error: ..."} rather than propagating.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

DEFAULT_TEST_TIMEOUT_SEC = 300

SUBJECT_RE = re.compile(r"^refactor\(tidy\): ")
BODY_PAGE_RE = re.compile(r"ch\.\s*\d+,\s*pp?\.\s*\d+")
CITATION_RE = re.compile(r"ch\.\s*(\d+),?\s*pp?\.\s*(\d+)")
REMOVED_LINE_RE = re.compile(r"^-(?!--)")
ADDED_LINE_RE = re.compile(r"^\+(?!\+\+)")
EDIT_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}


# --------------------------------------------------------------------------
# git plumbing
# --------------------------------------------------------------------------

def _git(args, cwd, timeout=60):
    return subprocess.run(
        ["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=timeout
    )


def _base_ref(workdir):
    r = _git(["rev-parse", "--verify", "-q", "agent-start"], cwd=workdir)
    if r.returncode == 0:
        return "agent-start"
    return "base"


def _new_commits(workdir):
    """Commits made after prepare, oldest first: [{sha, subject, body}, ...]."""
    base = _base_ref(workdir)
    r = _git(["log", "--reverse", f"{base}..HEAD", "--format=%H%x1f%s%x1f%b%x1e"], cwd=workdir)
    if r.returncode != 0:
        raise RuntimeError(f"git log {base}..HEAD failed: {r.stderr.strip()}")
    commits = []
    for rec in r.stdout.split("\x1e"):
        rec = rec.strip("\n")
        if not rec.strip():
            continue
        parts = rec.split("\x1f", 2)
        sha = parts[0].strip()
        subject = parts[1].strip() if len(parts) > 1 else ""
        body = parts[2].strip() if len(parts) > 2 else ""
        if sha:
            commits.append({"sha": sha, "subject": subject, "body": body})
    return commits


# --------------------------------------------------------------------------
# catalog.md parsing: "| # | Tidying | ... | Page |"
# --------------------------------------------------------------------------

# Part II ("Managing") and Part III ("Theory") don't have their own catalog
# table (they're not tidyings), but the tidier still cites their chapters —
# e.g. ch. 21 "First, After, Later, Never" — so their starting pages are
# hand-transcribed here for citation validation. Chs. 1-15 come from
# catalog.md instead, since that table is the source of truth for those.
PART_II_III_CHAPTER_START_PAGE = {
    16: 35, 17: 39, 18: 43, 19: 47, 20: 49, 21: 51, 22: 57, 23: 61, 24: 65,
    25: 67, 26: 69, 27: 73, 28: 75, 29: 77, 30: 81, 31: 85, 32: 89, 33: 91,
}


def _catalog_rows(catalog_path) -> list:
    """Parse a markdown table like catalog.md's into a list of
    {column_name_lower: cell_text} dicts, one per data row (the header and
    its `---` separator row excluded)."""
    text = Path(catalog_path).read_text(encoding="utf-8")
    header = None
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(re.fullmatch(r"-+", c) for c in cells if c):
            continue  # header separator row
        if len(cells) < len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def load_catalog(catalog_path) -> dict:
    """{tidying name (lowercased): starting page}, chs. 1-15."""
    catalog = {}
    for row in _catalog_rows(catalog_path):
        name = row.get("tidying", "").strip()
        m = re.search(r"\d+", row.get("page", ""))
        if name and m:
            catalog[name.lower()] = int(m.group())
    return catalog


def load_chapter_start_pages(catalog_path) -> dict:
    """{chapter number: starting page} for the whole book, chs. 1-33:
    1-15 parsed from catalog.md's '#'/'Page' columns, 16-33 the fixed
    Part II/III table above."""
    chapters = {}
    for row in _catalog_rows(catalog_path):
        m_num = re.search(r"\d+", row.get("#", ""))
        m_page = re.search(r"\d+", row.get("page", ""))
        if m_num and m_page:
            chapters[int(m_num.group())] = int(m_page.group())
    chapters.update(PART_II_III_CHAPTER_START_PAGE)
    return chapters


def _extract_chapter_page_citations(text: str) -> list:
    """[(chapter:int, page:int), ...] for every "ch. N, p. M" (or "pp.")
    citation in text, in order of appearance."""
    return [(int(ch), int(pg)) for ch, pg in CITATION_RE.findall(text)]


def _catalog_name_pattern(name: str) -> re.Pattern:
    """Case-insensitive regex for a catalog tidying name, tolerant of a
    dropped/added trailing 's' on any word (an agent writing "Delete
    Redundant Comment" or "Guard Clause" should still match). Each word
    that ends in 's' gets that 's' made optional; each word that doesn't
    gets an optional trailing 's' — e.g. "Delete Redundant Comments" ->
    delete\\s+redundants?\\s+comments?, matching both "comment" and
    "comments" (and, harmlessly, "redundants").
    """
    parts = []
    for word in name.split():
        if word.lower().endswith("s"):
            parts.append(re.escape(word[:-1]) + "s?")
        else:
            parts.append(re.escape(word) + "s?")
    return re.compile(r"\s+".join(parts), re.IGNORECASE)


# --------------------------------------------------------------------------
# individual checks — each may raise; verify() wraps them safely
# --------------------------------------------------------------------------

def check_clean_tree(workdir):
    r = _git(["status", "--porcelain"], cwd=workdir)
    if r.returncode != 0:
        raise RuntimeError(f"git status failed: {r.stderr.strip()}")
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    lines = [l for l in lines if not l[3:].startswith("target/")]
    passed = not lines
    return {"passed": passed, "evidence": "clean" if passed else "dirty: " + "; ".join(lines[:20])}


def check_commit_count(workdir, case):
    commits = _new_commits(workdir)
    n = len(commits)
    expect = case.get("expect", {})
    lo = expect.get("min_commits", 0)
    hi = expect.get("max_commits", 10 ** 9)
    passed = lo <= n <= hi
    listing = ", ".join(f"{c['sha'][:7]} {c['subject']}" for c in commits) or "none"
    return {"passed": passed, "evidence": f"{n} new commit(s) (expected {lo}..{hi}): {listing}"}


def check_commit_subjects(workdir):
    commits = _new_commits(workdir)
    if not commits:
        return {"passed": True, "evidence": "no new commits"}
    bad = []
    for c in commits:
        ok_subject = bool(SUBJECT_RE.match(c["subject"]))
        ok_body = bool(BODY_PAGE_RE.search(c["body"]))
        if not (ok_subject and ok_body):
            bad.append(
                f"{c['sha'][:7]} subject_ok={ok_subject} cites_page={ok_body} subject={c['subject']!r}"
            )
    passed = not bad
    return {"passed": passed, "evidence": "well-formed" if passed else "; ".join(bad)}


def check_pages_match_catalog(workdir, chapter_pages):
    """Validates every "ch. N, p. M" citation in each new commit's body
    against the chapter's starting page (chs. 1-33 — see
    load_chapter_start_pages), independent of whether the subject names a
    catalog tidying. This also catches a citation naming a tidying chapter
    (1-15) with the wrong page, and a citation for a Part II/III chapter
    (16-33, e.g. "First, After, Later, Never") that used to be skipped
    entirely because nothing in Part II/III has a subject-name match."""
    if not chapter_pages:
        return {"passed": True, "evidence": "catalog not available, skipped"}
    commits = _new_commits(workdir)
    if not commits:
        return {"passed": True, "evidence": "no new commits"}
    problems = []
    checked = 0
    for c in commits:
        for ch, pg in _extract_chapter_page_citations(c["body"]):
            checked += 1
            start = chapter_pages.get(ch)
            if start is None:
                problems.append(f"{c['sha'][:7]} cites ch.{ch} (outside 1-33) p.{pg}")
                continue
            if not (start <= pg <= start + 3):
                problems.append(f"{c['sha'][:7]} cites ch.{ch} p.{pg}, expected p.{start}..{start + 3}")
    passed = not problems
    evidence = f"{checked} citation(s) checked against catalog" if passed else "; ".join(problems)
    return {"passed": passed, "evidence": evidence}


def check_report_citations_match_catalog(run_record, chapter_pages):
    """Same validation as check_pages_match_catalog, but over the agent's
    final report text instead of commit bodies — a report table can cite a
    chapter/page pair with a typo (e.g. "ch. 31, p. 31") even when the
    commit itself got it right."""
    text = run_record.get("result_text") or ""
    citations = _extract_chapter_page_citations(text)
    if not citations:
        return {"passed": True, "evidence": "no chapter/page citations in report"}
    triples = []
    for ch, pg in citations:
        start = chapter_pages.get(ch)
        ok = start is not None and start <= pg <= start + 3
        triples.append((ch, pg, ok))
    passed = all(ok for _, _, ok in triples)
    return {"passed": passed, "evidence": str(triples)}


def check_required_tidyings(workdir, case):
    commits = _new_commits(workdir)
    subjects = " | ".join(c["subject"] for c in commits)
    required = case.get("expect", {}).get("required_tidyings", [])
    missing = [t for t in required if not _catalog_name_pattern(t).search(subjects)]
    passed = not missing
    return {"passed": passed, "evidence": "all present" if passed else "missing: " + ", ".join(missing)}


def check_forbidden_tidyings(workdir, case):
    commits = _new_commits(workdir)
    subjects = " | ".join(c["subject"] for c in commits)
    forbidden = case.get("expect", {}).get("forbidden_tidyings", [])
    present = [t for t in forbidden if _catalog_name_pattern(t).search(subjects)]
    passed = not present
    return {"passed": passed, "evidence": "none present" if passed else "found forbidden: " + ", ".join(present)}


def check_tests_green_each_commit(workdir, manifest):
    test_command = manifest.get("test_command")
    if not test_command:
        return {"passed": False, "evidence": "no test_command in manifest"}
    commits = _new_commits(workdir)
    if not commits:
        return {"passed": True, "evidence": "no new commits to check"}
    timeout = manifest.get("test_timeout_sec", DEFAULT_TEST_TIMEOUT_SEC)
    orig = _git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=workdir).stdout.strip()
    if not orig or orig == "HEAD":
        orig = _git(["rev-parse", "HEAD"], cwd=workdir).stdout.strip()
    results = []
    try:
        for c in commits:
            co = _git(["-c", "advice.detachedHead=false", "checkout", "-q", c["sha"]], cwd=workdir)
            if co.returncode != 0:
                results.append((c["sha"], False, "checkout failed: " + co.stderr[-300:]))
                continue
            try:
                r = subprocess.run(
                    test_command, shell=True, cwd=str(workdir),
                    capture_output=True, text=True, timeout=timeout,
                )
                ok = r.returncode == 0
                detail = "" if ok else (r.stdout[-400:] + r.stderr[-400:])
                results.append((c["sha"], ok, detail))
            except subprocess.TimeoutExpired:
                results.append((c["sha"], False, "test_command timed out"))
    finally:
        _git(["checkout", "-q", orig], cwd=workdir)
    bad = [f"{sha[:7]}: {detail}" for sha, ok, detail in results if not ok]
    passed = not bad
    evidence = "green at every commit" if passed else "; ".join(bad)
    return {"passed": passed, "evidence": evidence[:2000]}


def check_hidden_tests_green(workdir, manifest):
    ht = manifest.get("hidden_tests")
    if not ht:
        return {"passed": False, "evidence": "manifest has no hidden_tests"}
    repo_root = manifest.get("_repo_root")
    if not repo_root:
        return {"passed": False, "evidence": "repo_root unknown, cannot locate hidden tests"}
    src = Path(repo_root) / ht["from"]
    dst = Path(workdir) / ht["to"]
    if not src.exists():
        return {"passed": False, "evidence": f"hidden tests source not found: {src}"}
    test_command = manifest.get("test_command")
    if not test_command:
        return {"passed": False, "evidence": "no test_command in manifest"}

    existed_before = dst.exists()
    before_entries = {p.name for p in dst.iterdir()} if existed_before else set()
    dst.mkdir(parents=True, exist_ok=True)
    copied_names = []
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
        copied_names.append(item.name)

    try:
        r = subprocess.run(
            test_command, shell=True, cwd=str(workdir), capture_output=True, text=True,
            timeout=manifest.get("test_timeout_sec", DEFAULT_TEST_TIMEOUT_SEC),
        )
        passed = r.returncode == 0
        evidence = "hidden tests green" if passed else (r.stdout[-800:] + r.stderr[-800:])
    except subprocess.TimeoutExpired:
        passed = False
        evidence = "hidden test_command timed out"
    finally:
        for name in copied_names:
            if name not in before_entries:
                target = dst / name
                if target.is_dir():
                    shutil.rmtree(target, ignore_errors=True)
                elif target.exists():
                    target.unlink()
        if not existed_before and dst.exists() and not any(dst.iterdir()):
            dst.rmdir()
        _git(["checkout", "-q", "--", "."], cwd=workdir)
        _git(["clean", "-fdq"], cwd=workdir)
    return {"passed": passed, "evidence": evidence[:2000]}


def check_test_files_untouched(workdir, manifest):
    test_paths = manifest.get("test_paths") or []
    if not test_paths:
        return {"passed": True, "evidence": "no test_paths declared, skipped"}
    base = _base_ref(workdir)
    r = _git(["diff", "--name-only", f"{base}..HEAD"], cwd=workdir)
    if r.returncode != 0:
        raise RuntimeError(f"git diff {base}..HEAD failed: {r.stderr.strip()}")
    changed = [l for l in r.stdout.splitlines() if l.strip()]
    touched = [f for f in changed if any(f.startswith(tp) for tp in test_paths)]
    passed = not touched
    return {"passed": passed, "evidence": "untouched" if passed else "touched: " + ", ".join(touched)}


def check_decoys_intact(workdir, case, manifest):
    wanted = case.get("expect", {}).get("decoys_intact", [])
    decoys = {d["id"]: d for d in manifest.get("decoys", [])}
    problems = []
    checked = 0
    for did in wanted:
        d = decoys.get(did)
        if not d:
            problems.append(f"{did}: not found in manifest")
            continue
        r = _git(["show", f"HEAD:{d['file']}"], cwd=workdir)
        if r.returncode != 0:
            problems.append(f"{did}: cannot read {d['file']} at HEAD")
            continue
        checked += 1
        if not re.search(d["must_still_match"], r.stdout, re.M):
            problems.append(f"{did}: pattern no longer matches in {d['file']}")
    passed = not problems
    return {"passed": passed, "evidence": f"{checked} decoy(s) intact" if passed else "; ".join(problems)}


def _net_removed_lines(diff_text: str) -> list:
    """A tidying that de-indents (or re-indents) a whole block makes every
    line in it show up as a removed line in a `--unified=0` diff, even
    though its content didn't change. So a line only counts as NET removed
    if its whitespace-stripped content isn't cancelled out by an equally
    stripped added line: net = multiset(`-` lines, stripped) minus
    multiset(`+` lines, stripped). A pure re-indent removes and re-adds the
    same stripped text, so it cancels to zero net-removed occurrences.

    The multiset math runs on stripped text (so indentation-only moves
    cancel), but the lines returned keep their ORIGINAL, unstripped text —
    some mess anchors match on exact indentation, and stripping the
    returned lines would break those even when nothing was re-indented.
    """
    removed_raw = [l[1:] for l in diff_text.splitlines() if REMOVED_LINE_RE.match(l)]
    added_raw = [l[1:] for l in diff_text.splitlines() if ADDED_LINE_RE.match(l)]
    removed_counts = Counter(x.strip() for x in removed_raw)
    added_counts = Counter(x.strip() for x in added_raw)
    remaining = removed_counts - added_counts  # multiset diff: positive counts only

    net_removed_raw = []
    for raw in removed_raw:
        key = raw.strip()
        if remaining.get(key, 0) > 0:
            net_removed_raw.append(raw)
            remaining[key] -= 1
    return net_removed_raw


def check_one_mess_per_commit(workdir, manifest):
    commits = _new_commits(workdir)
    messes = manifest.get("messes", [])
    mapping = {}
    problems = []
    for c in commits:
        r = _git(["show", c["sha"], "--format=", "--unified=0"], cwd=workdir)
        net_removed_lines = _net_removed_lines(r.stdout)
        hit_ids = [m["id"] for m in messes if any(re.search(m["anchor"], line) for line in net_removed_lines)]
        mapping[c["sha"][:7]] = hit_ids
        if len(hit_ids) > 1:
            problems.append(f"{c['sha'][:7]}: touches {hit_ids}")
    passed = not problems
    mapping_str = "; ".join(f"{sha}:{ids}" for sha, ids in mapping.items()) or "no new commits"
    evidence = mapping_str if passed else "violations: " + "; ".join(problems) + " | map: " + mapping_str
    return {"passed": passed, "evidence": evidence}


def check_report_sections(run_record, case):
    text = run_record.get("result_text") or ""
    wanted = case.get("expect", {}).get("report_sections", [])
    missing = [s for s in wanted if s not in text]
    passed = not missing
    return {"passed": passed, "evidence": "all present" if passed else "missing: " + ", ".join(missing)}


def check_report_mentions(run_record, case):
    text = run_record.get("result_text") or ""
    wanted = case.get("expect", {}).get("report_mentions", [])
    missing = [p for p in wanted if not re.search(p, text)]
    passed = not missing
    return {"passed": passed, "evidence": "all matched" if passed else "no match for: " + ", ".join(missing)}


def check_report_not_mentions(run_record, case):
    text = run_record.get("result_text") or ""
    unwanted = case.get("expect", {}).get("report_not_mentions", [])
    present = [p for p in unwanted if re.search(p, text)]
    passed = not present
    return {"passed": passed, "evidence": "none matched" if passed else "matched: " + ", ".join(present)}


def check_max_report_lines(run_record, case):
    text = run_record.get("result_text") or ""
    n = len(text.splitlines())
    limit = case.get("expect", {}).get("max_report_lines", 10 ** 9)
    passed = n <= limit
    return {"passed": passed, "evidence": f"{n} lines (limit {limit})"}


def check_tree_unchanged_since_prepare(workdir, case):
    """Only the files prepare left dirty (uncommitted) may still be dirty."""
    expected_dirty = set()
    for op in case.get("prepare", []):
        if op["op"] in ("append", "write"):
            expected_dirty.add(op["file"])
        elif op["op"] == "commit":
            expected_dirty.clear()
    r = _git(["status", "--porcelain"], cwd=workdir)
    if r.returncode != 0:
        raise RuntimeError(f"git status failed: {r.stderr.strip()}")
    actual = set()
    for line in r.stdout.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        actual.add(path)
    passed = actual == expected_dirty
    return {"passed": passed, "evidence": f"expected dirty {sorted(expected_dirty)}, actual {sorted(actual)}"}


def check_first_tool(run_record, case):
    tool_uses = run_record.get("tool_uses", [])
    expected = case.get("expect", {}).get("first_tool", {})
    if not tool_uses:
        return {"passed": False, "evidence": "no tool_use in run"}
    first = tool_uses[0]
    name_ok = _tool_name_matches(first.get("name"), expected.get("name"))
    contains = expected.get("input_contains", "")
    input_str = json.dumps(first.get("input", {}), ensure_ascii=False)
    contains_ok = (not contains) or (contains.lower() in input_str.lower())
    passed = name_ok and contains_ok
    return {"passed": passed, "evidence": f"first tool_use: {first.get('name')} input~{input_str[:200]}"}


DELEGATION_TOOLS = {"Task", "Agent"}  # the subagent tool is named Agent in Claude Code >= 2.1


def _tool_name_matches(actual, wanted):
    if wanted in DELEGATION_TOOLS:
        return actual in DELEGATION_TOOLS
    return actual == wanted


def check_delegates_to(run_record, case):
    """Like check_first_tool, but the delegating tool_use need not be the
    very first one — the main session may explore for a turn or two before
    delegating. Passes if ANY tool_use has the expected name and the
    expected substring (case-insensitive) in json.dumps(input)."""
    expected = case.get("expect", {}).get("delegates_to", {})
    wanted_name = expected.get("name")
    contains = str(expected.get("input_contains", "")).lower()
    tool_uses = run_record.get("tool_uses", [])
    names_in_order = [t.get("name") for t in tool_uses]

    match_input = None
    for t in tool_uses:
        if _tool_name_matches(t.get("name"), wanted_name):
            input_str = json.dumps(t.get("input", {}), ensure_ascii=False)
            if not contains or contains in input_str.lower():
                match_input = input_str
                break

    passed = match_input is not None
    evidence = f"tool_uses in order: {names_in_order}"
    if match_input is not None:
        evidence += f"; first matching {wanted_name} input: {match_input[:200]}"
    else:
        evidence += f"; no {wanted_name} tool_use with {contains!r} in its input"
    return {"passed": passed, "evidence": evidence}


def check_must_not_delegate(run_record):
    offenders = []
    for t in run_record.get("tool_uses", []):
        if t.get("name") in DELEGATION_TOOLS:
            input_str = json.dumps(t.get("input", {}), ensure_ascii=False).lower()
            if "tidier" in input_str:
                offenders.append(input_str[:200])
    passed = not offenders
    return {"passed": passed, "evidence": "no delegation" if passed else "delegated: " + "; ".join(offenders)}


def check_skill_invoked(run_record, case):
    wanted = str(case.get("expect", {}).get("skill_invoked", "")).lower()
    for t in run_record.get("tool_uses", []):
        if t.get("name") == "Skill":
            input_str = json.dumps(t.get("input", {}), ensure_ascii=False).lower()
            if wanted in input_str:
                return {"passed": True, "evidence": f"Skill invoked with {input_str[:200]}"}
    return {"passed": False, "evidence": "no matching Skill tool_use found"}


def check_no_edits(run_record):
    offenders = [t.get("name") for t in run_record.get("tool_uses", []) if t.get("name") in EDIT_TOOLS]
    passed = not offenders
    return {"passed": passed, "evidence": "no edit tools used" if passed else "used: " + ", ".join(offenders)}


# --------------------------------------------------------------------------
# orchestration
# --------------------------------------------------------------------------

def _safe(fn, *args):
    try:
        return fn(*args)
    except Exception as e:  # noqa: BLE001 - a check must never raise
        return {"passed": False, "evidence": f"error: {type(e).__name__}: {e}"}


def verify(workdir, case, manifest, run_record, repo_root=None) -> dict:
    workdir = Path(workdir)
    expect = case.get("expect", {}) or {}
    manifest = dict(manifest or {})
    if repo_root is None:
        repo_root = manifest.get("_repo_root")
    if repo_root is not None:
        manifest["_repo_root"] = str(repo_root)

    catalog = {}
    chapter_pages = {}
    if repo_root is not None:
        cat_path = Path(repo_root) / "skills" / "tidy-first" / "references" / "catalog.md"
        if cat_path.exists():
            catalog = _safe_catalog(cat_path)
            chapter_pages = _safe_chapter_pages(cat_path)

    family = case.get("family")
    checks = {}

    if "clean_tree" in expect:
        checks["clean_tree"] = _safe(check_clean_tree, workdir)
    if "min_commits" in expect or "max_commits" in expect:
        checks["commit_count"] = _safe(check_commit_count, workdir, case)
    if family == "A":
        checks["commit_subjects"] = _safe(check_commit_subjects, workdir)
        checks["pages_match_catalog"] = _safe(check_pages_match_catalog, workdir, chapter_pages)
        checks["report_citations_match_catalog"] = _safe(check_report_citations_match_catalog, run_record, chapter_pages)
        checks["test_files_untouched"] = _safe(check_test_files_untouched, workdir, manifest)
    if "required_tidyings" in expect:
        checks["required_tidyings"] = _safe(check_required_tidyings, workdir, case)
    if "forbidden_tidyings" in expect:
        checks["forbidden_tidyings"] = _safe(check_forbidden_tidyings, workdir, case)
    if "tests_green_each_commit" in expect:
        checks["tests_green_each_commit"] = _safe(check_tests_green_each_commit, workdir, manifest)
    if "hidden_tests_green" in expect:
        checks["hidden_tests_green"] = _safe(check_hidden_tests_green, workdir, manifest)
    if "decoys_intact" in expect:
        checks["decoys_intact"] = _safe(check_decoys_intact, workdir, case, manifest)
    if "one_mess_per_commit" in expect:
        checks["one_mess_per_commit"] = _safe(check_one_mess_per_commit, workdir, manifest)
    if "report_sections" in expect:
        checks["report_sections"] = _safe(check_report_sections, run_record, case)
    if "report_mentions" in expect:
        checks["report_mentions"] = _safe(check_report_mentions, run_record, case)
    if "report_not_mentions" in expect:
        checks["report_not_mentions"] = _safe(check_report_not_mentions, run_record, case)
    if "max_report_lines" in expect:
        checks["max_report_lines"] = _safe(check_max_report_lines, run_record, case)
    if "tree_unchanged_since_prepare" in expect:
        checks["tree_unchanged_since_prepare"] = _safe(check_tree_unchanged_since_prepare, workdir, case)
    if "first_tool" in expect:
        checks["first_tool"] = _safe(check_first_tool, run_record, case)
    if "delegates_to" in expect:
        checks["delegates_to"] = _safe(check_delegates_to, run_record, case)
    if expect.get("must_not_delegate"):
        checks["must_not_delegate"] = _safe(check_must_not_delegate, run_record)
    if "skill_invoked" in expect:
        checks["skill_invoked"] = _safe(check_skill_invoked, run_record, case)
    if expect.get("no_edits"):
        checks["no_edits"] = _safe(check_no_edits, run_record)

    return checks


def _safe_catalog(cat_path):
    try:
        return load_catalog(cat_path)
    except Exception:
        return {}


def _safe_chapter_pages(cat_path):
    try:
        return load_chapter_start_pages(cat_path)
    except Exception:
        return {}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _find_repo_root(manifest_path: Path):
    for p in [manifest_path, *manifest_path.parents]:
        if p.name == "evals":
            return p.parent
    return manifest_path.resolve().parent


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("workdir")
    ap.add_argument("case_json")
    ap.add_argument("manifest_json")
    ap.add_argument("--result-text", help="file with the run's final result text")
    ap.add_argument("--run-record", help="optional JSON file with a full run_record (tool_uses, metrics...)")
    args = ap.parse_args(argv)

    case = json.loads(Path(args.case_json).read_text())
    manifest_path = Path(args.manifest_json)
    manifest = json.loads(manifest_path.read_text())

    run_record = {}
    if args.run_record:
        run_record = json.loads(Path(args.run_record).read_text())
    if args.result_text:
        run_record["result_text"] = Path(args.result_text).read_text()
    run_record.setdefault("tool_uses", [])
    run_record.setdefault("result_text", "")

    repo_root = _find_repo_root(manifest_path.resolve())
    checks = verify(args.workdir, case, manifest, run_record, repo_root=repo_root)
    print(json.dumps(checks, indent=2, sort_keys=True))
    all_passed = all(c["passed"] for c in checks.values())
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
