#!/usr/bin/env python3
"""Consolidate several run dirs into one iteration summary.

Usage: consolidate.py <title> <out.md> <run-dir>...
Per case × model: runs, passes, mean cost, mean turns, mean cache-read tokens,
mean output tokens, mean duration. Later dirs override earlier ones for the
same (case, model) — pass re-runs last.
"""
import glob, json, statistics, sys
from collections import defaultdict

title, out, *dirs = sys.argv[1:]
records = {}
for d in dirs:
    for f in sorted(glob.glob(f"{d}/*-[0-9].json")):
        r = json.load(open(f))
        if "case" not in r:
            continue
        records[(r["case"], r["model"], r["run"])] = r
groups = defaultdict(list)
for (case, model, run), r in sorted(records.items()):
    groups[(case, model)].append(r)
def mean(xs): return statistics.fmean(xs) if xs else float("nan")
lines = [f"# {title}", "", f"Sources: {', '.join(dirs)}", "",
         "| case | model | runs | pass | mean cost | mean turns | mean cache read | mean out tok | mean s |",
         "|---|---|---|---|---|---|---|---|---|"]
totals = defaultdict(lambda: [0, 0, 0.0])
for (case, model), rs in sorted(groups.items()):
    ok = [r for r in rs if not r.get("crashed")]
    passed = sum(1 for r in rs if r.get("passed"))
    m = lambda k: mean([r["metrics"].get(k) or 0 for r in ok])
    lines.append(f"| {case} | {model} | {len(rs)} | {passed}/{len(rs)} | ${m('cost_usd'):.2f} | {m('num_turns'):.0f} | {m('cache_read')/1000:.0f}k | {m('output_tokens')/1000:.1f}k | {m('duration_ms')/1000:.0f} |")
    t = totals[model]; t[0] += passed; t[1] += len(rs); t[2] += sum(r["metrics"].get("cost_usd") or 0 for r in ok)
lines += ["", "## Totals per model", "", "| model | pass | est. cost |", "|---|---|---|"]
for model, (p, n, c) in sorted(totals.items()):
    lines.append(f"| {model} | {p}/{n} | ${c:.2f} |")
lines += ["", "## Failed checks", ""]
for (case, model), rs in sorted(groups.items()):
    for r in rs:
        fails = [k for k, v in r["checks"].items() if not v["passed"]]
        if fails or r.get("crashed"):
            lines.append(f"- {case} · {model} · run {r['run']}: {', '.join(fails) or 'crashed'}")
open(out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:40]))
