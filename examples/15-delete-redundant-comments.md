# 15. Delete Redundant Comments

*Tidy First?*, cap. 15, pp. 31–32.

## Disparador y movimiento

> When you see a comment that says exactly what the code says, remove it.
>
> There's no mechanism to double-check the accuracy of prose as the system changes, and comments might become redundant as the code evolves.

## Ejemplo 1: el comentario dogmático

> ```
> getX()
>   # return X
>   return X
> ```
> This comment provides costs without benefits. As a writer, you've just wasted the reader's time—time they can't recover. If a comment is completely redundant, then delete it.

## Ejemplo 2: un tidying previo lo volvió redundante

> Tidyings often chain together. A previous tidying may have made a comment redundant. For example, the original code might look like this:
> ```
> if (generator)
>      ...a bunch of lines of code to set up the generator...
> else
>      # no generator, return the default
>      return getDefaultGenerator()
> ```
> After tidying with a guard clause, the code looks like this:
> ```
> if (! generator)
>     # no generator, return the default
>     return getDefaultGenerator()
> ...a bunch of lines of code to set up the generator...
> ```
> The comment isn't redundant at first. It returns our attention to the current context (no generator present) after reading a bunch of lines of code in a different context (generator present, needs setup). After tidying, however, the comment is a simple restatement of what the code says. So, let's delete it.

## Cuidado — solo lo *absolutamente* redundante (cap. 17)

> I'm going to emphasize once again, since I get accused of being anti-comment, that you should only delete absolutely, completely redundant comments. You should also tidy with an eye toward making comments absolutely, completely redundant.

## Encadena con (cap. 17)

> Eliminating the noise of redundant comments can help you see a better reading order or see the chance for explicit parameters.
