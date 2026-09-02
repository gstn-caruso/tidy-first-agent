# 29. Coupling

*Tidy First?*, ch. 29, pp. 77–79.

## Yourdon and Constantine: the origin of the term

> To prepare to write their classic text *Structured Design*, Ed Yourdon and Larry Constantine examined programs to find out what made them so expensive. They noticed that the expensive programs all had one property in common: changing one element required changing other elements. The cheap programs tended to require localized changes.
>
> They dubbed this change infection property "coupling." Two elements are coupled with respect to a particular change if changing one element necessitates changing the other element.

## Example: coupling with respect to what change

> For example, a calling function is coupled to a called function with respect to changes to the name of the called function:
> ```
> caller()
>     called()
>
> called() // changing this name requires changing the call site(s) too
>     ... // changing the formatting of the body requires no changes to call sites
> ```
> The second comment here emphasizes an important nuance of coupling: we can't just say that two elements are coupled. To say something useful, we have to also say coupled with respect to which changes. If two elements are coupled with respect to a change that never happens, then they aren't coupled in a way that should concern us. That coupling is the boulder at the top of the hill that never rolls down to crush the village.

## Coupling can't be seen just by looking at the code

> Analyzing coupling cannot be done simply by looking at the source code of a program. We need to know what changes have happened and/or are likely to happen before we can tell whether two elements are coupled. (For an experiment, see which pairs of files tend to show up together in commits. Those files are coupled.)

## Formal definition and Figure 29-1

> Coupling drives the cost of software. Because coupling is so fundamental, I express and visualize it in as many ways as I can. As a math-ish definition:
> ```
> coupled(E1, E2, Δ) ≡ ΔE1 ⇒ ΔE2
> ```
> Figure 29-1 shows this as an image.
>
> *(Figura 29-1: Called function coupled to calling function with respect to name changes)*

## 1–N and cascading

> If coupling were only ever between two elements, then it wouldn't haunt our nightmares. Instead, coupling has two properties that drag it center stage:
>
> **1–N**
>
> One element can be coupled with any number of other elements with respect to a change.
>
> **Cascading**
>
> Once a change has rippled from one element to another, that implied change can trigger another round of changes, which can themselves trigger changes of their own.
>
> The 1–N problem can be eliminated to some degree with tooling. If you have an automated refactoring to change a function name and all callers, then you can make a single change. The cost is the same whether you have one or one thousand callers. (Although if you're changing one thousand callers at once, you may want to get that change into production all by itself as quickly as possible.)
>
> Cascading changes are the bigger issue. As we will see in the next book, the cost of changes follows a power law distribution. This distribution is created by the cost of cascading changes. You will be using software design to reduce the probability and magnitude of cascading changes.

## Devalued coupling, and "connascence"

> The word "coupling" has lost its meaning over time, coming to mean any relationship between elements in a system. "This service is coupled with that service"—okay, but how? With respect to what changes? It's not enough to know that one service invokes another; we need to know what changes to one service would require changes to the other.
>
> Meilir Page-Jones used the word "connascence" to describe coupling in his book *What Every Programmer Should Know About Object-Oriented Design* (Dorset House). Since the definitions are exactly the same, I just say "coupling."

## Subtle coupling: the Facebook case

> In large, complex systems, coupling can be subtle. Indeed, when we say a system is "complex," we mean that changes have unexpected consequences. I remember an incident at Facebook where two services shared the same physical rack. One service changed its backup policy from incremental backups to complete backups. These backups saturated the network switch located on top of the rack, causing the second service to fail. The two services were coupled with respect to changes to the backup policy, even though the two teams working on the services weren't even aware of each other.

## Coupling and tidy first

> What does coupling mean for answering the question, "Should I tidy first?" Sometimes when you're staring at a messy change, it's coupling that's harshing your mellow: "But if I change this, then I'll have to change all those too." Messy. Take a minute to go through the list of tidyings and see which of them would reduce coupling.
>
> Coupling drives the cost of software. Next, we'll look at exactly how.

## For the tidier

- From "Example: coupling with respect to what change": before saying "this is coupled," ask coupled with respect to what change — if that change is never going to happen, the coupling doesn't matter and isn't worth tidying.
- From "Coupling can't be seen just by looking at the code": to know what's coupled to what, also look at the history (which files show up together in commits), not just the static structure.
- From "1–N and cascading": prioritize tidyings that cut cascades of changes (one change triggers another which triggers another) over ones that merely bring N sites down to 1 — 1–N gets solved with tooling, cascading doesn't.
- From "Coupling and tidy first": when a change feels heavy because "if I touch this I have to touch that too," go through the list of tidyings looking for the one that specifically reduces that coupling before moving on.
