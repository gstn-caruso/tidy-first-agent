# 27. Options Versus Cash Flows

*Tidy First?*, cap. 27, pp. 73–74.

## El tira y afloja económico de tidy first

> Here we have the economic tug-of-war that makes "tidy first?" such an interesting question:
>
> - Discounted cash flow tells us to make money sooner with greater likelihood and spend money later with less likelihood. Don't tidy first. That's spending money sooner and earning money later. Maybe don't even tidy after or later.
> - Options tell us to spend money now to make more money later (even if we don't currently know exactly how). Absolutely tidy first (when it creates options). Tidy after and later too.
>
> Tidy first? Yes. And also no.

## Cuándo tidyar primero es un sí rotundo

> Now, there are times to tidy first for sure. When:
> ```
> cost(tidying) + cost(behavior change after tidying) < cost(behavior change without tidying)
> ```
> then absolutely tidy first. It's still easy to get carried away and tidy too much, but set and maintain boundaries for how far you'll go and you'll be fine.

## Cuando la cuenta no cierra a corto plazo

> The more fraught situations occur when:
> ```
> cost(tidying) + cost(behavior change after tidying) > cost(behavior change without tidying)
> ```
> You might still want to tidy first, even though short-term economics discourage you. You may be implementing a series of behavior changes, all of which benefit from the tidying. Amortizing the cost of the tidying across all the changes might make sense, even discounting the cash flows.

## Cuando las opciones justifican tidyar igual

> Tidying first may make economic sense in spite of discounted cash flows if the value of the options created is greater than the value lost by spending money sooner and with certainty. We are firmly in the land of judgment here. Your sniffer might tell you, "There's more good stuff here, but I need to tidy to be able to see it." That may be good enough evidence for more tidying.

## Tidying como cuidado de uno mismo

> Or, since software design is an exercise in human relationships and we're talking about our relationship with ourself at the scale of tidying, you might tidy first just because it makes the subsequent behavior changes more pleasant. A little bit of this "tidying as self-care" is justified. Just recognize that you are going counter to your economic incentives.

## Dos formas de juicio que estamos practicando

> At the scale of tidying—minutes to hours—we can't (and shouldn't try to) precisely calculate the economics of our tidying. We are exercising two important forms of judgment, practicing for bigger things later:
>
> - Getting used to being aware of the incentives affecting the timing and scope of software design ("I want to spend more time designing and I'm getting pushback. What's going on?")
> - Practicing on ourselves the relationship skills that we will later be using with our direct colleagues, and then our more distant colleagues

## Lo que viene cuando suben las apuestas

> Once we raise the stakes, where the survival and thrival of a product is on the line, we'll be glad of a gut sense of when and how to design and when not to design.

## Para el tidier

- Regla dura: si costo(tidying) + costo(cambio después de tidyar) < costo(cambio sin tidyar), tidyar primero es correcto sin discusión — es la única condición del capítulo que no requiere juicio (de "Cuándo tidyar primero es un sí rotundo").
- Si esa cuenta no cierra a corto plazo, todavía puede convenir tidyar primero cuando la limpieza se amortiza contra varios cambios de comportamiento futuros que se benefician de ella, no solo el que tenés delante (de "Cuando la cuenta no cierra a corto plazo").
- También puede justificarse tidyar primero cuando "el sniffer" dice que hay más para ver pero el desorden lo tapa, o simplemente porque hace más agradable el cambio que sigue ("tidying as self-care") — hay que reconocer explícitamente que ahí se está yendo en contra del incentivo económico de corto plazo (de "Cuando las opciones justifican tidyar igual" y "Tidying como cuidado de uno mismo").
- A la escala de un tidying no hay que calcular la economía con precisión; alcanza con estar atento a qué incentivo está empujando la decisión (plata ahora vs. opción futura) y decidir con criterio, no con fórmula (de "Dos formas de juicio que estamos practicando").
