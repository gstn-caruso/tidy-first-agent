# Managing — Part II of *Tidy First?*

The discipline of fitting tidyings into the workflow: when to start, when to stop, how to separate them from the behavior change.

> The mechanics of the tidyings will come to you with practice. Most of them require no automated support. […] I want you to get used to designing software a little at a time, all the time. Tidyings are gateway refactorings.
>
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

The *why* behind all this — economics, reversibility, coupling, cohesion — is in Part III: [`../theory/`](../theory/README.md). What the agent uses most often from there is **ch. 28, Reversible Structure Changes** (pp. 75–76) — *"structure changes are generally reversible. You extract a helper function and you don't like it? Inline it. It's like that helper never existed."* That's why a failed tidying reverts without drama.
