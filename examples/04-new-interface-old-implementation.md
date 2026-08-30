# 4. New Interface, Old Implementation

*Tidy First?*, ch. 4, p. 9.

## Prompt and move

> So you need to call a routine, and the interface makes it difficult/complicated/confusing/tedious. Implement the interface you wish you could call and call it. Implement the new interface by simply calling the old one (you can inline the implementation later, after migrating all other callers).

## Why this is the essence of design

> Creating a pass-through interface is the micro-scale essence of software design. You want to make some behavior change. If the design were like thus and so, making that change would be easy(-er). So make the design like that.
>
> The same impulse holds true when you are:
> - Coding backward—Start with the last line of a routine, as if you already had all the intermediate results you needed.
> - Coding test-first—Start with the test that needs to pass.
> - Designing helpers—If only I had a routine/object/service that did XXX, then the rest of this would be easy.

## Chains into (ch. 17) — the first *fanout*

> Once you have your shiny new interface, you'll want to use it. If you don't have the automated rewrite tools to convert all callers, you'll need to convert them one at a time. This is the first time we've seen fanout—when one tidying leads to a bunch more, each of which can lead to a bunch more (way more about this when we talk about coupling and power laws).
