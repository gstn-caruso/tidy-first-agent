---
name: tidy-first
description: Kent Beck's Tidy First? for the main session — what a tidying is, the book's 15 tidyings, and when to tidy first/after/later/never; delegates the actual tidying to the tidier agent. Use when asked about tidyings, "tidy first", "tidy antes", "limpiá antes de la feature", separating structural from behavioral changes, or which tidyings apply to some code.
---

# Tidy First?

**The rule.** Structure changes (tidyings) and behavior changes go in separate commits and separate PRs (ch. 16). A commit is one tidying or one behavior change, never both.

**A tidying** is a tiny, reversible structural change that makes the next behavior change easier. The book has fifteen, chs. 1–15 — `references/catalog.md` gives prompt, move, caveat and page for each: Guard Clauses · Dead Code · Normalize Symmetries · New Interface, Old Implementation · Reading Order · Cohesion Order · Move Declaration and Initialization Together · Explaining Variables · Explaining Constants · Explicit Parameters · Chunk Statements · Extract Helper · One Pile · Explaining Comments · Delete Redundant Comments. The prompt has to be met *exactly*; almost the book's shape is not the book's tidying. Extracting a class or a service is a refactoring, not a tidying.

**Tidy first?** (ch. 21) Ask: How much harder is the messy change? How immediate is the benefit? How will it amortize? How sure are you? Tidy **first** when it pays off now and you know how; **after** when waiting would cost more; **later** (Fun List) when it is a big batch without immediate payoff; **never** when the code will not change again. Economics: `cost(tidying) + cost(change after) < cost(change without)` (ch. 27). Bias toward tidying first, but "just enough" (ch. 33).

**To apply**, delegate to the `tidier` agent with the target (file / diff / symbol), the behavior change that comes next (or "just landed" for tidy-after), the test command, and commit trailers if any. It tidies one commit at a time, tests green before and after, cites chapter and page, and reports Applied / Reverted / Fun List / Never / Next.

**To plan without touching code**, read the target and `references/catalog.md`; open a `references/tidyings/NN-*.md` only to confirm a prompt you are unsure about, and `deciding.md` only when the first/after/later/never call is not obvious. Answer with tidying · location · first/after/later/never · why, in chaining order.

## References (`references/`)
- `catalog.md` — the 15 in one table, with pages.
- `tidyings/NN-<name>.md` — each chapter's prompt, move, before/after, caveats and chaining, verbatim.
- `deciding.md` — chs. 16–21: separate tidying, chaining table, batch sizes, rhythm, getting untangled, first/after/later/never.
- `forces.md` — chs. 22–33: cost, options, reversibility, coupling, cohesion, "just enough".
- `languages/java.md` — test command and Java caveats per tidying.
