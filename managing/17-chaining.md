# 17. Chaining

*Tidy First?*, cap. 17, pp. 39–41.

> Tidyings are like potato chips. You eat one, and you'll want another. Managing the urge to keep tidying is a key tidying skill. You just tidied; should you tidy more? It depends.
>
> How big you step will be up to you, but I encourage you to experiment with sticking to tiny tidying steps. Optimize each step. From the outside it will look like you are running, but, like the centipede, you will know you're taking many little steps.

## Tabla de encadenamientos (verbatim)

| Después de… | …puede seguir |
|---|---|
| **Guard clause** | the condition may benefit from being turned into an explaining helper or extracted into an explaining variable. |
| **Dead code** | you may be able to see how to sort the code into reading order or cohesion order. |
| **Normalize symmetries** | you may be able to group precisely parallel code into reading order. |
| **New interface, old implementation** | you'll want to use it. If you don't have the automated rewrite tools to convert all callers, you'll need to convert them one at a time. This is the first time we've seen fanout. |
| **Reading order** | you may see the opportunity to normalize symmetries. Before, elements were far enough apart that you couldn't see the similarities. |
| **Cohesion order** | elements grouped together […] are candidates to be extracted into a subelement. Creating, for example, a helper object is out of the scope of tidying. |
| **Explaining variables** | the righthand side of the assignment […] is a candidate for an explaining helper (after which you may be able to inline the variable). The explanation offered by the variable name may make it possible to delete redundant comments. |
| **Explaining constants** | leads to cohesion order. Grouping constants that change in sync eases future changes. |
| **Explicit parameters** | you may be able to group a set of parameters into an object and move code into that object. This is out of the scope of tidying. |
| **Chunk statements** | you can precede each chunk with an explaining comment. You may extract a chunk as an explaining helper. |
| **Extract helper** | you may introduce a guard clause, extract explaining constants and variables, or delete redundant comments. |
| **One pile** | expect to tidy by chunking statements, adding explaining comments, and extracting helpers. |
| **Explaining comments** | move the information in the comment into the code if possible, by introducing an explaining variable, explaining constant, or explaining helper. |
| **Delete redundant comments** | can help you see a better reading order or see the chance for explicit parameters. |

## Conclusión del capítulo

> You will begin to flow tidyings together to achieve larger changes to the structure of your code. Be wary of changing too much, too fast. A failed tidying is expensive relative to the cost of a series of successful tidyings. Practice tidyings like the notes of a scale. When the notes are clean and relaxed, you can form them into melodies.
