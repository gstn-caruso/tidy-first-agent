# 21. First, After, Later, Never

*Tidy First?*, cap. 21, pp. 51–54. **La respuesta del libro a su propio título.**

> Let's talk about the timing of tidying with respect to a behavior change in the system. Tidy first, then change the behavior? Change the behavior, then tidy? Or simply note messiness (in the sense that future behavior changes are going to be harder than they need to be), then come back later to tidy? Or, don't tidy at all?

## Never

> Let's start with the last one. As always, we need to examine the trade-offs involved in not tidying at all. When should we say, "Yes, this is a giant mess, and we consciously choose not to do anything about it"? The best reason is because we're never going to change the behavior of the code ever, ever again.
>
> I stated the condition like that because it's rare that code truly never needs to have its behavior changed. However, it does happen. For truly static systems, "If it ain't broke, don't fix it" reasonably applies.

## Later

> Some folks think tidying later is pure fantasy, a unicorn, an honest politician. The mythological status of tidying later is used as justification for tidying too much now, whether that is before or after. I'm here to tell you that you really *can* tidy later. You may not like the prerequisite, though.
>
> Is there enough time to do your work? I'm not asking whether you have *plenty* of time, because of course not. I'm not asking whether there's more to do than you have time for, because of course there is. Ask yourself, "How would we work if we had enough time?" If the answer is wildly different from what you are actually doing, then no, there is not enough time to do your work.
>
> But I invite you to examine this assumption that there isn't enough time to do your work. I've worked with large, successful, long-lived, highly profitable businesses that still believed, in the face of all the evidence of being large, successful, long-lived, and highly profitable, that there just wasn't and wouldn't ever be enough time to do the work. Seems bizarre, like a bird questioning the laws of physics and suddenly falling out of the sky.
>
> What would you do if you temporarily, provisionally believed that there was enough time to do your work? You might make a list of messes to tidy later (I call this my Fun List, because I have an odd notion of "fun"). Then later, rather than jumping feverishly to the next feature to implement, you might glance at your Fun List and think, "I have an hour. I don't want to start something big. Why don't I take a crack at item 4?" And then you might.
>
> That's tidying later. It can happen. Try it. Then it *will* happen.
>
> Tidying makes future changes to the behavior of the system easier (through mechanisms we will explore in the next part of the book). If there is an area of the system that's guaranteed to change (strong word, "guaranteed"), then tidying in that general area creates value if it simplifies those future changes.
>
> Tidying later (that is, not tied to an immediate behavior change) creates value in a couple of other ways. One is by reducing the tax of messiness. You are migrating from an old API to a new API. You've changed the call sites that are immediately affected, but you have one hundred more call sites to migrate later. When you've migrated them all, you can remove the old API. However, until then, you have to mirror changes made to the new API in the old API.
>
> Tidying all those call sites isn't pointless mucking about. Once you migrate all of the changes, a certain class of changes becomes cheaper. There may not be a pressing need to reduce that cost, but taking the pebble out of your shoe lets you walk better.
>
> Another reason to tidy later is as a learning tool. The code "knows" how it wants to be structured. If you're listening and you move the code from its current structure toward its desired structure, you're bound to learn something. Tidying is a great way to become aware of the detailed consequences of your design. Tidying illuminates the design as it could be.
>
> Finally, tidying later just feels good. Software development is a human process. We are humans with human needs. Sometimes I just don't have the energy to tackle a new feature, but I want to work. Picking an item off the Fun List and tidying it brings me joy. Don't underestimate how much better you are as a programmer when you're happy.

## After

> You need to change behavior. The code is messy. You can't see how to tidy. You change the behavior anyway (good for you—mess is no excuse). But now, huzzah!, you see how the change you made could have been easier. Do you tidy after?
>
> It depends. Are you ever going to change the behavior in this same area again? (Likely yes, for reasons we'll get into in the next section, but still apply your judgment.) If you're going to change the area again, then a tidy after approach makes some sense.
>
> Why not just tidy first the next time you need to change behavior in this area? It might be harder later. You may have forgotten context that makes tidying easier right now. Other changes may have interfered with the tidying you'd like to do now. If waiting to tidy at a later date substantially increases the cost of tidying, consider doing it now.
>
> Also, how much tidying are we talking about? Say the behavior change took you an hour. Spending an hour tidying after makes sense. Spending a week tidying after? That doesn't make sense. That goes on the Fun List.
>
> So sure, tidy after, if:
> - You're going to change the same area again. Soon.
> - It's cheaper to tidy now.
> - The cost of tidying is roughly in proportion to the cost of behavior changes.

## First

> Now here, finally, at the end of the second part of the book, we come to an answer to the question posed by its title. Tidy first? And the answer is… It depends.
>
> I love my job sometimes. So okay, yeah, of course it depends, but what does it depend on? I need to change the behavior of this code. This code is messy. Do I tidy first? Ask yourself these questions:
>
> - How much harder is the messy change? If tidying doesn't make it any easier, don't tidy first.
> - How immediate is the benefit of tidying? Let's say you're not ready to change the behavior yet. You're just reading code for comprehension. Tidying helps you comprehend faster. Sure, tidy first.
> - How will this tidying amortize? If you'll only ever change this code once, then consider limiting your tidying. If this tidying will pay off weekly for years, then go for it.
> - How sure are you of your tidying? Bias away from speculation. "I can see the messiness here, right here. If it's gone, then this change will be easy." But also, "Tidying this will make it easier to understand. I know because I'm confused right now."
>
> In general, bias toward tidying first, but be wary of tidying becoming an end in itself. The tidyings I've cataloged are tiny precisely so you don't have to think too hard about applying them. If you tidy and it doesn't pay off, no big deal. Bias toward tidying shouldn't cost you much, and most of the time it will pay off.

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
