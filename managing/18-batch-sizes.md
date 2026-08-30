# 18. Batch Sizes

*Tidy First?*, cap. 18, pp. 43–46.

> How much tidying should you do before integrating and deploying?
>
> - How much tidying do you need to do? That is, if we define "tidying" as structural changes supporting the next behavior change, then how many structural changes do you need to make to support the next behavior change? Tidying is not looking toward a far-ahead future. Tidying meets an immediate need.
> - How much tidying will be easy to integrate and deploy?

## Costos que suben al agrandar el batch

> **Collisions** — The more tidyings per batch, the longer the delay before integrating, and the greater the chance that a tidying collides with work someone else is doing. As soon as we encounter a merge conflict, the cost of merging our work rises by an order of magnitude.
>
> **Interactions** — Likewise, the chance of a batch accidentally changing behavior rises with the number of tidyings in the batch.
>
> **Speculation** — I know we said we were only going to tidy just enough to support the next behavior change, but yeah. The more tidyings per batch, the more we are prone to tidying just because, with all the additional costs that creates.

## El costo que sube al achicarlo, y qué hacer con él

> In many organizations, the fixed cost of getting a single change through review and deployment is substantial. Programmers feel this cost, so they move right in the trade-off space, even as the costs of collisions, interactions, and speculation rise.
>
> Some folks act like these cost curves are inscribed on stone tablets […]. Nope. If we want to reduce the cost of tidying, thus increasing tidying and reducing the cost of making behavior changes, then we can reduce the cost of review.
>
> In teams with trust and a strong culture, tidyings don't require review. The risk of interactions has been reduced so far that unreviewed tidying doesn't destabilize the software.
