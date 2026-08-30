# 23. Structure and Behavior

*Tidy First?*, cap. 23, pp. 61–63.

## Dos formas de crear valor

> Software creates value in two ways:
>
> - What it does today
> - The possibility of new things we can make it do tomorrow
>
> "What it does today" is the system's behavior—calculating payroll, sending dropship orders, notifying friends. (And yes, all software systems are sociotechnical systems, and we won't be designing the socio- part of it just yet.)

## Cómo se caracteriza el comportamiento

> Behavior can be characterized in two ways:
>
> **Input/output pairs**
>
> This many hours at this pay rate in this jurisdiction should result in a paycheck like this and a tax filing like that.
>
> **Invariants**
>
> The sum of all entitlements should equal the sum of all deductions.

## El comportamiento crea valor

> Behavior creates value. Rather than having to calculate a bunch of numbers by hand, the computer can calculate millions of them every second. Turns out people will pay not to have to calculate numbers by hand. If running the software costs $1 in electricity and you can charge folks $10 to run it on their behalf, then you have a business.
>
> In theory, this business could run forever, producing $10 for every dollar we put in. We know this is an oversimplification. Bit rot is real. Something is always changing. Staying in place in the river requires constant paddling. But for purposes of the distinction I'm drawing, this is good enough for the moment.

## La máquina que se puede convertir en otra cosa

> You know what's better than a machine that spits out $10 for every $1 you put in? A machine that spits out $100 for every $10 you put in. Or $20 for every $1. How are we going to get to that better machine?
>
> In a word, optionality. The mere presence of a system behaving a certain way changes the desire for how the system should behave (Heisenberg's uncertainty principle). However much you'd pay for the $10/$1 machine, you'd pay more for one that could turn into either a $100/$10 machine or a $20/$1 machine—*even if you didn't know which it would turn into*.

## El secreto de las opciones

> This is the secret it took me decades to absorb. I didn't have to change the behavior of my system to make it more valuable. As soon as I added to the options of what it *could* do next, I had already made money. (I went down the rabbit hole of options pricing formulas to really cement this understanding, but I trust you to figure out how to convince yourself.)

## La opción de expandir

> Options are the economic magic of software—especially the option to expand. If you can build 1,000 cars, there's no guarantee you can build 100,000 cars. But if you can send 1,000 notifications, you almost certainly can, with work, send 100,000 (when we get to the outer limits of technology, expansion becomes less certain, but in early growth, expansion isn't risky).

## Volatilidad y opciones

> One of the coolest thing about options is that the more volatile the environment is, the more valuable options become. This was part of my motivation to subtitle my book *Extreme Programming Explained* "Embrace Change." As a young engineer, I was terrified when a seemingly settled situation turned chaotic. As I learned to enhance optionality, I saw chaos as an opportunity.

## Qué le hace daño a las opciones

> What interferes with options? Here are some scenarios that reduce the options value embedded in your software:
>
> - A key employee quits. Changes that would have taken days now take months.
> - You distance yourself from your customers. If you get a provocative suggestion a month instead of one every day, you have fewer options.
> - The cost of changes skyrockets. Instead of being able to exercise an option a day, you can only exercise an option a month. Fewer options, less value.
>
> Nothing in the scope of this book directly addresses the first two of these options killers, but we can react to the third. We can keep the kitchen clean as we cook.

## Estructura, comportamiento y legibilidad

> The structure of the system doesn't matter to its behavior. One big function, a whole bunch of itty bitties, same paycheck comes out. The structure creates options. The structure could make it easy to add new countries to our paycheck calculation, or it could make it hard.
>
> Here's the problem: structure is not legible in the same way behavior is legible. There's a reason product roadmaps are lists of features (behavior changes). It's easy to see when the behavior changes—a button appears that wasn't there before.

## Por qué es difícil saber si invertimos bien en estructura

> Even though we know that we have to invest in structure to maintain and expand optionality, we can't really tell if we have. The code is easier to change? Really? We can't really tell if we've done enough. If we invested more in the structure, the code would be even easier to change? Really? We can't really tell if we've made the right investments in structure. The structure changes we made were the best way to make the code easier to change? Really?
>
> And so people get muddled about structure changes in ways they don't about behavior changes. This book is not here to answer those questions for you; it's here to help you answer those questions for yourself. Start by understanding that structure changes and behavior changes are both ways to create value, but that they are fundamentally different. How? In a word, reversibility.

## Para el tidier

- El valor del software no es solo lo que hace hoy: es también las opciones que deja abiertas para mañana. Un tidying que no cambia comportamiento igual puede estar creando valor si amplía qué es fácil hacer después (de "La máquina que se puede convertir en otra cosa" y "El secreto de las opciones").
- La estructura (cómo está armado el código) no afecta el comportamiento observable, pero sí determina qué tan caro es el próximo cambio — por eso "mantener la cocina limpia mientras cocinamos" es la justificación económica de tidy first/after (de "Qué le hace daño a las opciones").
- A diferencia del comportamiento, la mejora estructural no es legible a simple vista ("¿de verdad quedó más fácil de cambiar?"): no hay que esperar una prueba objetiva antes de tidyar, pero tampoco sobreinvertir asumiendo que "más limpieza" siempre es mejor (de "Por qué es difícil saber si invertimos bien en estructura").
- La distinción de fondo entre cambio estructural (tidying) y cambio de comportamiento es la reversibilidad — clave para decidir, en capítulos siguientes, cuándo conviene tidy first y cuándo no (cierre del capítulo).
