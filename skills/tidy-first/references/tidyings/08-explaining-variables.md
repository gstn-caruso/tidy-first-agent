# 8. Explaining Variables

*Tidy First?*, ch. 8, p. 17.

## Prompt

> Some expressions grow. Even if they start small, they grow. And they grow and they grow. And then along you come with your reading glasses on, and you try to understand what's happening.

## The move

> When you understand a part of a big, hairy expression, extract the subexpression into a variable named after the intention of the expression.

## Before

> You'll see this frequently in graphics code:
> ```
> return new Point(
>     ...big long expression...,
>     ...another big long expression...
> )
> ```

## After

> Before changing one of those expressions, consider tidying first:
> ```
> x := ...big long expression...
> y := ...another big long expression...
> return new Point(x, y)
> ```
> Or maybe the expressions mean something more specific, like width and height, top and left, run and rise.

## Chains into (ch. 17)

> The righthand side of the assignment to an explaining variable is a candidate for an explaining helper (after which you may be able to inline the variable). The explanation offered by the variable name may make it possible to delete redundant comments.
