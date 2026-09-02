# 18. Batch Sizes

*Tidy First?*, ch. 18, pp. 43–46.

> How much tidying should you do before integrating and deploying?
>
> Well, there are a couple of considerations:
>
> - How much tidying do you need to do? That is, if we define "tidying" as structural changes supporting the next behavior change, then how many structural changes do you need to make to support the next behavior change? Tidying is not looking toward a far-ahead future. Tidying meets an immediate need. (We'll talk about this more when we talk about first/after/later, in Chapter 21.)
> - How much tidying will be easy to integrate and deploy?
>
> In Chapter 16, I discussed not mixing tidying and behavior changes. But we still have the open question of whether we batch all our tidyings together, do them all separately, or something in between (Figure 18-1).

*(Figure 18-1: Structure changes batched together or separately)*

> This puts us in a trade-off space, also known as a Goldilocks dilemma. What are the competing costs that let us evaluate what constitutes too few tidyings per batch, too many tidyings per batch, and the range of just the right number of tidyings per batch (Figure 18-2)?

*(Figure 18-2: Trade-off space for tidyings per batch)*

## Costs that rise as the batch grows

> Figure 18-3 shows the costs that rise as we put more tidyings in a batch.

*(Figure 18-3: Costs that rise as batches grow)*

> These include:
>
> **Collisions** — The more tidyings per batch, the longer the delay before integrating, and the greater the chance that a tidying collides with work someone else is doing. As soon as we encounter a merge conflict, the cost of merging our work rises by an order of magnitude. (Please remember that all these "numbers" are only directionally accurate, meant to help train your intuition.)
>
> **Interactions** — Likewise, the chance of a batch accidentally changing behavior rises with the number of tidyings in the batch. And likewise, merge costs rise dramatically when we have an interaction.
>
> **Speculation** — I know we said we were only going to tidy just enough to support the next behavior change, but yeah. The more tidyings per batch, the more we are prone to tidying just because, with all the additional costs that creates.

## The cost that rises as it shrinks, and what to do about it

> All of these factors reduce the number of tidyings we want in a batch before integrating and deploying (which are the same thing, right?). Yet, I see big batches of tidyings in the wild. What else is going on? Take a look at Figure 18-4.

*(Figure 18-4: Review costs rise as batches shrink)*

> In many organizations, the fixed cost of getting a single change through review and deployment is substantial. Programmers feel this cost, so they move right in the trade-off space, even as the costs of collisions, interactions, and speculation rise.
>
> What to do, what to do?
>
> Some folks act like these cost curves are inscribed on stone tablets, laws of the physics of the development universe we merely inhabit. Nope. If we want to reduce the cost of tidying, thus increasing tidying and reducing the cost of making behavior changes, then we can reduce the cost of review (Figure 18-5).

*(Figure 18-5: Reduce the cost of review to reduce the cost of tidying by shrinking batches)*

> You and your team are going to need to figure out how exactly to reduce the cost of review. In teams with trust and a strong culture, tidyings don't require review. The risk of interactions has been reduced so far that unreviewed tidying doesn't destabilize the software.
>
> Getting to the necessary level of safety and trust to eliminate tidying reviews is the work of months. Practice. Experiment. Review errors together.

## For the tidier

- From "Costs that rise as the batch grows": every extra tidying held before integrating raises the chance of a merge conflict and of the batch accidentally changing behavior, and both costs jump by an order of magnitude once they hit — so integrate the small batch rather than accumulating one more.
- From "Costs that rise as the batch grows": if the tidying you are about to add isn't needed by the next behavior change, that's speculation — end the batch there.
- From "The cost that rises as it shrinks, and what to do about it": when you feel pulled toward a big batch, check whether the reason is the fixed cost of getting a change reviewed and deployed rather than the code itself — that cost is not a law of physics, and the fix is to make tidying review cheap, not to grow the batch.
