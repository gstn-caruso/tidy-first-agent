# 14. Explaining Comments

*Tidy First?*, cap. 14, p. 29.

## Disparador y movimiento

> You know that moment when you're reading some code and you say, "Oh, so that's what's going on!" That's a valuable moment. Record it.
>
> Write down only what wasn't obvious from the code. Put yourself in the place of the future reader, or yourself 15 minutes ago. What is it that you would have liked to have known? You might make a note like, "The following is complicated by the need to reduce the number of network calls as much as possible."

## Escribile a alguien concreto

> Write to someone specific, even if they aren't much like you. Are you the only biologist on your team of computer scientists? Then you'd better explain any biology context in the code, even if it seems obvious to you.
>
> If you encounter a file with no header comment, consider adding a header telling prospective readers why they might find reading this file useful. (Thanks, Allan Mertner.)

## Ejemplo: al encontrar un defecto

> Immediately upon finding a defect is a good time to comment. For example, `// Be sure to change ../foo if you add another case.` It's not ideal to have that coupling in your code. Eventually, you'll have to learn how to eliminate it, but in the meantime, it's much better to add the comment that points out the coupling issue, rather than leaving it buried in the sand.

## Encadena con (cap. 17)

> Move the information in the comment into the code if possible, by introducing an explaining variable, explaining constant, or explaining helper.
