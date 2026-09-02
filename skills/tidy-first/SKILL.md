---
name: tidy-first
description: |
  Kent Beck's Tidy First? for the main session — what a tidying is, the book's 15, and when to tidy
  first / after / later / never. Planning and deciding happen here; applying is delegated to the
  `tidier` agent. Use it for "tidy first", "tidy antes de la feature", "limpiá esto antes de X",
  "which tidyings apply here", "separate structural from behavioral", "this commit mixes refactor
  and feature". WHERE a responsibility lives is `responsibility-driven-design`; WHAT to call the
  refactoring is `tactical-patterns`.
---

# Tidy First?

**The rule.** A commit is one tidying or one behavior change, never both — and they go in separate PRs (ch. 16).

**A tidying** is a tiny, reversible structural change that makes the next behavior change easier. The book has fifteen (chs. 1–15): Guard Clauses · Dead Code · Normalize Symmetries · New Interface, Old Implementation · Reading Order · Cohesion Order · Move Declaration and Initialization Together · Explaining Variables · Explaining Constants · Explicit Parameters · Chunk Statements · Extract Helper · One Pile · Explaining Comments · Delete Redundant Comments. The prompt has to be met *exactly* — almost the book's shape is not the book's tidying. Extracting a class or a service is a refactoring, not a tidying.

**Tidy first?** (ch. 21) How much harder is the messy change? How immediate is the benefit? How will it amortize? How sure are you? **First** when it pays off now and you know how; **after** when waiting would cost more; **later** (Fun List) for a big batch with no immediate payoff; **never** when the code will not change again. The economics: `cost(tidying) + cost(change after) < cost(change without)` (ch. 27). Bias toward tidying first, "just enough" (ch. 33).

**To apply, delegate to the `tidier` agent** — target (file / diff / symbol), the behavior change that comes next (or "just landed" for tidy-after), the test command, and commit trailers if any. It applies **one** tidying per invocation as one structural commit, tests green before and after, and reports Applied / Reverted / Fun List / Never / Pending / Next. Re-invoke it while `## Next` says there is pending work, handing back its `## Pending` as `plan` so it does not pay for detection twice.

**To plan without touching code**, read the target and answer with tidying · location · first/after/later/never · why. Do not read the whole corpus for that: `references/NN-<slug>.md` only to confirm a prompt you are unsure about, `references/21-first-after-later-never.md` only when the call is not obvious.

## References (`references/`)
Not loaded automatically. All 33 chapters verbatim, one file per chapter, plus `java.md`; `references/README.md` maps question → chapter. Chapters 22–33 close with a **For the tidier** block — the decision rule distilled from that chapter.
