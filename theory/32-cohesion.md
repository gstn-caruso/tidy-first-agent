# 32. Cohesion

*Tidy First?*, ch. 32, pp. 89–90.

## Two implications of cohesion

> Coupled elements should be subelements of the same containing element. That's the first implication of cohesion. Shovel all the manure into one pile. The second implication of cohesion is that elements that aren't manure (well, that aren't coupled) should go elsewhere.

## Example: a module with 10 functions (Figure 32-1)

> For example, suppose we have a module containing 10 functions. Three of those functions are coupled. Where do the other seven go? We have two options (Figure 32-1).
>
> *(Figura 32-1: Incohesive element improved either by (top) extracting a cohesive subelement or by (bottom) moving uncoupled subelements elsewhere)*

## Option 1: extract the cohesive subelement

> The first is to bundle the coupled elements into their own subelement. We could create a submodule that only contained the three functions. That submodule would be cohesive because its elements were coupled. The original module might be less cohesive because now none of its elements would be coupled, but we won't be in worse shape than before.
>
> Extracting a helper function is this kind of "extract a cohesive subelement" approach. If the lines of the helper function have to be changed together, then the helper is cohesive, with all the benefits that come from cohesion: easier analysis, easier change, resistance to accidental behavior change.

## Option 2: move what isn't coupled

> The second option is to take the uncoupled elements and put them elsewhere. Where? This is where you get to be a designer. What are those functions coupled with? Move the functions closer to their siblings. Are they coupled with each other? Make another submodule for them to live in.

## No sudden moves: the Scout rule

> Make no sudden moves. You're working with incomplete and changing information about what's coupled with what. Don't dramatically rearrange everything. Move one element at a time. Make the code tidier for the next person. If everyone follows the Scout rule ("leave it better than you found it"), the code will become more livable-with over time.

## For the tidier

- From "Two implications of cohesion": to decide whether a tidying adds cohesion, check two things — does it group what's coupled together, and does it move out what isn't coupled?
- From "Option 1: extract the cohesive subelement": extracting a helper only adds cohesion if the lines left inside have to change together — if they don't change together, it isn't cohesive, it's just moving code around.
- From "No sudden moves: the Scout rule": apply cohesion one element at a time — information about what's coupled with what is incomplete and changing, so reorganizing everything at once is more risk than benefit.
