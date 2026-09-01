# Iteration 1 — restructured agent (commit ffbd4c4), A1–A6 × {sonnet, haiku} × 2, B/C

Sources: evals/results/iteration-1-sonnet, evals/results/iteration-1-haiku, evals/results/iteration-1-sonnet-a5, evals/results/iteration-1-haiku-a5, evals/results/iteration-1-b2, evals/results/iteration-1-bc

| case | model | runs | pass | mean cost | mean turns | mean cache read | mean out tok | mean s |
|---|---|---|---|---|---|---|---|---|
| A1-pricer-first | haiku | 2 | 0/2 | $0.13 | 25 | 469k | 8.5k | 118 |
| A1-pricer-first | sonnet | 2 | 2/2 | $0.47 | 33 | 905k | 15.9k | 190 |
| A2-parser-first | haiku | 2 | 0/2 | $0.07 | 15 | 211k | 5.2k | 64 |
| A2-parser-first | sonnet | 2 | 0/2 | $0.26 | 19 | 363k | 10.2k | 117 |
| A3-dirty-tree | haiku | 2 | 1/2 | $0.05 | 11 | 149k | 3.9k | 51 |
| A3-dirty-tree | sonnet | 2 | 2/2 | $0.05 | 6 | 72k | 1.2k | 16 |
| A4-no-tests | haiku | 2 | 1/2 | $0.12 | 20 | 357k | 9.4k | 122 |
| A4-no-tests | sonnet | 2 | 1/2 | $0.31 | 20 | 470k | 12.7k | 147 |
| A5-pricer-after | haiku | 2 | 1/2 | $0.14 | 30 | 586k | 8.7k | 123 |
| A5-pricer-after | sonnet | 2 | 2/2 | $0.25 | 18 | 372k | 9.0k | 117 |
| A6-pricer-comprehension | haiku | 2 | 1/2 | $0.13 | 25 | 483k | 9.3k | 123 |
| A6-pricer-comprehension | sonnet | 2 | 2/2 | $0.46 | 31 | 835k | 16.3k | 188 |
| B1-trigger-tidy-first | sonnet | 1 | 0/1 | $0.12 | 3 | 61k | 0.5k | 6 |
| B2-trigger-spanish | sonnet | 1 | 0/1 | $0.14 | 3 | 61k | 2.0k | 24 |
| B3-trigger-which-apply | sonnet | 1 | 0/1 | $0.12 | 3 | 61k | 0.8k | 11 |
| B4-trigger-after | sonnet | 1 | 0/1 | $0.13 | 3 | 61k | 1.4k | 16 |
| B5-no-trigger-feature | sonnet | 1 | 1/1 | $0.11 | 3 | 61k | 0.4k | 6 |
| B6-no-trigger-fix | sonnet | 1 | 1/1 | $0.11 | 3 | 61k | 0.3k | 5 |
| B7-no-trigger-refactor | sonnet | 1 | 1/1 | $0.12 | 3 | 61k | 0.6k | 7 |
| C1-skill-plan-pricer | sonnet | 1 | 1/1 | $0.43 | 15 | 273k | 17.1k | 174 |
| C2-skill-plan-parser | sonnet | 1 | 1/1 | $0.34 | 6 | 107k | 18.7k | 186 |

## Totals per model

| model | pass | est. cost |
|---|---|---|
| haiku | 4/12 | $1.28 |
| sonnet | 14/21 | $5.23 |

## Failed checks

- A1-pricer-first · haiku · run 1: pages_match_catalog, report_citations_match_catalog
- A1-pricer-first · haiku · run 2: commit_subjects, required_tidyings, tests_green_each_commit
- A2-parser-first · haiku · run 1: required_tidyings, report_mentions
- A2-parser-first · haiku · run 2: commit_count, required_tidyings, report_mentions
- A2-parser-first · sonnet · run 1: report_mentions
- A2-parser-first · sonnet · run 2: commit_count, report_mentions
- A3-dirty-tree · haiku · run 2: report_mentions
- A4-no-tests · haiku · run 2: forbidden_tidyings
- A4-no-tests · sonnet · run 2: report_mentions
- A5-pricer-after · haiku · run 1: report_sections
- A6-pricer-comprehension · haiku · run 1: report_mentions
- B1-trigger-tidy-first · sonnet · run 1: first_tool
- B2-trigger-spanish · sonnet · run 1: first_tool
- B3-trigger-which-apply · sonnet · run 1: first_tool
- B4-trigger-after · sonnet · run 1: first_tool
