# tidy-first-agent evals

Scores the `tidier` agent and the `tidy-first` skill against a Java fixture
(`evals/fixtures/java-orders/`, built separately — see its `manifest.json`)
using real `claude -p` runs plus deterministic git/test checks.

## Run it

```
python3 evals/scripts/run.py --cases A1,A2 --model sonnet --runs 2
python3 evals/scripts/run.py --cases all --model sonnet --dry-run   # print commands only
python3 evals/scripts/run.py --cases B --model sonnet --baseline    # ablation: no plugin/agent
```

`--cases` matches case-id prefixes (`A1` → `A1-pricer-first.json`), a
family (`A`/`B`/`C`), or `all`. Other flags: `--plugin-dir` (default: repo
root), `--agent-name` (default `tidy-first:tidier`), `--out` (default
`evals/results/run-<timestamp>`), `--timeout-min` (default 25),
`--no-warmup`. Runs are sequential; a missing fixture degrades to a clear
per-case skip note instead of a crash, in `--dry-run` and real runs alike.

## What is measured

- **Family A** (`--agent tidy-first:tidier`): right tidyings, one per
  commit, tests green at every commit, decoys left alone, chapter/page
  cited and matching `skills/tidy-first/references/catalog.md`, a report.
- **Family B** (no `--agent`, 2 turns): does the main agent delegate to
  `tidier` (via `Task`) on tidy-shaped prompts, and *not* on
  feature/bugfix/big-refactor prompts.
- **Family C** (no `--agent`, 6 turns): does `tidy-first` answer a
  planning question via the `Skill` tool, citing real tidying names,
  without touching files.

`verify.py` implements every check as a pure function of the tidied
workdir + case + manifest + parsed run record, each wrapped so it reports
`{"passed": False, "evidence": "error: ..."}` instead of raising. A few
checks (`commit_subjects`, `pages_match_catalog`, `test_files_untouched`)
always run for family A — the tidier's own contract. New commits are
counted from an `agent-start` tag (set right after `prepare` runs, before
`claude -p` starts), not `base` — so `prepare`'s own setup commits (A4
drops the test dir, A5 adds a test) skip that contract.

## Reading results

Per run: `evals/results/<label>/<case>-<model>-<n>.json` — metrics (cost,
tokens, turns, duration), `tool_use_counts`, every `checks[name]` with
evidence, overall `passed`, and `crashed` (falsy, or timeout / missing
`result` event + stderr tail). Raw transcripts: `.stream.jsonl` /
`.stderr.log`. Per batch: `evals/results/<label>/summary.md` (case ×
model pass rate, mean cost/tokens/turns/duration, top failing checks)
plus `summary.json`.

## Testing the harness

```
python3 evals/scripts/verify.py <workdir> <case.json> <manifest.json> [--result-text file]
```

Useful against a hand-built git repo without spending a `claude -p` call.
