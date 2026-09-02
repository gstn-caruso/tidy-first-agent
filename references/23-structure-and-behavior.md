# 23. Structure and Behavior

*Tidy First?*, ch. 23, pp. 61–63.

## Two ways to create value

> Software creates value in two ways:
>
> - What it does today
> - The possibility of new things we can make it do tomorrow
>
> "What it does today" is the system's behavior—calculating payroll, sending dropship orders, notifying friends. (And yes, all software systems are sociotechnical systems, and we won't be designing the socio- part of it just yet.)

## How behavior is characterized

> Behavior can be characterized in two ways:
>
> **Input/output pairs**
>
> This many hours at this pay rate in this jurisdiction should result in a paycheck like this and a tax filing like that.
>
> **Invariants**
>
> The sum of all entitlements should equal the sum of all deductions.

## Behavior creates value

> Behavior creates value. Rather than having to calculate a bunch of numbers by hand, the computer can calculate millions of them every second. Turns out people will pay not to have to calculate numbers by hand. If running the software costs $1 in electricity and you can charge folks $10 to run it on their behalf, then you have a business.
>
> In theory, this business could run forever, producing $10 for every dollar we put in. We know this is an oversimplification. Bit rot is real. Something is always changing. Staying in place in the river requires constant paddling. But for purposes of the distinction I'm drawing, this is good enough for the moment.

## The machine that can turn into something else

> You know what's better than a machine that spits out $10 for every $1 you put in? A machine that spits out $100 for every $10 you put in. Or $20 for every $1. How are we going to get to that better machine?
>
> In a word, optionality. The mere presence of a system behaving a certain way changes the desire for how the system should behave (Heisenberg's uncertainty principle). However much you'd pay for the $10/$1 machine, you'd pay more for one that could turn into either a $100/$10 machine or a $20/$1 machine—*even if you didn't know which it would turn into*.

## The secret of options

> This is the secret it took me decades to absorb. I didn't have to change the behavior of my system to make it more valuable. As soon as I added to the options of what it *could* do next, I had already made money. (I went down the rabbit hole of options pricing formulas to really cement this understanding, but I trust you to figure out how to convince yourself.)

## The option to expand

> Options are the economic magic of software—especially the option to expand. If you can build 1,000 cars, there's no guarantee you can build 100,000 cars. But if you can send 1,000 notifications, you almost certainly can, with work, send 100,000 (when we get to the outer limits of technology, expansion becomes less certain, but in early growth, expansion isn't risky).

## Volatility and options

> One of the coolest thing about options is that the more volatile the environment is, the more valuable options become. This was part of my motivation to subtitle my book *Extreme Programming Explained* "Embrace Change." As a young engineer, I was terrified when a seemingly settled situation turned chaotic. As I learned to enhance optionality, I saw chaos as an opportunity.

## What hurts options

> What interferes with options? Here are some scenarios that reduce the options value embedded in your software:
>
> - A key employee quits. Changes that would have taken days now take months.
> - You distance yourself from your customers. If you get a provocative suggestion a month instead of one every day, you have fewer options.
> - The cost of changes skyrockets. Instead of being able to exercise an option a day, you can only exercise an option a month. Fewer options, less value.
>
> Nothing in the scope of this book directly addresses the first two of these options killers, but we can react to the third. We can keep the kitchen clean as we cook.

## Structure, behavior, and legibility

> The structure of the system doesn't matter to its behavior. One big function, a whole bunch of itty bitties, same paycheck comes out. The structure creates options. The structure could make it easy to add new countries to our paycheck calculation, or it could make it hard.
>
> Here's the problem: structure is not legible in the same way behavior is legible. There's a reason product roadmaps are lists of features (behavior changes). It's easy to see when the behavior changes—a button appears that wasn't there before.

## Why it's hard to know if we invested well in structure

> Even though we know that we have to invest in structure to maintain and expand optionality, we can't really tell if we have. The code is easier to change? Really? We can't really tell if we've done enough. If we invested more in the structure, the code would be even easier to change? Really? We can't really tell if we've made the right investments in structure. The structure changes we made were the best way to make the code easier to change? Really?
>
> And so people get muddled about structure changes in ways they don't about behavior changes. This book is not here to answer those questions for you; it's here to help you answer those questions for yourself. Start by understanding that structure changes and behavior changes are both ways to create value, but that they are fundamentally different. How? In a word, reversibility.

## For the tidier

- Software's value isn't only what it does today: it's also the options it leaves open for tomorrow. A tidying that doesn't change behavior can still be creating value if it expands what's easy to do next (from "The machine that can turn into something else" and "The secret of options").
- Structure (how the code is put together) doesn't affect observable behavior, but it does determine how expensive the next change is — that's why "keeping the kitchen clean as we cook" is the economic justification for tidy first/after (from "What hurts options").
- Unlike behavior, structural improvement isn't legible at a glance ("did it really get easier to change?"): don't wait for objective proof before tidying, but don't overinvest either by assuming "more cleanup" is always better (from "Why it's hard to know if we invested well in structure").
- The underlying distinction between structure change (tidying) and behavior change is reversibility — key to deciding, in later chapters, when tidy first pays off and when it doesn't (chapter closing).
