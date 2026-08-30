# Theory — Parte III de *Tidy First?*

El *por qué* de los tidyings: qué es diseño, en qué se diferencian estructura y comportamiento, la economía que tira para cada lado, y las dos fuerzas que el libro pone en el centro — acoplamiento y cohesión. Cada archivo trae el capítulo verbatim bajo encabezados en castellano y cierra con un bloque **Para el tidier**: la regla de decisión que el agente se lleva de ese capítulo.

| # | Capítulo | Idea central | Página |
|---|---|---|---|
| [22](22-beneficially-relating-elements.md) | Beneficially Relating Elements | diseño = elementos, relaciones y el beneficio de esas relaciones; un diseñador solo puede crear/borrar elementos, crear/borrar relaciones, o aumentar el beneficio de una | 57 |
| [23](23-structure-and-behavior.md) | Structure and Behavior | el comportamiento crea valor hoy; la estructura crea *opciones*; la diferencia de fondo es la reversibilidad | 61 |
| [24](24-economics-time-value-and-optionality.md) | Economics: Time Value and Optionality | dos imperativos del dinero que chocan: ganar antes / gastar después, y crear opciones ante la incertidumbre | 65 |
| [25](25-a-dollar-today.md) | A Dollar Today > A Dollar Tomorrow | el valor temporal empuja a *tidy after* — salvo que tidy first haga más barato el total, y ahí "always tidy first" | 67 |
| [26](26-options.md) | Options | "qué comportamiento puedo implementar después" vale por sí solo; cuanto más volátil, más vale la opción | 69 |
| [27](27-options-versus-cash-flows.md) | Options Versus Cash Flows | la desigualdad `cost(tidying) + cost(change after) < cost(change without)`, y el terreno de juicio cuando no se cumple | 73 |
| [28](28-reversible-structure-changes.md) | Reversible Structure Changes | los cambios de estructura se deshacen con un gesto — por eso "just tidying"; lo irreversible (extraer un servicio) se piensa despacio | 75 |
| [29](29-coupling.md) | Coupling | acoplado *respecto de un cambio*: `coupled(E1, E2, Δ) ≡ ΔE1 ⇒ ΔE2`; 1–N y cascadas | 77 |
| [30](30-constantines-equivalence.md) | Constantine's Equivalence | `cost(software) ~= cost(change) ~= cost(big changes) ~= coupling` | 81 |
| [31](31-coupling-versus-decoupling.md) | Coupling Versus Decoupling | pagar el acoplamiento o pagar el desacople; no exprimir hasta la última gota | 85 |
| [32](32-cohesion.md) | Cohesion | lo acoplado va junto (extraer un subelemento cohesivo) y lo no acoplado va a otro lado; un elemento por vez | 89 |
| [33](33-conclusion.md) | Conclusion | las cuatro fuerzas — costo, revenue, acoplamiento, cohesión — y vos; "Tidy first? Likely yes. Just enough. You're worth it." | 91 |

## Por qué está acá

> Now that we've seen what to tidy and how and when to tidy, we can discuss why to tidy. You don't need to know exactly how a medication works to experience its effects, but knowing how it works gives you a deeper appreciation of it and allows you to use the medication in novel circumstances.
>
> Theory doesn't convince. No one is going to say, "Tidying is bullshit. Oh, wait, you're creating optionality. I guess it's a good idea after all."
>
> Understanding theory optimizes application. The forever questions in software design are:
> - When do I start making software design decisions?
> - When do I stop making software design decisions and get on with changing the behavior of the system?
> - How do I make the next decision?

— Parte III, introducción (p. 55).

Fuente: Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. ISBN 978-1-098-15124-9.
