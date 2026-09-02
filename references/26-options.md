# 26. Options

*Tidy First?*, ch. 26, pp. 69–71.

## We create value when we change cash flows

> The previous chapter modeled the economic value of a software system as the sum of the discounted future cash flows. We create value when we change those flows:
>
> - Earning money more, sooner, and with greater likelihood
> - Spending money less, later, and with less likelihood

## Another source of value: optionality

> Working inside this model as a software designer already isn't easy. We live in a Goldilocks world: not too much design or too soon, not too little design or too late. But wait, there's more. (If it was easy, everybody would already be doing it and there'd be no excuse for this book.) There's another, sometimes conflicting, source of value: optionality.

## How I learned about options pricing

> Decades back I worked with trading software on Wall Street. I did the background reading, as I like to do, and discovered options pricing. Down the rabbit hole I went. I had recently invented test-driven development (TDD), and I was looking for practice topics. Options pricing seemed like a great example: complicated algorithm with known answers.
>
> I implemented the extant options pricing formulas test first (discovering the need for an epsilon when comparing floating-point numbers in the process). Along the way I developed an intuition for options that started to leak out into my general thinking about software design.

## The lessons of options

> I can't implement all those algorithms for you, but I can report the lessons I learned (I encourage you to try the exercise if you really want to "get it"):
>
> - "What behavior can I implement next?" has value all on its own, even before I implement it. This surprised me. I thought I was getting paid for what I had done (as per the previous chapter). I wasn't. I was mostly getting paid for what I could do next.
> - "What behavior can I implement next?" is more valuable the more behaviors are in the portfolio. If I can increase the size of the portfolio, I have created value.
> - "What behavior can I implement next?" is more valuable the more the behaviors in that portfolio are valuable. I can't predict which behavior will be most valuable, nor how valuable it will be, but…
> - I don't have to care which item will be most valuable, as long as I keep open the option of implementing it.
> - (This is the best one.) The *more* uncertain my predictions of value are, the *greater* the value of the option is (versus just implementing it). If I embrace change, I maximize the value I create in exactly those situations where (then) conventional software development fails most spectacularly.
>
> If you haven't encountered financial options before, here is my quick primer.

## The simple deal: a potato for a dollar

> Start out with a thing with a price. A potato for a dollar. I have a dollar. You have a potato. I give you the dollar. You give me the potato. Now I have a potato, but I don't have the dollar. You have the dollar, but you don't have the potato anymore.

## Paying today for a potato tomorrow

> Maybe I don't want the potato now; I want it tomorrow. I'm sure will I want it tomorrow. I can give you a dollar today in return for your promise of a potato tomorrow. Tomorrow you deliver the potato, and we're both happy. I'll give you a little less than a dollar today, because of the time value of money.

## When I'm not sure: the option is born

> What if I'm not sure if I want the potato tomorrow? I might have a picnic if the weather is good, in which case I'll make potato salad. If the weather is bad, though, I don't want to have bought a potato that will go to waste. In this case I can buy your promise of a potato tomorrow for a dollar tomorrow, but I might not hold you to that promise.

## How much that 'promise for a promise' is worth

> How much should I pay you for this "promise for a promise"? You're going to get the dollar tomorrow, but only if I hold you to your promise to sell your potato to me. You need to know what else you'll do with the potato if you can't sell it to me tomorrow. If you have other good uses for the potato tomorrow, then you can sell me this option for pennies. You don't much care if I buy it tomorrow or not. But if the potato is going to waste if I don't buy it tomorrow, then you have to charge me pretty much full price today.

## What a call option is

> I have just described a call option—the right, but not obligation, to purchase something in the future at a fixed price. Financial options have these parameters:
>
> - The *underlying* thing that we can buy
> - The *price* of the underlying, including the volatility of that price
> - The *premium* of the option, or the price we pay today
> - The *duration* of the option, or how long we have to decide whether to purchase the underlying (some options let you buy the underlying anytime between now and the end of the duration, which is what software looks like)

## What this means for software design

> What does this mean for software design? Software design is preparation for change; change of behavior. The behavior changes we *could* make next are the potatoes from the story. Design we do today is the premium we pay for the "option" of "buying" the behavior change tomorrow.

## Turning fear around

> Thinking of software design in terms of optionality turned my thinking upside-down. When I focused on balancing creating options and changing behavior, what used to scare me now excited me:
>
> - The more volatile the value of a potential behavior change, the better.
> - The longer I could develop, the better.
> - Yes, the cheaper I could develop in future, the better, but that was a small proportion of the value.
> - The less design work I could do to create an option, the better.

## The problem still left open

> But I was still faced with that tricky problem I breezed over by saying, "Balancing creating options and changing behavior."

## For the tidier

- A tidying is an option premium, not a purchase: you're not paying for the behavior change itself, but for keeping the right to make it later cheap. The less design it takes to open that option, the better (from "What this means for software design").
- The more uncertainty there is about what behavior you'll need later, the more valuable the option a tidying leaves open — you don't need to know what the next change will be to justify it (from "The lessons of options" and "Turning fear around").
- Not every cleanup is free: as with the potato, if "that structure" has other equally good uses even if you don't tidy now, the option is worth little; if the code will rot unless you touch it, it's worth almost full price — weigh the tidying as a promise for a promise, not a whim (from "How much that 'promise for a promise' is worth").
- Software resembles an American option (it can be exercised at any time up to expiration, not just at the end): that favors small, reversible tidyings over one big one all at once (from "What a call option is").
