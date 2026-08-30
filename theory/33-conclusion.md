# 33. Conclusion

*Tidy First?*, cap. 33, pp. 91–92.

## Las cuatro fuerzas: costo, revenue, coupling, cohesión

> And with that you are prepared to answer the question "tidy first?" Over and over. Each time slightly differently, but each time affected by the same forces:
>
> - Cost—Will tidying make costs smaller, later, or less likely?
> - Revenue—Will tidying make revenue larger, sooner, or more likely?
> - Coupling—Will tidying make it so I need to change fewer elements?
> - Cohesion—Will tidying make it so the elements I need to change are in a smaller, more concentrated scope?

## Lo más importante: vos

> Most important, though, is you. Will tidying bring peace, satisfaction, and joy to your programming? Maybe some. This is important because if you are your best self, you are a better programmer. You can't be your best self if you're always rushing, if you're always changing code that's painful to change.

## No te dejes llevar: tidyings son las Pringles

> Don't get carried away with tidying. Once you realize you can make your own life and work better by tidying, sometimes and somewhat, you can get giddy. Unlike the risk and uncertainty of features, where you can do what you think is right and folks can still be dissatisfied, you are the audience for your tidying, and you're very likely to be satisfied.
>
> Coupling conducts one tidying to the next to the next. Tidyings are the Pringles of software design. When you're tidying first, resist the urge to eat the next one. Tidy to enable the next behavior change. Save the tidying binge for later, when you can go nuts without delaying the change someone else is waiting for.

## Diseñando para otros como vos

> And be aware that as you practice tidying for yourself, you are preparing to design on behalf of others like you. That's where this is going—making software design an ordinary, balanced part of development.
>
> We seldom program alone. Just as there is coupling between elements in a design, we are coupled to each other. A change I make can ripple to you, and a change you make can ripple to me.

## El primer libro: individuos

> This first book has dealt with software design by and for individuals. Sure, your colleagues will benefit from tidier code, but the focus has been on you. Is it worth some investment to help you work with greater ease? Probably.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |

## El próximo libro: changers

> The next book in the series examines the relationships between changers, those who can directly change the system. We must get those relationships healthy before we are prepared for the ultimate relationship challenge, between changers and those who can do little but wait for our changes to land. Software design can nourish these relationships or damage them.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |
> | You and programmer colleagues | Days to weeks | Refactorings | Weekly planning | Power laws |

## El horizonte final: negocio y tecnología

> Of all people, I know not to plan too far ahead, but the ultimate payoff of this brilliant technique you are learning is to get along better with people who aren't like you. The relationships between business-oriented folks and technology-oriented folks are the most fraught, but also the most consequential and potentially the most rewarding. Once you make software design part of both daily business and strategic planning, you have the opportunity to play your part in healing the rift between business and technology.
>
> | Who? | When? | What? | How? | Why? |
> |---|---|---|---|---|
> | You | Minutes to hours | Tidyings | SB diffs | Coupling and cohesion |
> | You and programmer colleagues | Days to weeks | Refactorings | Weekly planning | Power laws |
> | All stakeholders | Months to years | Architectural evolution | Dynamic balance | ? |

## Cierre

> That's where we're going with this—to make software design truly an exercise in human relationships. So to start…
>
> Tidy first? Likely yes. Just enough. You're worth it.

## Para el tidier

- De "Las cuatro fuerzas": para responder "tidy first?" en un caso concreto, pasalo por las cuatro preguntas del libro —¿baja costos?, ¿sube revenue?, ¿baja coupling?, ¿concentra cohesión?— y decidí con eso, no a ojo.
- De "Lo más importante: vos": si un tidying no mueve ninguna de las cuatro fuerzas pero te da paz para seguir programando bien, igual cuenta — no lo descartes solo porque no se mide en costo o coupling.
- De "No te dejes llevar: tidyings son las Pringles": en un tidy-first, tidyá lo justo para habilitar el próximo cambio de comportamiento y parate ahí — la tentación de seguir ("uno más") se guarda para una sesión de tidy later, no para ahora.
- De "Diseñando para otros como vos": el próximo que toque este código hereda el coupling y la cohesión que dejaste, así que el criterio de "¿vale la pena tidyar?" incluye a esa persona, no solo a vos.
- De las tres tablas (El primer libro / El próximo libro / El horizonte final): la escala Who/When/What/How/Why (vos-minutos-tidyings → equipo-semanas-refactorings → todos-años-evolución arquitectónica) marca que no se aplica el mismo criterio de "tidy first" a un extract helper que a un cambio arquitectónico — cada escalón tiene su propio ritmo y quién decide.
- De "Cierre": la respuesta por defecto es "sí, tidy first" — pero "just enough": el objetivo no es maximizar el tidying, es maximizar el valor que ese tidying libera para el cambio que sigue.
