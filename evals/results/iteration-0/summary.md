# Eval run summary

Generated: 2026-09-01T22:43:02.532953+00:00

## Case x model

| case | model | runs | pass rate | mean cost | mean input (incl. cache) | mean cache read | mean out tok | mean turns | mean duration |
|---|---|---|---|---|---|---|---|---|---|
| A1-pricer-first | sonnet | 2 | 50% | $0.526 | n/a | 999010 | 15800 | 33.5 | 246630ms |

## Most frequent failing checks per case

- **A1-pricer-first**: report_citations_match_catalog (1), required_tidyings (1)

## Per-run results

| case | model | run | passed | failed checks |
|---|---|---|---|---|
| A1-pricer-first | sonnet | 1 | no | report_citations_match_catalog, required_tidyings |
| A1-pricer-first | sonnet | 2 | yes | - |
