# 13. One Pile

*Tidy First?*, cap. 13, pp. 27–28.

## Disparador y movimiento

> Sometimes you read code that's been split into many tiny pieces, but in a way that hinders you from understanding it. Inline as much of the code as you need until it's all in one big pile. Tidy from there.

## Por qué va contra el sesgo habitual

> The biggest cost of code is the cost of reading and understanding it, not the cost of writing it. Tidy first has a bias toward lots of little pieces, both theoretically, to increase cohesion as a path to reducing coupling, and practically, to reduce the amount of detail that needs to be held in your head at any one time.
>
> The goal of this bias toward small pieces is to enable the code to be understood a little at a time. Sometimes, though, this process goes wrong. Because of how the small pieces interact, the code is harder to understand. To regain clarity, the code must first be mooshed together so new, easier-to-understand parts can then be extracted.

## Síntomas

> Some symptoms you're looking for are:
>
> - Long, repeated argument lists
> - Repeated code, especially repeated conditionals
> - Poor naming of helper routines
> - Shared mutable data structures

## Cómo se siente

> Given the bias toward more, smaller pieces, creating one pile feels odd while tidying. However, it's strangely satisfying. I've been trying to understand the code in pieces. I'm starting to doubt my own abilities. I turn 180 degrees and start lumping it all together (it really helps to have automated refactorings for this, but I'll do it manually if I have to). What a relief!
>
> As the pile gets bigger, the shape starts to emerge in my mind. I see—first we calculate this, then we use it to calculate that! Why didn't they just say so? Now I get to ask the title question: should I tidy first? Or just make the change I can now see?

## Encadena con (cap. 17)

> After making a big, obvious mess, expect to tidy by chunking statements, adding explaining comments, and extracting helpers.
