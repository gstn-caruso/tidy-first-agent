# 22. Beneficially Relating Elements

*Tidy First?*, ch. 22, pp. 57–59.

## What is software design

> What is software design? I'm not a fan of starting with definitions, but we're hardly starting by now. You've seen examples of what I mean by design. You've seen how individual decisions chain together to achieve larger goals. You've seen the first glimpses of what I mean by "software design is an exercise in human relationships." Now I can say what I mean by "software design": *beneficially relating elements*.
>
> That's not many words for a big concept. Each word must be carrying substantial weight. Let's pick them apart and then put them back together.

## Elements

> Substantial structures have parts.
>
> Organelle → organ → organism.
>
> Atoms → molecules → crystals.
>
> In our world: tokens → expressions → statements → functions → objects/modules → systems.
>
> Elements have boundaries. You know where they start and end.
>
> Elements contain subelements. In our world we like to have homogeneous hierarchies (*à la* Composite pattern). Natural hierarchies, like previous examples, are not homogeneous. Contained subelements differ from the container. (I'm not sure this point is terribly important, but I like to keep it in mind—someday I'll write a truly philosophical book about software design as a natural process.)

## Relationships

> Okay, so we have a hierarchy of elements. Those elements exist in relation to each other. One function calls another. The functions are the elements. "Calls/called by" is the relationship. In the natural world, we have relationships like "eats," "shades," and "fertilizes."
>
> In software design, we have a handful of relationships like:
>
> - Invokes
> - Publishes
> - Listens
> - Refers (as in fetching the value of a variable)

## Beneficially

> Here's where the magic happens. One design is to have a single gigantic soup of tiny subelements. Think assembly language with a global namespace. This program would work. It would behave from the point of view of an external observer exactly the same as a well-designed program. Quickly, however, we would be unable to change it. There would be too many relationships, often implicit, between the elements.
>
> When we design, creating intermediate elements between the machine instructions and the whole, those intermediate elements begin benefitting each other. Function A can be simpler because function B takes care of the complexity of a part of the calculation.

## Beneficially relating elements

> One reading of the phrase "beneficially relating elements" starts with "the design is…." What is the design? It's the elements, their relationships, and the benefits derived from those relationships.
>
> Another reading starts with "designers are…." What do designers do? They beneficially relate elements. From this perspective, software designers can only:
>
> - Create and delete elements.
> - Create and delete relationships.
> - Increase the benefit of a relationship.
>
> There—easy, right? (← sarcasm warning)
>
> Take one of my favorite examples. I have an object that invokes another object twice in one function:
> ```
> caller()
>     return box.width() * box.height()
> ```
> The calling function has two relationships with the box, those of invoking two functions. Let's move the expression into the box:
> ```
> caller()
>     return box.area()
>
> Box>>area()
>     return width() * height()
> ```
> From a design standpoint, we have created a new element, `Box.area()`, and adjusted the relationship between the caller and the box. Now they are related by a single function invocation, with the benefit that the calling function is simpler and the cost that `Box` is one function bigger.
>
> When I talk about the structure of the system, I'm talking about:
>
> - The element hierarchy
> - The relationships between elements
> - The benefits created by those relationships
>
> Now we can make a firmer distinction between the structure and the behavior of the system.

## For the tidier

- A tidying is always one of these three moves and nothing else: create/delete an element, create/delete a relationship, or increase the benefit of an existing relationship (from "Beneficially relating elements"). If a proposed cleanup doesn't fit any of the three, it's probably not a tidying.
- Before applying a tidying, identify which concrete relationship improves (invokes, publishes, listens, refers) and what the benefit consists of — "it looks tidier" is not enough (from "Relationships" and "Beneficially").
- The `Box.area()` example shows the typical trade-off: extracting/moving code enlarges one element in exchange for simplifying the relationship with its caller. That cost/benefit has to be named, not assumed for free (from "Beneficially relating elements").
- A tidying touches structure (element hierarchy, relationships, benefits) without touching observable behavior — that's the line separating a tidying from a functional change (from "Beneficially relating elements", chapter closing).
