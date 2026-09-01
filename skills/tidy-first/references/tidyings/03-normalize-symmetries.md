# 3. Normalize Symmetries

*Tidy First?*, ch. 3, pp. 7–8.

## Prompt

> In growing organically, the same problem may be solved differently at different times or by different people. That's okay, but it makes for difficult reading. As a reader, you'd like consistency. If you see a pattern, you can confidently jump to the conclusion that you know what's going on.

## Example: lazily initialized variables

> Take the example of lazily initialized variables. You might see them written different ways:
> ```
> foo()
>     return foo if foo not nil
>     foo := ...
>     return foo
>
> foo()
>     if foo is nil
>         foo := ...
>     return foo
>
> # tricky
> foo()
>     return foo not nil
>         ? foo
>         : foo := ...
>
> # doubly tricky, assuming assignment is an expression
> foo()
>     return foo := foo not nil
>         ? foo
>         : ...
>
> # even trickier, hiding the conditional
> foo()
>     return foo := foo || ...
> ```
> (See if you can find or invent more variants.)
>
> All of these are ways of saying, "Compute and cache a value for foo if we haven't already." Each has its pros and cons. You as a reader will quickly get acclimated to any one of them. Things get confusing when two or more of the patterns are used interchangeably. As a reader, you expect that difference means difference. Here you have difference that obscures the fact that the same thing is going on.

## The move

> Pick a way. Convert one of the variants into that way. Tidy one form of unnecessary variation at a time—lazy initialization, for example, first.
>
> Sometimes the commonality is hidden by extra detail. Look for routines that are similar but not identical. Separate the different parts from the identical parts.

## Chains into (ch. 17)

> Once you've made identical code identical and different code different, you may be able to group precisely parallel code into reading order. I did this once with a file containing several web entry points. Once they all looked alike, it was natural to group them at the top of the file as a kind of table of contents to the rest of the code.
