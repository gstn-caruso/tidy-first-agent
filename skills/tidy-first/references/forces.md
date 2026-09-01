# The forces behind every tidying decision — Part III, chs. 22–33

*Tidy First?*, Part III, pp. 55–92. Each chapter: the rule the tidier takes from it (ours, not Beck's), then the verbatim passage it rests on. Read when the mess is coupling, when tidy-first economics are unclear, or when you are tempted to keep tidying.

## 22. Beneficially Relating Elements (pp. 57–59)
- (ch. 22, pp. 57–59) A tidying is always one of three moves: create/delete an element, create/delete a relationship, or increase an existing relationship's benefit.
- (ch. 22, pp. 57–59) A tidying touches only the element hierarchy, its relationships, or their benefits — never observable behavior.
> - Create and delete elements.
> - Create and delete relationships.
> - Increase the benefit of a relationship.

## 23. Structure and Behavior (pp. 61–63)
- (ch. 23, pp. 61–63) Behavior creates value today; structure creates the options for tomorrow — a tidying that changes nothing today can still be worth doing.
- (ch. 23, pp. 61–63) Structure and behavior differ in one key way, reversibility — the axis later chapters use to decide tidy first vs. after.
> The structure of the system doesn't matter to its behavior. One big function, a whole bunch of itty bitties, same paycheck comes out. The structure creates options. The structure could make it easy to add new countries to our paycheck calculation, or it could make it hard.

## 24. Economics: Time Value and Optionality (pp. 65–66)
- (ch. 24, pp. 65–66) Two economic logics pull in tension: earn sooner/spend later (time value) vs. create options under uncertainty — they don't always agree.
- (ch. 24, pp. 65–66) When what feels tidy clashes with the economics, distrust your own judgment — money wins, eventually.
> - A dollar today is worth more than a dollar tomorrow, so earn sooner and spend later.
> - In a chaotic situation, options are better than things, so create options in the face of uncertainty.

## 25. A Dollar Today > A Dollar Tomorrow (pp. 67–68)
- (ch. 25, pp. 67–68) Time value favors tidy after by default — ship the change, tidy after — except when tidying first makes the total cheaper; then always tidy first.
- (ch. 25, pp. 67–68) For any tidying's payoff, ask when it lands and how sure you are — a distant or uncertain benefit is worth less than it looks.
> In the scope of this book, the time value of money encourages tidy after over tidy first. If we can implement a behavior change that makes us money now and tidy after, we make money sooner and spend money later. (As noted earlier, sometimes tidying first means the total cost of tidying first + behavior change is less than the cost of the behavior change without tidying. Always tidy first in such a case.)

## 26. Options (pp. 69–71)
- (ch. 26, pp. 69–71) A tidying is an option premium, not a purchase — you're paying for the right to change cheaply later, not for the change itself.
- (ch. 26, pp. 69–71) The more uncertain what you'll need later, the more valuable the option a tidying opens; you don't need to know the next change to justify it.
> - The more volatile the value of a potential behavior change, the better.

## 27. Options Versus Cash Flows (pp. 73–74)
- (ch. 27, pp. 73–74) Hard rule, no judgment needed: if cost(tidying) + cost(change after) < cost(change without), tidy first — full stop.
- (ch. 27, pp. 73–74) If that inequality doesn't hold, tidying first can still pay off when it amortizes across several future changes, or when the mess is hiding something you need to see.
> ```
> cost(tidying) + cost(behavior change after tidying) < cost(behavior change without tidying)
> ```
> then absolutely tidy first. It's still easy to get carried away and tidy too much, but set and maintain boundaries for how far you'll go and you'll be fine.

## 28. Reversible Structure Changes (pp. 75–76)
- (ch. 28, pp. 75–76) Ask first whether a change is reversible. Most tidyings are — don't overinvest in getting it right the first time; tidy and move on.
- (ch. 28, pp. 75–76) If the change isn't reversible (extracting a service, say), make it reversible first — feature flag, prototype in production — before committing fully.
> Because there is so little value to avoiding mistakes, we shouldn't invest much in doing so. That's the economic reality I was hinting at when choosing "tidying" to describe what we're doing in this book. It's no big deal. Just tidying.

## 29. Coupling (pp. 77–79)
- (ch. 29, pp. 77–79) Before calling something coupled, name the change it's coupled with respect to — coupling that only matters for a change that never happens isn't worth tidying.
- (ch. 29, pp. 77–79) Coupling can't be read off the code alone: check history too — files that keep showing up together in commits are coupled.
> ```
> coupled(E1, E2, Δ) ≡ ΔE1 ⇒ ΔE2
> ```

## 30. Constantine's Equivalence (pp. 81–83)
- (ch. 30, pp. 81–83) Since cost(software) ~= coupling, measure a tidying's value by how much coupling it removes, not by how many lines it touches.
- (ch. 30, pp. 81–83) Don't spread tidying evenly: look for where the next expensive, cascading change is likely hiding and tidy there first.
> And now we have the full Constantine's Equivalence:
> ```
> cost(software) ~= cost(change) ~= cost(big changes) ~= coupling
> ```

## 31. Coupling Versus Decoupling (pp. 85–87)
- (ch. 31, pp. 85–87) Don't assume coupling is a mistake — sometimes it was the right economic call then (revenue sooner, expense later) and still is today.
- (ch. 31, pp. 85–87) Don't chase zero coupling: lowering it for one kind of change tends to raise it for another — stop once the tidying stops paying for itself.
> It doesn't really matter why the coupling is there. You're faced with a choice today: pay the cost of coupling or pay the cost of decoupling. "Tidy first?" is this decision in miniature (although only some messes are made of coupling).

## 32. Cohesion (pp. 89–90)
- (ch. 32, pp. 89–90) To check whether a tidying adds cohesion, ask two things: does it group what's coupled together, and does it move out what isn't?
- (ch. 32, pp. 89–90) Apply cohesion one element at a time — what's coupled with what is incomplete, changing information; no sudden moves.
> Coupled elements should be subelements of the same containing element. That's the first implication of cohesion. Shovel all the manure into one pile. The second implication of cohesion is that elements that aren't manure (well, that aren't coupled) should go elsewhere.
> Make no sudden moves. You're working with incomplete and changing information about what's coupled with what. Don't dramatically rearrange everything. Move one element at a time. Make the code tidier for the next person. If everyone follows the Scout rule ("leave it better than you found it"), the code will become more livable-with over time.

## 33. Conclusion (pp. 91–92)
- (ch. 33, pp. 91–92) Run a candidate tidying through the four forces — cost, revenue, coupling, cohesion — before deciding; if none of them move, it may not be worth it.
- (ch. 33, pp. 91–92) Tidyings chain: resist eating "just one more" mid-feature — tidy enough to enable the next behavior change and stop; save the binge for tidy-later.
- (ch. 33, pp. 91–92) If nothing else applies, remember "most important: you" — a tidying that only buys peace of mind while programming still counts.
> - Cost—Will tidying make costs smaller, later, or less likely?
> - Revenue—Will tidying make revenue larger, sooner, or more likely?
> - Coupling—Will tidying make it so I need to change fewer elements?
> - Cohesion—Will tidying make it so the elements I need to change are in a smaller, more concentrated scope?
> Most important, though, is you. Will tidying bring peace, satisfaction, and joy to your programming? Maybe some. This is important because if you are your best self, you are a better programmer. You can't be your best self if you're always rushing, if you're always changing code that's painful to change.
> Coupling conducts one tidying to the next to the next. Tidyings are the Pringles of software design. When you're tidying first, resist the urge to eat the next one. Tidy to enable the next behavior change. Save the tidying binge for later, when you can go nuts without delaying the change someone else is waiting for.
> Tidy first? Likely yes. Just enough. You're worth it.
