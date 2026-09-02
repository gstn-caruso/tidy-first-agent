# 17. Chaining

*Tidy First?*, ch. 17, pp. 39–41.

## Why chain tidyings

> Tidyings are like potato chips. You eat one, and you'll want another. Managing the urge to keep tidying is a key tidying skill. You just tidied; should you tidy more? It depends (we'll get to what it depends on in Part III).
>
> How big you step will be up to you, but I encourage you to experiment with sticking to tiny tidying steps. Optimize each step. From the outside it will look like you are running, but, like the centipede, you will know you're taking many little steps.
>
> Tidying becomes a game of chess, with moves visible ahead. Let's look at how tidyings set up further tidyings:

## Chaining table (verbatim)

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

## On comments, to be clear

> I'm going to emphasize once again, since I get accused of being anti-comment, that you should only delete absolutely, completely redundant comments. You should also tidy with an eye toward making comments absolutely, completely redundant. Your job as a software designer is to set yourself and your team up for success, now and in the future.
>
> Since change is the dominant cost of software development and understanding code is the dominant cost of change, communicating the structure and intent of working code is one of the most valuable skills you can exercise. Comments are *a* form of communication, but tidying lets you explore the limits of communicating through the other elements of programming.

## Chapter conclusion

> You will begin to flow tidyings together to achieve larger changes to the structure of your code. Be wary of changing too much, too fast. A failed tidying is expensive relative to the cost of a series of successful tidyings. Practice tidyings like the notes of a scale. When the notes are clean and relaxed, you can form them into melodies.

## For the tidier

- From "Why chain tidyings": after finishing a tidying, treat "should I tidy more?" as a decision, not an urge — and if you do continue, make the next step tiny rather than bigger.
- From "Chaining table (verbatim)": to choose the next tidying, look up the one you just applied in the table and take the follow-on it sets up, instead of rescanning the code from scratch.
- From "Chaining table (verbatim)": when the chain points at creating a helper object or grouping parameters into an object, stop — the table marks those as out of the scope of tidying; note the abstraction the code revealed and leave it for a design change.
- From "On comments, to be clear": delete a comment only when it is absolutely, completely redundant, and get it there by moving its information into the code (explaining variable, explaining constant, explaining helper) first.
- From "Chapter conclusion": stop chaining before you are changing too much too fast — one failed tidying costs more than a series of small successful ones saves.
