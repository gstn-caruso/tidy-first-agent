# 19. Rhythm

*Tidy First?*, cap. 19, pp. 47–48.

> Let's go back to the beginning. You are tidying to make future changes to the behavior of the system easier. You are making future behavior changes easier because you're worth it (we'll get into the economics later, if anyone objects). What are we talking about here? A brief moment, then back to the slog? Hour upon hour of blissful tidying?
>
> Part of the art of managing tidying is managing the rhythm of it. In the previous chapter, we saw this image (Figure 19-1), encouraging smaller batches of tidying.

*(Figura 19-1: Structure changes batched together or separately)*

> How much time is represented in one of those successions of structure changes followed by a behavior change?
>
> Well, software design is fractal, so it could be any time scale. For the purposes of this book, however, we are talking about one scale of software design: software design with personal impact. For that, we are talking about minutes, up to an hour. More than an hour of tidying at a time before making a behavior change likely means you've lost track of the minimum set of structure changes needed to enable your desired behavior change.
>
> Another possibility, though, is that the code is in such a mess that you can profitably tidy for hours before making a behavior change. If this is true, it won't be true for long. Software design has a strong "pave the path" tendency.

## "Pave the path"

> If you haven't heard the story, here's how it goes: a college built a bunch of buildings, and the planners were trying to figure out where to put walking paths between them. Rather than make carefully educated guesses, however, they just planted all the area between the buildings with grass.
>
> A few months later, students' feet had worn paths in the grass. The planners paved those areas that had been worn smooth.
>
> Behavior changes tend to cluster in the code. From Pareto, 80% of the changes will occur in 20% of the files. One of the beauties of tidying first is that the tidyings cluster too. And they cluster in exactly those spots most attractive for behavior changes.
>
> Even if at first you tidy a *lot*, soon you will find yourself wanting to make a behavior change in code that's already tidy. Continue for a bit, and most changes will happen in already-tidied areas of the code. Eventually, encountering untidy code will be the exception, even though most of the code in the system hasn't been touched.
>
> That's why I'm confident in saying that tidying is a minutes-to-an-hour kind of activity. Yes, sometimes it goes on longer, but not for long.
