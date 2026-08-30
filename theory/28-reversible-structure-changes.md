# 28. Reversible Structure Changes

*Tidy First?*, cap. 28, pp. 75–76.

## Corte de pelo vs. tatuaje

> What's the difference between a bad haircut and a bad tattoo? The bad haircut grows out, but the bad tattoo is forever (well, not forever forever, but it's way harder to undo).
>
> How are structure changes different from behavior changes? One property relevant to tidying first is that structure changes are generally reversible. You extract a helper function and you don't like it? Inline it. It's like that helper never existed.

## Decisiones reversibles e irreversibles

> Contrast this with a regrettable behavior change. Let's say you've sent out 100,000 tax notices with the wrong number on them. Now what? Well, it'll cost you plenty to fix them. The damage to your reputation may be permanent. If only you'd caught that problem five minutes *before* you sent the notices instead of five minutes *after*.
>
> In general, we should treat reversible decisions differently than irreversible decisions. There's great value in reviewing, double-checking, triple-checking irreversible decisions. The pace should be slow and deliberate. Even if there is a great upside to the decision, there is also potentially a great downside if we get it wrong. Yes, we want the upside, but even more we want to avoid the downside.
>
> How about reversible decisions? Most software design decisions are easily reversible. There is some upside to making them (making behavior changes easier, as we've seen throughout this book). But there's really not much downside, because we can so easily reverse a decision if it turns out to be wrong.
>
> Because there is so little value to avoiding mistakes, we shouldn't invest much in doing so. That's the economic reality I was hinting at when choosing "tidying" to describe what we're doing in this book. It's no big deal. Just tidying.

## Cuando el code review no distingue

> Code review processes (which I've promised multiple times to trash, but now is not the time) don't distinguish between reversible and irreversible changes. We end up making the same investment with radically different payoff profiles. What a waste.

## Hacer reversible lo irreversible

> What about design changes that *aren't* reversible? For example, "extract as a service" tends to be a big deal and hard to undo. Think about it some more, for example by actually implementing a prototype first. And by "implementing," I mean putting it into production. Does this require a feature flag? Okay. Does it require checking the feature flag in a whole bunch of places? Okay, tidy first so it only requires a few feature flag checks.
>
> Do you see what we're doing? We are making "extract as a service" reversible, at least for a while. If we get halfway into it and realize this is one of those services that really could have been a SQL query (thanks, Josh Wills), then we can change it without too much fuss.

## Cuando la decisión se propaga

> Another scenario where reversible design decisions become irreversible is when the decision propagates throughout the code base. Now changing from an integer to a long would require changing a million spots, some of them extremely tricky. Okay: 1) think a little more about whether this decision is one that is likely to propagate, and 2) yeah that happens, and when it happens we get out of it one tidying at a time. Tidy first or after for a while, then tidy later to finish reversing the decision. (As always, in short, interruptible slices.)

## Contra el mito de la decisión perfecta

> There seems to be an idealistic form of geek thinking that holds that if only we made decisions better, we would never make mistakes. I was a young adherent, a worshipper at the altar of "If Only I Were Infinitely Smart." Fortunately, I got over it. I learned the value of reversibility (long before I had a name for it) and realized the value of making decisions reversible.

## Para el tidier

- De "Decisiones reversibles e irreversibles": para decidir el ritmo de una decisión de diseño, preguntate primero si es reversible — si lo es, no vale la pena invertir en evitar el error, alcanza con tidy y seguir.
- De "Hacer reversible lo irreversible": si el cambio estructural que estás por hacer no es reversible (extraer un servicio, por ejemplo), tu primer movimiento es hacerlo reversible (feature flag, prototipo en producción) antes de comprometerte del todo.
- De "Cuando la decisión se propaga": si el tidying implica tocar un número creciente de sitios porque la decisión se propaga por toda la base de código, no lo hagas de una — repartilo en tidy first/after en el momento y dejá el resto para tidy later, en tandas cortas e interrumpibles.
- De "Cuando el code review no distingue": si tu proceso de review trata todo cambio estructural igual que uno irreversible, es una señal de que estás pagando de más por un tidying de bajo riesgo — no dejes que el costo del proceso te frene de tidyar.
