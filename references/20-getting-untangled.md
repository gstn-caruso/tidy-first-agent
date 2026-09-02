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

## For the tidier

- From "Three options, none of them pretty": once tidyings and behavior changes are already tangled, there are only three exits — ship it as is, untangle it into a sequence of commits or PRs, or discard the work in progress and redo it tidying first — and the one to pick is the one that best explains your intentions to the next person, not the one that reaches working code fastest.
- From "Three options, none of them pretty": don't let tests that already pass decide for you — that's sunk cost; the option worth experimenting with is discarding and re-implementing, because re-implementing often shows you something new and leaves a coherent chain of commits.
- From "The sooner you notice, the smaller it is": watch for the tangle while you work — the sooner you catch the shift from "cruising along making changes" to "what have I done here," the smaller the untangling job is and the less the choice between the three strategies matters.
