# The 15 tidyings — catalog

*Tidy First?* (Kent Beck, O'Reilly 2023), Part I, chs. 1–15. One line per tidying: what you see (the prompt), what you do (the move), what to watch (the caveat), and the page the chapter starts on. Full text of each: `tidyings/NN-<name>.md`.

| # | Tidying | Prompt (you see…) | Move | Caveat | Page |
|---|---|---|---|---|---|
| 1 | Guard Clauses | `if (condition) …all the rest of the routine…`, maybe nested | `if (not condition) return` up top, flat logic after | Only when the prompt is met precisely. 7–8 guards is not easier to read. | 3 |
| 2 | Dead Code | code that never executes (or a value assigned and never read) | delete it | A little per diff. If unsure (reflection), pre-tidy by logging its use. Version control keeps it. | 5 |
| 3 | Normalize Symmetries | the same thing written several ways (e.g. lazy init variants) | pick one way, convert one variant at a time | One form of variation per tidying. "Difference means difference" — make sure it does not. | 7 |
| 4 | New Interface, Old Implementation | the interface you must call is awkward | write the interface you wish you had; implement it by calling the old one | Migrate callers one at a time (fanout). Inline the old one later. | 9 |
| 5 | Reading Order | the detail that explains everything was at the end | reorder in the order a reader wants | Alone. Careful in declaration-order-sensitive languages. No perfect order. | 11 |
| 6 | Cohesion Order | one change touches several dispersed spots | put coupled elements adjacent (routines, files, repos) | Decoupling is better if you know how and can afford it. | 13 |
| 7 | Move Declaration and Initialization Together | `int a` far from `a = …` | move the initialization up to the declaration (or both down to first use) | Respect data dependencies. Mistake? Back up, smaller steps. | 15 |
| 8 | Explaining Variables | a big, hairy expression | extract the subexpression into a variable named after its intention | Separate the tidying commit from the behavior commit. | 17 |
| 9 | Explaining Constants | a literal you had to figure out (`404`) | symbolic constant, replace the literal | The same literal can mean different things in different places. `ONE = 1` helps nobody. | 19 |
| 10 | Explicit Parameters | data arrives in a map / env var, not as a parameter | split: top part gathers params, passes them explicitly to the body | Then push the params up the call chain. | 21 |
| 11 | Chunk Statements | "this part does this and that part does that" | a blank line between the parts | Simplest tidying. Don't get caught in the design vortex. | 23 |
| 12 | Extract Helper | a block with an obvious purpose and limited interaction with the rest | extract, name after purpose not mechanism | Also for temporal coupling `a(); b()` → `ab()`. Don't chase every call site now. | 25 |
| 13 | One Pile | so many tiny pieces you can't follow | inline until it's one pile, then tidy from there | Symptoms: long repeated arg lists, repeated conditionals, bad helper names, shared mutable data. | 27 |
| 14 | Explaining Comments | "oh, so that's what's going on!" | write down only what wasn't obvious, to someone specific | Best moment: right after finding a defect. | 29 |
| 15 | Delete Redundant Comments | a comment that says exactly what the code says | delete it | Only *absolutely, completely* redundant ones. Often a previous tidying made it redundant. | 31 |

Mechanically safe without a test suite (the tidier's own rule, not the book's): 15, 11, 9 (when the literal is unambiguous), 7 (when data dependencies are trivial), 14.
