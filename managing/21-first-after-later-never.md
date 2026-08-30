# 21. First, After, Later, Never

*Tidy First?*, cap. 21, pp. 51–54. **La respuesta del libro a su propio título.**

## Never

> The best reason is because we're never going to change the behavior of the code ever, ever again. […] For truly static systems, "If it ain't broke, don't fix it" reasonably applies.

## Later

> Some folks think tidying later is pure fantasy, a unicorn, an honest politician. […] I'm here to tell you that you really can tidy later. You may not like the prerequisite, though.
>
> Ask yourself, "How would we work if we had enough time?" If the answer is wildly different from what you are actually doing, then no, there is not enough time to do your work.
>
> You might make a list of messes to tidy later (I call this my Fun List, because I have an odd notion of "fun"). Then later, rather than jumping feverishly to the next feature to implement, you might glance at your Fun List and think, "I have an hour. I don't want to start something big. Why don't I take a crack at item 4?"

Razones para tidy later: reducir el impuesto del desorden (migrar los cien call sites que quedan para poder borrar la API vieja); aprender ("The code 'knows' how it wants to be structured"); y porque se siente bien ("Don't underestimate how much better you are as a programmer when you're happy").

## After

> You need to change behavior. The code is messy. You can't see how to tidy. You change the behavior anyway (good for you—mess is no excuse). But now, huzzah!, you see how the change you made could have been easier. Do you tidy after?
>
> Why not just tidy first the next time you need to change behavior in this area? It might be harder later. You may have forgotten context that makes tidying easier right now.
>
> Say the behavior change took you an hour. Spending an hour tidying after makes sense. Spending a week tidying after? That doesn't make sense. That goes on the Fun List.
>
> So sure, tidy after, if:
> - You're going to change the same area again. Soon.
> - It's cheaper to tidy now.
> - The cost of tidying is roughly in proportion to the cost of behavior changes.

## First

> Tidy first? And the answer is… It depends.
>
> - How much harder is the messy change? If tidying doesn't make it any easier, don't tidy first.
> - How immediate is the benefit of tidying? Let's say you're not ready to change the behavior yet. You're just reading code for comprehension. Tidying helps you comprehend faster. Sure, tidy first.
> - How will this tidying amortize? If you'll only ever change this code once, then consider limiting your tidying. If this tidying will pay off weekly for years, then go for it.
> - How sure are you of your tidying? Bias away from speculation. "I can see the messiness here, right here. If it's gone, then this change will be easy." But also, "Tidying this will make it easier to understand. I know because I'm confused right now."
>
> In general, bias toward tidying first, but be wary of tidying becoming an end in itself. The tidyings I've cataloged are tiny precisely so you don't have to think too hard about applying them. If you tidy and it doesn't pay off, no big deal.

## Resumen (verbatim, p. 54)

> **Tidy never when:**
> - You're never changing this code again.
> - There's nothing to learn by improving the design.
>
> **Tidy later when:**
> - You have a big batch of tidying to do without immediate payoff.
> - There's eventual payoff for completing the tidying.
> - You can tidy in little batches.
>
> **Tidy after when:**
> - Waiting until next time to tidy first will be more expensive.
> - You won't feel a sense of completion if you don't tidy after.
>
> **Tidy first when:**
> - It will pay off immediately, either in improved comprehension or in cheaper behavior changes.
> - You know what to tidy and how.
