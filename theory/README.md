# Theory — Part III of *Tidy First?*

The *why* behind the tidyings: what design is, how structure and behavior differ, the economics pulling each way, and the two forces the book puts at the center — coupling and cohesion. Each file carries the chapter verbatim under English headings and closes with a **For the tidier** block: the decision rule the agent takes away from that chapter.

| # | Chapter | Core idea | Page |
|---|---|---|---|
| [22](22-beneficially-relating-elements.md) | Beneficially Relating Elements | design = elements, relationships, and the benefit of those relationships; a designer can only create/delete elements, create/delete relationships, or increase the benefit of one | 57 |
| [23](23-structure-and-behavior.md) | Structure and Behavior | behavior creates value today; structure creates *options*; the underlying difference is reversibility | 61 |
| [24](24-economics-time-value-and-optionality.md) | Economics: Time Value and Optionality | two clashing imperatives of money: earn sooner / spend later, and create options in the face of uncertainty | 65 |
| [25](25-a-dollar-today.md) | A Dollar Today > A Dollar Tomorrow | time value pushes toward *tidy after* — unless tidy first makes the total cheaper, in which case "always tidy first" | 67 |
| [26](26-options.md) | Options | "what behavior can I implement next" has value on its own; the more volatile, the more valuable the option | 69 |
| [27](27-options-versus-cash-flows.md) | Options Versus Cash Flows | the inequality `cost(tidying) + cost(change after) < cost(change without)`, and the terrain of judgment when it doesn't hold | 73 |
| [28](28-reversible-structure-changes.md) | Reversible Structure Changes | structure changes undo with a gesture — hence "just tidying"; the irreversible (extracting a service) gets thought through slowly | 75 |
| [29](29-coupling.md) | Coupling | coupled *with respect to a change*: `coupled(E1, E2, Δ) ≡ ΔE1 ⇒ ΔE2`; 1–N and cascades | 77 |
| [30](30-constantines-equivalence.md) | Constantine's Equivalence | `cost(software) ~= cost(change) ~= cost(big changes) ~= coupling` | 81 |
| [31](31-coupling-versus-decoupling.md) | Coupling Versus Decoupling | pay for coupling or pay for decoupling; don't squeeze out the last drop | 85 |
| [32](32-cohesion.md) | Cohesion | what's coupled goes together (extract a cohesive subelement) and what's not coupled goes elsewhere; one element at a time | 89 |
| [33](33-conclusion.md) | Conclusion | the four forces — cost, revenue, coupling, cohesion — and you; "Tidy first? Likely yes. Just enough. You're worth it." | 91 |

## Why it is here

> Now that we've seen what to tidy and how and when to tidy, we can discuss why to tidy. You don't need to know exactly how a medication works to experience its effects, but knowing how it works gives you a deeper appreciation of it and allows you to use the medication in novel circumstances.
>
> Theory doesn't convince. No one is going to say, "Tidying is bullshit. Oh, wait, you're creating optionality. I guess it's a good idea after all."
>
> Understanding theory optimizes application. The forever questions in software design are:
> - When do I start making software design decisions?
> - When do I stop making software design decisions and get on with changing the behavior of the system?
> - How do I make the next decision?

— Part III, introduction (p. 55).

Source: Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. ISBN 978-1-098-15124-9.
