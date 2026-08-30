# 12. Extract Helper

*Tidy First?*, cap. 12, pp. 25–26.

## Disparador y movimiento

> You see a block of code inside a routine that has an obvious purpose and limited interaction with the rest of the code in the routine. Extract it as a helper routine. Name the routine after the purpose (not how the routine works).
>
> The refactoring-aware among you will recognize "Extract Method" in this tidying. Executing this tidying/refactoring can be tricky without automated refactoring. That's why you should be in an environment that offers automatic refactoring. It is the 21st century, after all.

## Caso 1: cambiar un par de líneas dentro de una rutina grande

> I want to mention a couple of special cases of extracting a helper. One is when you have to change a couple of lines within a larger routine. Extract those lines as a helper, change just the lines in the helper, then, if it makes sense, inline the helper back into the calling routine. (Usually you'll find yourself growing fond of the helper and keeping it around.) So, this:
> ```
> routine()
>     ...stuff that stays the same...
>     ...stuff that needs to change...
>     ...stuff that stays the same...
> ```
> becomes:
> ```
> helper()
>     ...stuff that needs to change...
>
> routine()
>     ...stuff that stays the same...
>     helper()
>     ...stuff that stays the same...
> ```
> (If you've read ahead you'll recognize this as cohering, or creating a cohesive element. If not, don't worry, we'll get there.)

## Caso 2: expresar acoplamiento temporal

> Another case for extracting a helper is expressing temporal coupling (`a()` needs to be called before `b()`). If you see:
> ```
> foo.a()
> foo.b()
> ```
> frequently, then create:
> ```
> ab()
>     a()
>     b()
> ```

## Los helpers son vocabulario

> Fondness is not the only reason to keep helpers around. Frequently you'll find yourself wanting to use your new helper again hours or even minutes after you've created it. Interfaces become tools for thinking about problems. New interfaces emerge when we're ready to think more abstractly, to add words to our design vocabulary.
>
> Don't worry about using the helper everywhere it might apply. Using the helper can be taken care of in another tidying. (Some tools will automatically identify and modify all the places where a new helper applies. Heaven bless those tools.)

## Encadena con (cap. 17)

> After extracting a helper you may introduce a guard clause, extract explaining constants and variables, or delete redundant comments.
