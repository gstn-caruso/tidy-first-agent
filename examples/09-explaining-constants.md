# 9. Explaining Constants

*Tidy First?*, cap. 9, p. 19.

## Disparador

> So you're reading along, and you see a number you don't recognize. Or you're reading along and you see a constant string repeated all over the code. You figure out what the constant *means*.

## Movimiento

> Create a symbolic constant. Replace uses of the literal constant with the symbol.

## Antes

> I mean, c'mon. I've been seeing this advice since I was a wee little programmer and yet still somehow folks think this is okay:
> ```
> if response.code = 404
>     ...blah blah blah...
> ```

## Después

> Okay, I got blame-y there for a second. We're not here to judge the person who made the mess (pro tip: it might be us). We're here to take care of ourselves by tidying first before changing things:
> ```
> PAGE_NOT_FOUND := 404
> if response.code = PAGE_NOT_FOUND
>     ...blah blah blah...
> ```

## Cuidado — el mismo literal puede significar cosas distintas

> Be careful. The same literal can appear in two places and mean something different. It doesn't help to tidy to:
> ```
> ONE = 1
> ...ONE... # everywhere you need unity
> ```
> You're reading. You understand. You're putting that understanding into the code so you don't have to hold it in your head.

## Lo que sigue

> There are a few tidyings downstream of this one about putting constants that change together or need to be understood together in one place and separating them from constants that cluster for other reasons. I'm going to let you figure those out. Coupling, cohesion, just do your thing.

## Encadena con (cap. 17)

> Extracting an explaining constant leads to cohesion order. Grouping constants that change in sync eases future changes.
>
> There are whole philosophies about where to put constants and how to arrange them. I won't get into all that here—pick something that makes your work easy. Well, easier.
