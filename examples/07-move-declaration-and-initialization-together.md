# 7. Move Declaration and Initialization Together

*Tidy First?*, ch. 7, pp. 15–16.

## Prompt

> Variables and their initialization seem to drift apart sometimes. The name of a variable gives you a hint as to its role in the computation. However, the initialization reinforces the message of the name. When you come across code that separates the declaration (with a possible type) and initialization, it's harder to read. By the time you get to the initialization, you've forgotten some of the context of what the variable is *for*.

## Before

> Here's what this tidying looks like. Imagine you have some code like this:
> ```
> fn()
>     int a
>     ...some code that doesn't use a
>     a = ...
>     int b
>     ...some more code, maybe it uses a but doesn't use b
>     b = ...a...
>     ...some code that uses b
> ```

## After

> Tidy this by moving the initialization up to the declaration:
> ```
> fn()
>     int a = ...
>     ...some code that doesn't use a
>     ...some more code, maybe it uses a but doesn't use b
>     int b = ...a...
>     ...some code that uses b
> ```
> Play around with the order. Is it easier to read and understand the code if each of the variables is declared and initialized just before it's used, or if they're all declared and initialized together at the top of the function? This is where you get to be a mystery writer, imagining the experience of a reader of your code and leaving them the clues they need to guess who done it.

## Caveat — data dependencies

> You can't just put variables and code that sets them in any old order. You must respect the data dependencies between variables. If you use `a` to initialize `b`, you have to initialize `a` first.
>
> If you have to analyze data dependencies by hand, you are going to eventually make mistakes. You'll accidentally change the behavior of the code when you were just trying to improve its structure. No problem. Back up to a known correct version of the code. Work in smaller steps. That's the tidying way. Big design changes too hard and scary? Take smaller steps. No, smaller. Still scary? No? Good.
