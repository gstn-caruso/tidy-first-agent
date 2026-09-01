# 4. New Interface, Old Implementation

*Tidy First?*, ch. 4, p. 9.

## Prompt and move

> So you need to call a routine, and the interface makes it difficult/complicated/confusing/tedious. Implement the interface you wish you could call and call it. Implement the new interface by simply calling the old one (you can inline the implementation later, after migrating all other callers).

## Chains into (ch. 17) — the first *fanout*

> Once you have your shiny new interface, you'll want to use it. If you don't have the automated rewrite tools to convert all callers, you'll need to convert them one at a time. This is the first time we've seen fanout—when one tidying leads to a bunch more, each of which can lead to a bunch more (way more about this when we talk about coupling and power laws).
