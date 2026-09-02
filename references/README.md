# References — *Tidy First?*, chapters 1–33

Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. ISBN 978-1-098-15124-9. Every chapter is here **verbatim**, split under English headings. Chapters 16–33 close with a **For the tidier** block — that chapter's decision rules, distilled, the only non-verbatim text in the corpus. Each bullet cites the section it comes from.

Nothing here is loaded automatically. The `tidier` agent carries the catalog in its prompt and opens **one** of these files at a time, when it needs it. This index is the read map.

For chapters 16–33, what gets read is the block, not the chapter — it is around a fifth of the size and it is the part written to be acted on:

```sh
awk '/^## For the tidier/{f=1} f' references/21-*.md
```

The chapter body is for quoting from once the decision is made.

## When to open what

| Situation | Open |
|---|---|
| About to apply tidying `N` | `NN-*.md` — its exact prompt, the move, the caveats, and what it chains into |
| The first/after/later/never call is not obvious | `21-*` — its block carries the whole four-way switch; then `27-*` for the inequality |
| Tidying and behavior are already tangled in the tree | `20-*` |
| Wondering how many tidyings to put in one batch, or when to stop | `18-*`, `19-*` |
| One tidying seems to open another | `17-*` |
| The mess is "if I touch this I have to touch that" | `29-*`, then `32-*` |
| Deciding whether a change is safe to try at all | `28-*` |
| The target is Java | `java.md` — test-command detection and per-tidying Java caveats |

## Part I — The tidyings (chs. 1–15)

> Those of you familiar with refactoring will see great similarity between refactorings, defined as changes to structure that don't change behavior, and tidyings. Tidyings are a subset of refactorings. Tidyings are the cute, fuzzy little refactorings that nobody could possibly hate on.

— Part I, introduction (p. 1).

| # | Tidying | Prompt (in one line) | Page |
|---|---|---|---|
| [01](01-guard-clauses.md) | Guard Clauses | `if (condition) ...all the rest of the routine...` | 3 |
| [02](02-dead-code.md) | Dead Code | code that never runs | 5 |
| [03](03-normalize-symmetries.md) | Normalize Symmetries | the same thing written several ways (e.g. lazy init) | 7 |
| [04](04-new-interface-old-implementation.md) | New Interface, Old Implementation | the interface you have to call is awkward | 9 |
| [05](05-reading-order.md) | Reading Order | the key detail was at the end of the file | 11 |
| [06](06-cohesion-order.md) | Cohesion Order | one change forces you to touch several scattered places | 13 |
| [07](07-move-declaration-and-initialization-together.md) | Move Declaration and Initialization Together | `int a` far from `a = ...` | 15 |
| [08](08-explaining-variables.md) | Explaining Variables | a big, hairy expression | 17 |
| [09](09-explaining-constants.md) | Explaining Constants | `404`, a literal you finally understood | 19 |
| [10](10-explicit-parameters.md) | Explicit Parameters | data arriving in a map / env var, not as a parameter | 21 |
| [11](11-chunk-statements.md) | Chunk Statements | "this part does this and that part does that" | 23 |
| [12](12-extract-helper.md) | Extract Helper | a block with an obvious purpose and little interaction with the rest | 25 |
| [13](13-one-pile.md) | One Pile | so many small pieces it's hard to follow | 27 |
| [14](14-explaining-comments.md) | Explaining Comments | "ah, that's what's going on!" — write it down | 29 |
| [15](15-delete-redundant-comments.md) | Delete Redundant Comments | the comment says exactly what the code says | 31 |

## Part II — Managing (chs. 16–21)

> Just being able to identify that a tidying applies and applying it doesn't mean you've mastered tidying. The title of this book is Tidy First?, with emphasis on the question mark. I wanted to acknowledge that just because you can tidy doesn't mean you should tidy.

— Part II, introduction (p. 33).

| # | Chapter | Core idea | Page |
|---|---|---|---|
| [16](16-separate-tidying.md) | Separate Tidying | tidyings in their own PRs, as few as possible per PR | 35 |
| [17](17-chaining.md) | Chaining | table of which tidying enables which; "potato chips" | 39 |
| [18](18-batch-sizes.md) | Batch Sizes | collisions, interactions, speculation vs. cost of review | 43 |
| [19](19-rhythm.md) | Rhythm | minutes up to an hour; "pave the path" | 47 |
| [20](20-getting-untangled.md) | Getting Untangled | ship / untangle / discard and redo tidy-first | 49 |
| [21](21-first-after-later-never.md) | First, After, Later, Never | the answer to the title: *it depends*, and on what | 51 |

## Part III — Theory (chs. 22–33)

> Understanding theory optimizes application. The forever questions in software design are: When do I start making software design decisions? When do I stop making software design decisions and get on with changing the behavior of the system? How do I make the next decision?

— Part III, introduction (p. 55).

| # | Chapter | Core idea | Page |
|---|---|---|---|
| [22](22-beneficially-relating-elements.md) | Beneficially Relating Elements | design = elements, relationships, and the benefit of those relationships | 57 |
| [23](23-structure-and-behavior.md) | Structure and Behavior | behavior creates value today; structure creates *options* | 61 |
| [24](24-economics-time-value-and-optionality.md) | Economics: Time Value and Optionality | earn sooner / spend later, and create options under uncertainty | 65 |
| [25](25-a-dollar-today.md) | A Dollar Today > A Dollar Tomorrow | time value pushes toward *tidy after* — unless tidy first is cheaper overall | 67 |
| [26](26-options.md) | Options | "what behavior can I implement next" has value on its own | 69 |
| [27](27-options-versus-cash-flows.md) | Options Versus Cash Flows | `cost(tidying) + cost(change after) < cost(change without)` | 73 |
| [28](28-reversible-structure-changes.md) | Reversible Structure Changes | structure changes undo with a gesture — hence "just tidying" | 75 |
| [29](29-coupling.md) | Coupling | coupled *with respect to a change*: `coupled(E1, E2, Δ) ≡ ΔE1 ⇒ ΔE2` | 77 |
| [30](30-constantines-equivalence.md) | Constantine's Equivalence | `cost(software) ~= cost(change) ~= cost(big changes) ~= coupling` | 81 |
| [31](31-coupling-versus-decoupling.md) | Coupling Versus Decoupling | pay for coupling or pay for decoupling; don't squeeze out the last drop | 85 |
| [32](32-cohesion.md) | Cohesion | what's coupled goes together; what isn't goes elsewhere, one at a time | 89 |
| [33](33-conclusion.md) | Conclusion | the four forces — cost, revenue, coupling, cohesion — and you | 91 |

## Language notes

- [`java.md`](java.md) — test-command detection, what only *looks* dead under Spring/JPA/reflection, and the per-tidying Java caveats.
