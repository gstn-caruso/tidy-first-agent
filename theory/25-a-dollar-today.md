# 25. A Dollar Today > A Dollar Tomorrow

*Tidy First?*, ch. 25, pp. 67–68.

## More isn't always more

> More is more and less is less, right? Depends. With money, it depends on:
>
> - When
> - How sure

## Why a dollar tomorrow is worth less

> If I give you a dollar today, you can spend it on something you want or you can invest it in a way that gives you more money later. If I promise you a dollar tomorrow, it's worth less than the dollar I give you today. Why?
>
> - You can't spend it, so it's worth less.
> - You can't invest it, so when you get it, it will be worth less than the dollar you got today.
> - There's some chance that I won't actually give it to you. Well, not me. I'm entirely trustworthy. But someone else, yeah, you have to be prepared that they won't give you the dollar, making that "dollar tomorrow" worth less.

## Every dollar needs a date

> How much less? This is a complicated question. For now, the important fact is that all dollars are not valued equally. If we want to, for example, add them up, then we need a date attached to each one.

## How to value a software system

> How do we value a software system? Say you have a software system and I want to buy it. How much should I reasonably pay you?
>
> What it *is* is irrelevant. It's a payment system. It consists of umpteen services. It has 1.4 million lines of code. Its average function cyclomatic complexity is 14 (just kidding, the average of power law–distributed values is useless). But none of this matters to me as a purchaser.

## Dated cash flows

> As a purchaser, I want to know how the money is going to flow. "Gazinttas and gazouttas," as my Pappy would have said. To value the software, I can model it as a set of cash flows, some in, some out, but (and this is the key point) each flow connected to a date.

## An exercise to sharpen your intuition

> Here's an exercise to help sharpen your intuition about time/money. Which is more attractive, a software system that over the next 10 years will cost $10 million and bring in $20 million, or one that will cost $10 million and bring in $12 million?
>
> It's a trick question. "Over the next 10 years" is financially equivalent to saying, "Until the heat death of the universe." The intuition to sharpen is, when you see those numbers, to immediately ask, "Yeah, but when and how sure?"

## Paying first or collecting first: it feels different

> Feel the difference between "I pay $10 million today and in 10 years I get $20 million" and "I get $12 million today and in 10 years I pay $10 million." That first deal makes me nervous. Yes, it seems like a good investment, but I'm going to be sweating out those 10 years. The second deal is a no-brainer. I'm guaranteed $2 million profit from day 1, plus whatever I get from investing over the 10 years. I'm excited about the 10 years instead of afraid of it.

## What this means for tidy first

> In the scope of this book, the time value of money encourages tidy after over tidy first. If we can implement a behavior change that makes us money now and tidy after, we make money sooner and spend money later. (As noted earlier, sometimes tidying first means the total cost of tidying first + behavior change is less than the cost of the behavior change without tidying. Always tidy first in such a case.)

## At the scale of a tidying

> At the scale we are talking about, minutes to hours, discounting cash flows probably doesn't make a huge economic difference. It does make a difference, though. Practicing with time value will help us in later books as we move to larger scales.

## What's next: optionality

> Next we'll look at the other source of software's economic value: optionality. Fun times, because time value and option value often conflict.

## For the tidier

- The time value of money pushes, by default, toward tidy after rather than tidy first: if a behavior change makes money now, ship it and tidy after, except for the explicit exception (from "What this means for tidy first").
- The exception that always wins: if cost(tidy) + cost(change after tidying) < cost(change without tidying), tidying first is unambiguously the right choice (from "What this means for tidy first").
- For any estimate of a tidying's benefit, ask "when does it pay off, and how sure are we?" — a distant or uncertain benefit is worth less than it looks (from "An exercise to sharpen your intuition" and "Paying first or collecting first: it feels different").
- At the scale of an individual tidying (minutes to hours) you don't need to discount cash flows precisely; intuition is enough — the discipline of thinking this way matters more for bigger decisions (from "At the scale of a tidying").
