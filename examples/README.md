# Catálogo de tidyings — Parte I de *Tidy First?*

Un archivo por capítulo, con el capítulo entero **tal cual aparece en el libro** (pseudocódigo de Beck, sin traducir), partido bajo encabezados en castellano: disparador, movimiento, antes/después, cuidados. Cada uno cierra con lo que encadena según el cap. 17.

> Those of you familiar with refactoring will see great similarity between refactorings, defined as changes to structure that don't change behavior, and tidyings. Tidyings are a subset of refactorings. Tidyings are the cute, fuzzy little refactorings that nobody could possibly hate on.

— Parte I, introducción (p. 1).

| # | Tidying | Disparador (en una línea) | Página |
|---|---|---|---|
| [01](01-guard-clauses.md) | Guard Clauses | `if (condition) ...all the rest of the routine...` | 3 |
| [02](02-dead-code.md) | Dead Code | código que no se ejecuta | 5 |
| [03](03-normalize-symmetries.md) | Normalize Symmetries | lo mismo escrito de varias formas (ej: lazy init) | 7 |
| [04](04-new-interface-old-implementation.md) | New Interface, Old Implementation | la interfaz que tenés que llamar es incómoda | 9 |
| [05](05-reading-order.md) | Reading Order | el detalle clave estaba al final del archivo | 11 |
| [06](06-cohesion-order.md) | Cohesion Order | para un cambio tenés que tocar varios lugares dispersos | 13 |
| [07](07-move-declaration-and-initialization-together.md) | Move Declaration and Initialization Together | `int a` lejos de `a = ...` | 15 |
| [08](08-explaining-variables.md) | Explaining Variables | expresión grande y peluda | 17 |
| [09](09-explaining-constants.md) | Explaining Constants | `404`, un literal que entendiste | 19 |
| [10](10-explicit-parameters.md) | Explicit Parameters | datos que llegan en un map / env var, no como parámetro | 21 |
| [11](11-chunk-statements.md) | Chunk Statements | "esta parte hace esto y esa parte hace aquello" | 23 |
| [12](12-extract-helper.md) | Extract Helper | bloque con propósito obvio y poca interacción con el resto | 25 |
| [13](13-one-pile.md) | One Pile | tantas piezas chicas que no se entiende | 27 |
| [14](14-explaining-comments.md) | Explaining Comments | "ah, ¡esto es lo que pasa!" — anotalo | 29 |
| [15](15-delete-redundant-comments.md) | Delete Redundant Comments | el comentario dice exactamente lo que dice el código | 31 |

Fuente: Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. ISBN 978-1-098-15124-9.
