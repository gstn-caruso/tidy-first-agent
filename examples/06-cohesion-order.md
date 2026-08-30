# 6. Cohesion Order

*Tidy First?*, cap. 6, p. 13.

## Disparador

> You read the code, you figure out that to make a behavior change you're going to have to change several widely dispersed spots in the code, and you get grumpy. What should you do?

## Movimiento

> Reorder the code so the elements you need to change are adjacent. Cohesion order works for routines in a file: if two routines are coupled, put them next to each other. It also works for files in directories: if two files are coupled, put them in the same directory. It even works across repositories: put coupled code in the same repository before changing it.

## ¿Por qué no eliminar el acoplamiento directamente?

> Why not just eliminate the coupling? If you know how to do that, go for it. That's the best tidying of all, assuming:
> ```
> cost(decoupling) + cost(change) < cost(coupling) + cost(change)
> ```
> It may not be feasible, though, for various reasons:
> - Decoupling can be an intellectual stretch (you don't know how to do it).
> - Decoupling can be a time/money stretch (you could do it, but you can't afford to take that time just now).
> - Decoupling can be a relationship stretch (the team has taken as much change as it can handle right now).
>
> You aren't stuck with Swiss cheese changes. Tidying can increase cohesion enough to make behavior changes easier. Sometimes the increased clarity from slightly better cohesion unlocks whatever is blocking you from decoupling. Sometimes better cohesion helps you live with the coupling.

## Encadena con (cap. 17)

> Elements grouped together for cohesion order are candidates to be extracted into a subelement. Creating, for example, a helper object is out of the scope of tidying. As you get comfortable and confident in tidying, though, it's natural to see larger-scale design changes that will ease further behavior changes.
