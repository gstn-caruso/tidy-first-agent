# 33. Conclusion

*Tidy First?*, ch. 33, pp. 91–92.

## The four forces: cost, revenue, coupling, cohesion

> And with that you are prepared to answer the question "tidy first?" Over and over. Each time slightly differently, but each time affected by the same forces:
>
> - Cost—Will tidying make costs smaller, later, or less likely?
> - Revenue—Will tidying make revenue larger, sooner, or more likely?
> - Coupling—Will tidying make it so I need to change fewer elements?
> - Cohesion—Will tidying make it so the elements I need to change are in a smaller, more concentrated scope?

## Most important: you

> Most important, though, is you. Will tidying bring peace, satisfaction, and joy to your programming? Maybe some. This is important because if you are your best self, you are a better programmer. You can't be your best self if you're always rushing, if you're always changing code that's painful to change.

## Don't get carried away: tidyings are the Pringles

> Don't get carried away with tidying. Once you realize you can make your own life and work better by tidying, sometimes and somewhat, you can get giddy. Unlike the risk and uncertainty of features, where you can do what you think is right and folks can still be dissatisfied, you are the audience for your tidying, and you're very likely to be satisfied.
>
> Coupling conducts one tidying to the next to the next. Tidyings are the Pringles of software design. When you're tidying first, resist the urge to eat the next one. Tidy to enable the next behavior change. Save the tidying binge for later, when you can go nuts without delaying the change someone else is waiting for.

## Designing for others like you

> And be aware that as you practice tidying for yourself, you are preparing to design on behalf of others like you. That's where this is going—making software design an ordinary, balanced part of development.
>
> We seldom program alone. Just as there is coupling between elements in a design, we are coupled to each other. A change I make can ripple to you, and a change you make can ripple to me.

## The first book: individuals

> This first book has dealt with software design by and for individuals. Sure, your colleagues will benefit from tidier code, but the focus has been on you. Is it worth some investment to help you work with greater ease? Probably.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |

## The next book: changers

> The next book in the series examines the relationships between changers, those who can directly change the system. We must get those relationships healthy before we are prepared for the ultimate relationship challenge, between changers and those who can do little but wait for our changes to land. Software design can nourish these relationships or damage them.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |
> | You and programmer colleagues | Days to weeks | Refactorings | Weekly planning | Power laws |

## The final horizon: business and technology

> Of all people, I know not to plan too far ahead, but the ultimate payoff of this brilliant technique you are learning is to get along better with people who aren't like you. The relationships between business-oriented folks and technology-oriented folks are the most fraught, but also the most consequential and potentially the most rewarding. Once you make software design part of both daily business and strategic planning, you have the opportunity to play your part in healing the rift between business and technology.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |
> | You and programmer colleagues | Days to weeks | Refactorings | Weekly planning | Power laws |
> | All stakeholders | Months to years | Architectural evolution | Dynamic balance | ? |

## Closing

> That's where we're going with this—to make software design truly an exercise in human relationships. So to start…
>
> Tidy first? Likely yes. Just enough. You're worth it.

## For the tidier

- From "The four forces": to answer "tidy first?" in a concrete case, run it through the book's four questions — does it lower costs, raise revenue, lower coupling, concentrate cohesion? — and decide from that, not by eye.
- From "Most important: you": if a tidying doesn't move any of the four forces but gives you the peace of mind to keep programming well, it still counts — don't discard it just because it isn't measured in cost or coupling.
- From "Don't get carried away: tidyings are the Pringles": in a tidy-first, tidy just enough to enable the next behavior change and stop there — save the temptation to keep going ("one more") for a tidy-later session, not for now.
- From "Designing for others like you": whoever touches this code next inherits the coupling and cohesion you left behind, so the criterion of "is it worth tidying?" includes that person, not just you.
- From the three tables (The first book / The next book / The final horizon): the Who/When/What/How/Why scale (you-minutes-tidyings → team-weeks-refactorings → everyone-years-architectural evolution) shows the same "tidy first" criterion doesn't apply to an extract-helper the way it applies to an architectural change — each level has its own pace and its own decision-maker.
- From "Closing": the default answer is "yes, tidy first" — but "just enough": the goal isn't to maximize tidying, it's to maximize the value that tidying unlocks for the change that follows.
