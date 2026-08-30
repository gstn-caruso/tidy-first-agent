# 2. Dead Code

*Tidy First?*, cap. 2, p. 5.

## Movimiento

> Delete it. That's all. If the code doesn't get executed, just delete it.

## Los sesgos que lo frenan

> Deleting dead code can feel mighty strange. After all, someone took the time and effort to write it. The organization paid for it. There it is. All somebody has to do to make it valuable is call it again. If we need it again, we'll be sad we deleted it.
>
> I'll leave it as an exercise for you, tidy reader, to identify all the cognitive biases I just demonstrated.

## Pre-tidying cuando no estás seguro

> Sometimes it's easy to identify dead code. Sometimes, because of extensive use of reflection, it's not so easy. If you suspect code isn't used, pre-tidy it by logging its use. Put the pre-tidying into production and wait until you're confident.

## "¿Y si lo necesitamos después?"

> You might ask, "But what if we need it later?" That's what version control is for. We aren't really deleting anything. We just don't have to look at it right now. If (and this is a long string of conditionals) we 1) have a lot of code that 2) isn't used right now that 3) we want to use in the future 4) in exactly the same way it was originally written and 5) it still works, then yes, we can get it back. Or we can just write it again, and better. But if worse comes to worst, we can always get it back.

## Tamaño del paso

> As always, delete only a little code in each tidying diff. That way, if it turns out you were wrong it will be relatively easy to revert the change (see Chapter 28). "A little" is a cognitive measure, not a lines-of-code measure. It could be one clause in a conditional (e.g., you see the condition reduces to true), one routine, one file, one directory.

## Encadena con (cap. 17)

> Once you've removed the clutter of dead code, you may be able to see how to sort the code into reading order or cohesion order.
