# 16. Separate Tidying

*Tidy First?*, ch. 16, pp. 35–37.

## The ugly loop

> 1. I put my tidyings in with my behavior changes.
> 2. Reviewers complain that my PRs are too long.
> 3. I separate the tidyings into their own PRs, either before (more likely) or after the behavior changes.
> 4. Reviewers complain that the tidying PRs are pointless.
> 5. Go to 1.
>
> The tidyings have to go somewhere, or you don't tidy. Where do they go? Summary: they go in their own PRs, with as few tidyings per PR as possible.

## The phases you go through

> Let's go through the trade-offs in more depth. Folks learning to tidy seem to go through predictable phases. In the first phase we're just making changes, and we begin with an undifferentiated mass of changes (Figure 16-1).

*(Figure 16-1: Undifferentiated mass of changes)*

> Here, we're in the middle of fixing an `if` statement, realize a name is wrong, fix that, and go back to the `if` statement. Change is change.
>
> After learning the tidyings, it's as if our picture under the microscope snaps into focus. Some of those changes were changing the behavior of the program, its attributes as observed from the running of the program. Some of those changes, though, were changing the structure of the program. Those changes can only be observed by looking at the code: B=behavior, S=structure (Figure 16-2).

*(Figure 16-2: Behavior changes and structure changes)*

> At this point there is still no plan, and no flow between changing behavior and structure—just an awareness that there are two different things playing together.
>
> After a bit of this, we start noticing the common flows. Chunking statements leads to explaining helpers leads to an easier time making behavior changes. Now programming is more like chess, and you can guess how the game will play out several moves (or sequences) ahead (Figure 16-3).

*(Figure 16-3: Behavior and structure changes in sequence)*

> Note that we still have one big PR at this point. We're at step 1 of the loop. Every move we made was intentional, aimed either at making easy changes or making those changes easy. Put it all together, though, and it's a bit of a mess. Reviewers will balk.
>
> And so we split our changes into separate PRs. Sequences of tidyings (or even just one tidying) go in one PR. Behavior changes go in a separate PR. Each time we switch between tidying and changing behavior, we open a new PR (Figure 16-4).

*(Figure 16-4: Behavior and structure changes in separate PRs)*

## Incentives

> How you lump or split your PRs is a trade-off. Think of it in terms of incentives. A big, all-inclusive PR shows a whole picture but may be too much for a reviewer to provide useful feedback on. Teensy-tiny PRs invite feedback in the small sense, but it comes at the risk of going off into the weeds.
>
> Review latency is also an incentive. If code gets reviewed rapidly, then you're encouraged to create more, smaller PRs. Those more-focused PRs encourage even more rapid reviews. Equally, this reinforcing loop can run backward, with slow reviews encouraging larger PRs, further slowing future reviews.
>
> Once you get comfortable with tidying, with working in small steps, with working with absolute safety, I encourage you to experiment with not requiring reviews for tidying PRs. This reduces latency further, incentivizing even smaller tidying PRs.
