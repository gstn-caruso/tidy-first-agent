# 32. Cohesion

*Tidy First?*, cap. 32, pp. 89–90.

## Dos implicancias de la cohesión

> Coupled elements should be subelements of the same containing element. That's the first implication of cohesion. Shovel all the manure into one pile. The second implication of cohesion is that elements that aren't manure (well, that aren't coupled) should go elsewhere.

## Ejemplo: un módulo con 10 funciones (Figura 32-1)

> For example, suppose we have a module containing 10 functions. Three of those functions are coupled. Where do the other seven go? We have two options (Figure 32-1).
>
> *(Figura 32-1: Incohesive element improved either by (top) extracting a cohesive subelement or by (bottom) moving uncoupled subelements elsewhere)*

## Opción 1: extraer el subelemento cohesivo

> The first is to bundle the coupled elements into their own subelement. We could create a submodule that only contained the three functions. That submodule would be cohesive because its elements were coupled. The original module might be less cohesive because now none of its elements would be coupled, but we won't be in worse shape than before.
>
> Extracting a helper function is this kind of "extract a cohesive subelement" approach. If the lines of the helper function have to be changed together, then the helper is cohesive, with all the benefits that come from cohesion: easier analysis, easier change, resistance to accidental behavior change.

## Opción 2: mover lo que no está acoplado

> The second option is to take the uncoupled elements and put them elsewhere. Where? This is where you get to be a designer. What are those functions coupled with? Move the functions closer to their siblings. Are they coupled with each other? Make another submodule for them to live in.

## Sin movimientos bruscos: el Scout rule

> Make no sudden moves. You're working with incomplete and changing information about what's coupled with what. Don't dramatically rearrange everything. Move one element at a time. Make the code tidier for the next person. If everyone follows the Scout rule ("leave it better than you found it"), the code will become more livable-with over time.

## Para el tidier

- De "Dos implicancias de la cohesión": para decidir si un tidying suma cohesión, chequeá dos cosas — ¿junta lo que está acoplado?, ¿saca lo que no lo está?
- De "Opción 1: extraer el subelemento cohesivo": extraer un helper solo suma cohesión si las líneas que quedan adentro tienen que cambiar juntas — si no cambian juntas, no es cohesivo, es solo mover código de lugar.
- De "Sin movimientos bruscos: el Scout rule": aplicá cohesión de a un elemento por vez — la información sobre qué está acoplado con qué es incompleta y cambia, así que reordenar todo de una es más riesgo que beneficio.
