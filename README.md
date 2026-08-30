# tidy-first-agent

Un agente de Claude Code que hace de **tidier** según *Tidy First? A Personal Exercise in Empirical Software Design* (Kent Beck, O'Reilly 2023), con los ejemplos del libro extraídos **verbatim** como material de consulta.

Dado un archivo/diff/función —idealmente junto con el cambio de comportamiento que viene después— el agente:

1. arma la red de seguridad (tests en verde, working tree limpio),
2. lee como lector y detecta qué tidyings del catálogo aplican, exigiendo que el disparador se cumpla *exactamente*,
3. decide **First / After / Later / Never** (cap. 21) y arma un plan chico (cap. 18, 19),
4. aplica **un tidying por commit**, corriendo los tests después de cada uno y revirtiendo si algo se pone rojo,
5. reporta qué aplicó, qué revirtió y qué quedó en la *Fun List*, citando capítulo y página.

Nunca cambia comportamiento. Nunca mezcla.

## Layout

```
agents/tidier.md        el agente (frontmatter + prompt); lo que se instala en ~/.claude/agents/
examples/               Parte I — los 15 tidyings, un capítulo entero por archivo, tal cual el libro
examples/README.md      índice del catálogo
managing/               Parte II — Separate Tidying, Chaining, Batch Sizes, Rhythm, Getting Untangled, First/After/Later/Never
managing/README.md      índice
theory/                 Parte III — diseño, estructura vs. comportamiento, economía, reversibilidad, acoplamiento, cohesión, Conclusion
theory/README.md        índice; cada capítulo cierra con un bloque "Para el tidier" (la regla de decisión que se lleva el agente)
install.sh              copia el agente a ~/.claude/agents/tidier.md
assets/                 el libro (pdf/epub) — ignorado por git, no se pushea; es la fuente de la que se extrajo todo lo demás
```

Los tres directorios contienen el libro **verbatim** (partes I a III, capítulos 1–33), partidos bajo encabezados en castellano. El agente lee `examples/NN-*.md` antes de aplicar cada tidying para verificar que el movimiento coincide con el del libro, `managing/21` y `theory/27` cuando la decisión first/after/later/never no es obvia, y `theory/29` y `theory/32` cuando el desorden es acoplamiento. Si las carpetas no están, trabaja con el catálogo y la tabla de fuerzas embebidos en el prompt y lo avisa.

## Instalar

```sh
./install.sh
```

Copia `agents/tidier.md` a `~/.claude/agents/tidier.md`. Claude Code relee `~/.claude/agents/` entre turnos: en una sesión abierta, `tidier` aparece en la lista de agentes a partir del próximo mensaje (si no, reiniciá la sesión).

## Usar

Desde una sesión de Claude Code, en un repo con tests:

> Usá el agente `tidier` sobre `src/orders.py`. El cambio de comportamiento que viene es: soportar descuentos por volumen en `price_for()`.

O sin cambio de comportamiento a la vista (modo "leer para entender", más conservador):

> Hacé un pase de Tidy First con `tidier` sobre `lib/parser.js`.

O después de un cambio que ya entró y dejó a la vista el desorden (modo *after*, cap. 21):

> Acabo de mergear el descuento por volumen en `price_for()`. Tidy after con `tidier`.

Qué le podés pasar: el target, el próximo cambio de comportamiento (o el que acaba de entrar), el comando de tests (si no, lo detecta) y trailers para los commits.

## Qué NO hace

- Cambios de comportamiento, ni un bugfix "ya que estoy".
- Refactors grandes: extraer un objeto/servicio, nuevas abstracciones — el libro los deja explícitamente fuera del alcance de un tidying (cap. 17) y, en el caso de los servicios, los marca como difíciles de deshacer (cap. 28).
- Seguir ordenando más allá de lo que sirve al próximo cambio de comportamiento: "Save the tidying binge for later" (cap. 33).
- Trabajar sobre una imagen viva de Cuis: ahí el estado compartido es la imagen, no el working tree; usar `cuis-tcr-tdd-driver`.

## Relación con el skill `tidy-first`

El skill `~/.claude/skills/tidy-first/` es la guía **inline** (teoría, cuándo cargarla, traducciones a Java). Este agente es el **worker**: arranca en frío, aplica y commitea. Son independientes; el agente trae sus propios ejemplos.

## Fuente

Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023. ISBN 978-1-098-15124-9. Las citas son del libro; los ejemplos están en el pseudocódigo original de Beck.
