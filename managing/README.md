# Managing — Parte II de *Tidy First?*

La disciplina para meter los tidyings en el flujo de trabajo: cuándo empezar, cuándo parar, cómo separarlos del cambio de comportamiento.

> The mechanics of the tidyings will come to you with practice. Most of them require no automated support. […] I want you to get used to designing software a little at a time, all the time. Tidyings are gateway refactorings.
>
> Just being able to identify that a tidying applies and applying it doesn't mean you've mastered tidying. The title of this book is Tidy First?, with emphasis on the question mark. I wanted to acknowledge that just because you can tidy doesn't mean you should tidy.

— Parte II, introducción (p. 33).

| # | Capítulo | Idea central | Página |
|---|---|---|---|
| [16](16-separate-tidying.md) | Separate Tidying | tidyings en sus propios PRs, los menos posibles por PR | 35 |
| [17](17-chaining.md) | Chaining | tabla de qué tidying habilita cuál; "potato chips" | 39 |
| [18](18-batch-sizes.md) | Batch Sizes | colisiones, interacciones, especulación vs. costo de review | 43 |
| [19](19-rhythm.md) | Rhythm | minutos hasta una hora; "pave the path" | 47 |
| [20](20-getting-untangled.md) | Getting Untangled | ship / desenredar / tirar y rehacer tidy-first | 49 |
| [21](21-first-after-later-never.md) | First, After, Later, Never | la respuesta al título: *it depends*, y de qué | 51 |

El *por qué* de todo esto — economía, reversibilidad, acoplamiento, cohesión — está en la Parte III: [`../theory/`](../theory/README.md). Lo que el agente usa a cada rato de ahí es el **cap. 28, Reversible Structure Changes** (pp. 75–76) — *"structure changes are generally reversible. You extract a helper function and you don't like it? Inline it. It's like that helper never existed."* Por eso un tidying fallido se revierte sin drama.
