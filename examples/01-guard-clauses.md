# 1. Guard Clauses

*Tidy First?*, cap. 1, pp. 3–4.

## Disparador

> You see some code like this:
> ```
> if (condition)
>     ...some code...
> ```
> Or even better, this:
> ```
> if (condition)
>     if (not other condition)
>         ...some code...
> ```

## Movimiento

> As a reader, it's easy to get lost in nested conditions. Tidy the above to:
> ```
> if (not condition) return
> if (other condition) return
> ...some code...
> ```
> This is easier to read. It says, "Before we get into the details of the code, there are some preconditions we need to bear in mind."

## Sobre los múltiples returns

> (But what about MuLTipLe ReTuRns? The "rule" about having a single return for a routine came from the days of FORTRAN, where a single routine could have multiple entry *and* exit points. It was nearly impossible to debug such code. You couldn't tell what statements were executed. Code with guard clauses is easier to analyze because the preconditions are explicit.)

## Cuidado — el disparador tiene que cumplirse *exactamente*

> Don't overdo guard clauses. A routine with seven or eight guard clauses (I've seen it in the wild) is not easier to read. It needs more acute care to partition complexity.
>
> Only tidy to a guard clause if the prompt is met precisely:
> ```
> if (condition)
>     ...all the rest of the code in the routine...
> ```
> I see code I want to tidy but can't:
> ```
> if (condition)
>     ...some code...
> ...some other code...
> ```
> Maybe the first two lines can be extracted to a helper method and then a guard clause tidied, but always and only take tiny steps.

Ejemplo real citado por Beck: <https://github.com/Bogdanp/dramatiq/pull/470>.

## Encadena con (cap. 17)

> Once you've set up a guard clause, the condition may benefit from being turned into an explaining helper or extracted into an explaining variable.
