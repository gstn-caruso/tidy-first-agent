# 8. Explaining Variables

*Tidy First?*, cap. 8, p. 17.

## Disparador

> Some expressions grow. Even if they start small, they grow. And they grow and they grow. And then along you come with your reading glasses on, and you try to understand what's happening.

## Movimiento

> When you understand a part of a big, hairy expression, extract the subexpression into a variable named after the intention of the expression.

## Antes

> You'll see this frequently in graphics code:
> ```
> return new Point(
>     ...big long expression...,
>     ...another big long expression...
> )
> ```

## Después

> Before changing one of those expressions, consider tidying first:
> ```
> x := ...big long expression...
> y := ...another big long expression...
> return new Point(x, y)
> ```
> Or maybe the expressions mean something more specific, like width and height, top and left, run and rise.

## Por qué

> In this tidying you are taking your hard-won understanding and putting it back into the code. This sets you up to change either one of those expressions more easily (because now they are separated), and to read them more quickly next time the code needs to change.
>
> As always, separate the tidying commit from the behavior change commit.

## Encadena con (cap. 17)

> The righthand side of the assignment to an explaining variable is a candidate for an explaining helper (after which you may be able to inline the variable). The explanation offered by the variable name may make it possible to delete redundant comments.
