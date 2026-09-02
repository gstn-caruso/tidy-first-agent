# 20. Getting Untangled

*Tidy First?*, ch. 20, pp. 49–50.

> You're changing the behavior of some code. You see a tidying that would make it easier to change. You tidy. Then you write another test case. Now you need to change the behavior some more. That leads to more tidying. An hour later you:
>
> - Actually understand all the behavior changes that need to be made
> - Actually understand all the tidying that eases those behavior changes
> - Have a mess of tidyings and changes all tangled together

## Three options, none of them pretty

> You have at least three options, none of them attractive:
>
> - Ship it as is. This is impolite to reviewers and prone to errors, but it's quick.
> - Untangle the tidyings and changes into separate PRs, or a sequence of PRs, or a sequence of commits in a single PR. This is more polite, but it can be a lot of work.
> - Discard your work in progress and start over, tidying first. This is more work, but it leaves a coherent chain of commits.
>
> The sunk cost fallacy complicates the choice between these options. You have some new tests. They pass. Why would you want to throw that away?
>
> The answer, as always, is because you are not just instructing a computer, you are explaining your intentions for the computer to other people. The shortest path to instructing the computer is not an interesting end goal.
>
> By this point in the book it may not surprise you that I encourage you to experiment with the last option. Re-implementation raises the possibility that you will see something new as you re-implement, letting you squeeze more value out of the same set of behavior changes.

## The sooner you notice, the smaller it is

> Untangling a ball of yarn starts with noticing that you have a tangle. The sooner you realize the need to untangle, the smaller the job is (and the less important the decision between the strategies becomes). When you first begin consciously tidying, whether first or after, you'll likely miss the transition between "cruising along making changes" and "oh no, what all have I done?" Don't worry. You'll get better at sequencing tidyings and changes over time.
>
> Speaking of "first or after," it's time to talk about timing.
