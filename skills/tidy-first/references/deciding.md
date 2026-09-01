# Deciding when and how much to tidy — Part II, chs. 16–21

*Tidy First?*, Part II, pp. 33–54. Verbatim. Read when a first/after/later/never call isn't obvious, sizing a batch, or the tree is tangled.

## 16. Separate Tidying (pp. 35–37)

> And so we split our changes into separate PRs. Sequences of tidyings (or even just one tidying) go in one PR. Behavior changes go in a separate PR. Each time we switch between tidying and changing behavior, we open a new PR (Figure 16-4).

> Once you get comfortable with tidying, with working in small steps, with working with absolute safety, I encourage you to experiment with not requiring reviews for tidying PRs. This reduces latency further, incentivizing even smaller tidying PRs.

## 17. Chaining (pp. 39–41)

| Tidying | Full text (verbatim) |
|---|---|
| **Guard clause** | Once you've set up a guard clause, the condition may benefit from being turned into an explaining helper or extracted into an explaining variable. |
| **Dead code** | Once you've removed the clutter of dead code, you may be able to see how to sort the code into reading order or cohesion order. |
| **Normalize symmetries** | Once you've made identical code identical and different code different, you may be able to group precisely parallel code into reading order. I did this once with a file containing several web entry points. Once they all looked alike, it was natural to group them at the top of the file as a kind of table of contents to the rest of the code. |
| **New interface, old implementation** | Once you have your shiny new interface, you'll want to use it. If you don't have the automated rewrite tools to convert all callers, you'll need to convert them one at a time. This is the first time we've seen fanout—when one tidying leads to a bunch more, each of which can lead to a bunch more (way more about this when we talk about coupling and power laws). |
| **Reading order** | After you've established reading order, you may see the opportunity to normalize symmetries. Before, elements were far enough apart that you couldn't see the similarities. |
| **Cohesion order** | Elements grouped together for cohesion order are candidates to be extracted into a subelement. Creating, for example, a helper object is out of the scope of tidying. As you get comfortable and confident in tidying, though, it's natural to see larger-scale design changes that will ease further behavior changes. |
| **Explaining variables** | The righthand side of the assignment to an explaining variable is a candidate for an explaining helper (after which you may be able to inline the variable). The explanation offered by the variable name may make it possible to delete redundant comments. |
| **Explaining constants** | Extracting an explaining constant leads to cohesion order. Grouping constants that change in sync eases future changes. There are whole philosophies about where to put constants and how to arrange them. I won't get into all that here—pick something that makes your work easy. Well, easier. |
| **Explicit parameters** | After making parameters explicit, you may be able to group a set of parameters into an object and move code into that object. This is out of the scope of tidying, but be on the lookout for new abstractions revealed as you tidy. Some of the most powerful abstractions you will ever discover derive from running code. You would never have created them on speculation. |
| **Chunk statements** | You can precede each chunk with an explaining comment. You may extract a chunk as an explaining helper. |
| **Extract helper** | After extracting a helper you may introduce a guard clause, extract explaining constants and variables, or delete redundant comments. |
| **One pile** | After making a big, obvious mess, expect to tidy by chunking statements, adding explaining comments, and extracting helpers. |
| **Explaining comments** | Move the information in the comment into the code if possible, by introducing an explaining variable, explaining constant, or explaining helper. |
| **Delete redundant comments** | Eliminating the noise of redundant comments can help you see a better reading order or see the chance for explicit parameters. |

> You will begin to flow tidyings together to achieve larger changes to the structure of your code. Be wary of changing too much, too fast. A failed tidying is expensive relative to the cost of a series of successful tidyings. Practice tidyings like the notes of a scale. When the notes are clean and relaxed, you can form them into melodies.

## 18. Batch Sizes (pp. 43–46)

> **Collisions** — The more tidyings per batch, the longer the delay before integrating, and the greater the chance that a tidying collides with work someone else is doing. As soon as we encounter a merge conflict, the cost of merging our work rises by an order of magnitude. (Please remember that all these "numbers" are only directionally accurate, meant to help train your intuition.)
>
> **Interactions** — Likewise, the chance of a batch accidentally changing behavior rises with the number of tidyings in the batch. And likewise, merge costs rise dramatically when we have an interaction.
>
> **Speculation** — I know we said we were only going to tidy just enough to support the next behavior change, but yeah. The more tidyings per batch, the more we are prone to tidying just because, with all the additional costs that creates.

> In many organizations, the fixed cost of getting a single change through review and deployment is substantial. Programmers feel this cost, so they move right in the trade-off space, even as the costs of collisions, interactions, and speculation rise.

## 19. Rhythm (pp. 47–48)

> How much time is represented in one of those successions of structure changes followed by a behavior change?
>
> Well, software design is fractal, so it could be any time scale. For the purposes of this book, however, we are talking about one scale of software design: software design with personal impact. For that, we are talking about minutes, up to an hour. More than an hour of tidying at a time before making a behavior change likely means you've lost track of the minimum set of structure changes needed to enable your desired behavior change.

## 20. Getting Untangled (pp. 49–50)

> - Ship it as is. This is impolite to reviewers and prone to errors, but it's quick.
> - Untangle the tidyings and changes into separate PRs, or a sequence of PRs, or a sequence of commits in a single PR. This is more polite, but it can be a lot of work.
> - Discard your work in progress and start over, tidying first. This is more work, but it leaves a coherent chain of commits.

> By this point in the book it may not surprise you that I encourage you to experiment with the last option. Re-implementation raises the possibility that you will see something new as you re-implement, letting you squeeze more value out of the same set of behavior changes.

## 21. First, After, Later, Never (pp. 51–54)

> What would you do if you temporarily, provisionally believed that there was enough time to do your work? You might make a list of messes to tidy later (I call this my Fun List, because I have an odd notion of "fun"). Then later, rather than jumping feverishly to the next feature to implement, you might glance at your Fun List and think, "I have an hour. I don't want to start something big. Why don't I take a crack at item 4?" And then you might.

> So sure, tidy after, if:
> - You're going to change the same area again. Soon.
> - It's cheaper to tidy now.
> - The cost of tidying is roughly in proportion to the cost of behavior changes.

> - How much harder is the messy change? If tidying doesn't make it any easier, don't tidy first.
> - How immediate is the benefit of tidying? Let's say you're not ready to change the behavior yet. You're just reading code for comprehension. Tidying helps you comprehend faster. Sure, tidy first.
> - How will this tidying amortize? If you'll only ever change this code once, then consider limiting your tidying. If this tidying will pay off weekly for years, then go for it.
> - How sure are you of your tidying? Bias away from speculation. "I can see the messiness here, right here. If it's gone, then this change will be easy." But also, "Tidying this will make it easier to understand. I know because I'm confused right now."

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
