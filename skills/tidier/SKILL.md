---
name: tidier
description: |
  Kent Beck's Tidy First? in the current session — what a tidying is, the book's 15, and when to tidy
  first / after / later / never. Deciding happens here; applying is delegated to the `tidier` agent,
  which does one tidying per invocation as one structural commit. Use it for "tidy first", "tidy this
  before I add X", "limpiá esto antes de la feature", "which tidyings apply here", "separate
  structural from behavioral", "this commit mixes refactor and feature", "tidy after". Not for
  behavior changes, bug fixes, or refactorings that extract a class or a service.
---

# Tidy First?

**The rule.** A commit is one tidying or one behavior change, never both — and they go in separate PRs (ch. 16).

**A tidying** is a tiny, reversible structural change that makes the next behavior change easier. The book has fifteen (chs. 1–15): Guard Clauses · Dead Code · Normalize Symmetries · New Interface, Old Implementation · Reading Order · Cohesion Order · Move Declaration and Initialization Together · Explaining Variables · Explaining Constants · Explicit Parameters · Chunk Statements · Extract Helper · One Pile · Explaining Comments · Delete Redundant Comments. The prompt has to be met *exactly* — almost the book's shape is not the book's tidying. Extracting a class or a service is a refactoring, not a tidying.

**Tidy first?** (ch. 21) How much harder is the messy change? How immediate the benefit? How does it amortize? How sure are you? **First** when it pays off now and you know how · **after** when waiting would cost more · **later** (Fun List) for a batch with no immediate payoff · **never** when the code will not change again. The economics: `cost(tidying) + cost(change after) < cost(change without)` (ch. 27). Bias toward first, "just enough" (ch. 33).

**To apply, delegate to the `tidier` agent**: target (file / diff / symbol), the behavior change that comes next (or "just landed" for tidy-after), the test command, trailers if any. It applies **one** tidying as one structural commit, tests green either side, and reports Applied / Reverted / Fun List / Never / Pending / Next. Re-invoke while `## Next` names a tidying, handing back its `## Pending` as `plan` so detection is not paid twice.

**To plan without touching code**, read the target and answer tidying · location · first/after/later/never · why. Open `references/NN-<slug>.md` only to confirm a prompt you doubt.

## References (`references/`)
Not loaded automatically. The 33 chapters verbatim, one file each, plus `java.md`; `references/README.md` maps question → chapter. Chapters 16–33 end in a `## For the tidier` block carrying that chapter's decision rules — take the block, never the chapter: `awk '/^## For the tidier/{f=1} f' references/21-*.md`.
