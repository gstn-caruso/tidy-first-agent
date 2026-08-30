# Catalog of tidyings — Part I of *Tidy First?*

One file per chapter, with the whole chapter **exactly as it appears in the book** (Beck's pseudocode, untranslated), split under English headings: prompt, move, before/after, caveats. Each one closes with what it chains into according to ch. 17.

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

Source: Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. ISBN 978-1-098-15124-9.
