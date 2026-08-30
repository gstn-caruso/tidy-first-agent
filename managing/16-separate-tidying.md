# 16. Separate Tidying

*Tidy First?*, cap. 16, pp. 35–37.

## El loop feo

> 1. I put my tidyings in with my behavior changes.
> 2. Reviewers complain that my PRs are too long.
> 3. I separate the tidyings into their own PRs, either before (more likely) or after the behavior changes.
> 4. Reviewers complain that the tidying PRs are pointless.
> 5. Go to 1.
>
> The tidyings have to go somewhere, or you don't tidy. Where do they go? Summary: they go in their own PRs, with as few tidyings per PR as possible.

## Las fases por las que pasa uno

> In the first phase we're just making changes, and we begin with an undifferentiated mass of changes. […] Here, we're in the middle of fixing an if statement, realize a name is wrong, fix that, and go back to the if statement. Change is change.
>
> After learning the tidyings, it's as if our picture under the microscope snaps into focus. Some of those changes were changing the behavior of the program, its attributes as observed from the running of the program. Some of those changes, though, were changing the structure of the program. Those changes can only be observed by looking at the code: B=behavior, S=structure.
>
> After a bit of this, we start noticing the common flows. Chunking statements leads to explaining helpers leads to an easier time making behavior changes. Now programming is more like chess, and you can guess how the game will play out several moves (or sequences) ahead.
>
> And so we split our changes into separate PRs. Sequences of tidyings (or even just one tidying) go in one PR. Behavior changes go in a separate PR. Each time we switch between tidying and changing behavior, we open a new PR.

## Incentivos

> A big, all-inclusive PR shows a whole picture but may be too much for a reviewer to provide useful feedback on. Teensy-tiny PRs invite feedback in the small sense, but it comes at the risk of going off into the weeds.
>
> Review latency is also an incentive. If code gets reviewed rapidly, then you're encouraged to create more, smaller PRs. Those more-focused PRs encourage even more rapid reviews. Equally, this reinforcing loop can run backward, with slow reviews encouraging larger PRs, further slowing future reviews.
>
> Once you get comfortable with tidying, with working in small steps, with working with absolute safety, I encourage you to experiment with not requiring reviews for tidying PRs.
