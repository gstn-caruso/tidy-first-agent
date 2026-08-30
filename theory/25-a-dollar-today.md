# 25. A Dollar Today > A Dollar Tomorrow

*Tidy First?*, cap. 25, pp. 67–68.

## Más no siempre es más

> More is more and less is less, right? Depends. With money, it depends on:
>
> - When
> - How sure

## Por qué un dólar mañana vale menos

> If I give you a dollar today, you can spend it on something you want or you can invest it in a way that gives you more money later. If I promise you a dollar tomorrow, it's worth less than the dollar I give you today. Why?
>
> - You can't spend it, so it's worth less.
> - You can't invest it, so when you get it, it will be worth less than the dollar you got today.
> - There's some chance that I won't actually give it to you. Well, not me. I'm entirely trustworthy. But someone else, yeah, you have to be prepared that they won't give you the dollar, making that "dollar tomorrow" worth less.

## Hace falta una fecha para cada dólar

> How much less? This is a complicated question. For now, the important fact is that all dollars are not valued equally. If we want to, for example, add them up, then we need a date attached to each one.

## Cómo valuar un sistema de software

> How do we value a software system? Say you have a software system and I want to buy it. How much should I reasonably pay you?
>
> What it *is* is irrelevant. It's a payment system. It consists of umpteen services. It has 1.4 million lines of code. Its average function cyclomatic complexity is 14 (just kidding, the average of power law–distributed values is useless). But none of this matters to me as a purchaser.

## Flujos de caja con fecha

> As a purchaser, I want to know how the money is going to flow. "Gazinttas and gazouttas," as my Pappy would have said. To value the software, I can model it as a set of cash flows, some in, some out, but (and this is the key point) each flow connected to a date.

## Un ejercicio para afinar la intuición

> Here's an exercise to help sharpen your intuition about time/money. Which is more attractive, a software system that over the next 10 years will cost $10 million and bring in $20 million, or one that will cost $10 million and bring in $12 million?
>
> It's a trick question. "Over the next 10 years" is financially equivalent to saying, "Until the heat death of the universe." The intuition to sharpen is, when you see those numbers, to immediately ask, "Yeah, but when and how sure?"

## Pagar antes o cobrar antes: se siente distinto

> Feel the difference between "I pay $10 million today and in 10 years I get $20 million" and "I get $12 million today and in 10 years I pay $10 million." That first deal makes me nervous. Yes, it seems like a good investment, but I'm going to be sweating out those 10 years. The second deal is a no-brainer. I'm guaranteed $2 million profit from day 1, plus whatever I get from investing over the 10 years. I'm excited about the 10 years instead of afraid of it.

## Qué implica esto para tidy first

> In the scope of this book, the time value of money encourages tidy after over tidy first. If we can implement a behavior change that makes us money now and tidy after, we make money sooner and spend money later. (As noted earlier, sometimes tidying first means the total cost of tidying first + behavior change is less than the cost of the behavior change without tidying. Always tidy first in such a case.)

## A la escala de un tidying

> At the scale we are talking about, minutes to hours, discounting cash flows probably doesn't make a huge economic difference. It does make a difference, though. Practicing with time value will help us in later books as we move to larger scales.

## Lo que sigue: optionality

> Next we'll look at the other source of software's economic value: optionality. Fun times, because time value and option value often conflict.

## Para el tidier

- El valor tiempo del dinero empuja, por defecto, a tidy after y no a tidy first: si un cambio de comportamiento genera plata ya, conviene entregarlo y tidyar después, salvo la excepción explícita (de "Qué implica esto para tidy first").
- La excepción que siempre gana: si costo(tidy) + costo(cambio después de tidyar) < costo(cambio sin tidyar), tidyar primero es la opción correcta sin ambigüedad (de "Qué implica esto para tidy first").
- Ante cualquier estimación de beneficio de un tidying, preguntá "¿cuándo se cobra y con cuánta certeza?" — un beneficio lejano o incierto vale menos de lo que aparenta (de "Un ejercicio para afinar la intuición" y "Pagar antes o cobrar antes: se siente distinto").
- A la escala de un tidying individual (minutos a horas) no hace falta descontar flujos de caja con precisión; la intuición alcanza — la disciplina de pensar así importa más para decisiones grandes (de "A la escala de un tidying").
