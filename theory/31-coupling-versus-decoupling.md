# 31. Coupling Versus Decoupling

*Tidy First?*, cap. 31, pp. 85–87.

## ¿Por qué no desacoplar todo?

> Why don't you just decouple all the things? Why have any coupling at all?
>
> Coupling, like the Lego piece in the night, often isn't obvious until you step on it. You go to make a behavior change, then notice, "Oh, if I change this, I will have to change that, and that too." Or worse, you change this, put it in production, break things, and realize, "Oh, I guess I also have to change that and that." You're not aware what unconscious assumptions you're making.

## Razones legítimas para tener coupling

> Discounted cash flows account for some coupling. There's a quick, coupled way to implement some behavior, and a longer, more expensive, decoupled way. At the time, you made the economically correct decision to implement it with coupling—revenue sooner, expenses later. Now it's later.
>
> Another legitimate reason to have coupling in a system is because it wasn't a problem until just now. The boulder that was perched on the hill decided now was a good time to roll down. "Who knew that we would have to translate this into any other language?" And you didn't. Until you did.
>
> A final reason to have coupling is that some coupling is just inevitable. I'm afraid I don't have a better argument for this than "confident assertion." I'll work on it.

## La decisión de hoy: pagar coupling o pagar decoupling

> It doesn't really matter why the coupling is there. You're faced with a choice today: pay the cost of coupling or pay the cost of decoupling. "Tidy first?" is this decision in miniature (although only some messes are made of coupling).

## Ejemplo: protocolo de comunicación acoplado

> Let's take a look at a concrete example—a communication protocol. A simple way to implement it is to have a sending function and a receiving function:
> ```
> Sender>>send()
>     writeField1()
>     writeField2()
>
> Receiver>>receive()
>     readField1()
>     readField2()
> ```
> These functions are coupled. Change one, and you'd better change the other. Then you have to worry about deploying the changes in perfect synchronization.

## Desacoplando con un lenguaje de definición de interfaz

> By the hundredth time you modify these functions, you're probably getting tired of the extra care required. You define an interface definition language:
> ```
> format = [
>     {field: "1", type: "integer"},
>     {field: "2", type: "string"}
> ]
>
> Sender>>send()
>     writeFields(format)
>
> Receiver>>receive()
>     readFields(format)
> ```
> Poof! Coupling gone. Now you can change the format in one place. No need to change send() and receive() at the same time.

## El coupling que no se fue del todo

> But it turns out the coupling isn't "gone" gone. Yes, we can change the format in one place, say by adding a third field. However, somewhere deep inside the Sender, we still need to compute that third field. Until we've done that, we can't read and use the field in the Receiver. So Sender and Receiver are still coupled; if Receiver needs to change to use the new field, Sender needs to change too. We have given ourself more options for the order of implementation.

## Reducir coupling de un tipo aumenta el de otro

> Here's something I believe but can't prove or adequately explain: the more you reduce coupling for one class of changes, the greater the coupling becomes for other classes of changes. The practical implication of this (if it matches your intuition) is that you shouldn't bother to squeeze out every last bit of coupling. The coupling created in doing so isn't worth it.

## El espacio de trade-off (Figura 31-1)

> Overall, we are left with a trade-off space (Figure 31-1).
>
> *(Figura 31-1: Cost of coupling trades off with cost of decoupling)*
>
> This picture is naive in that the exact costs of coupling and decoupling aren't knowable in advance. These costs both play out over time, which introduces discounted cash flows. Decoupling also creates options, the value of which is uncertain and evolves over time.

## La decisión permanece

> The fundamental decision space remains. You can pay the cost of coupling or pay the cost (and reap the benefits) of decoupling. And you can fall anywhere along this continuum. No wonder software design is hard. And we won't even get to the interpersonal relationship part until the next book in this series.

## Para el tidier

- De "Razones legítimas para tener coupling": no asumas que todo coupling es un error a corregir — a veces fue la decisión económica correcta en su momento (ingreso antes, gasto después) y sigue siendo válida hoy.
- De "La decisión de hoy: pagar coupling o pagar decoupling": frente a un mess de acoplamiento, la pregunta no es "¿desacoplo sí o no?" sino "¿qué sale más barato hoy: vivir con el acoplamiento o pagar el costo de sacarlo?" — eso es el tidy first en miniatura.
- De "El coupling que no se fue del todo": cuando desacoples con una capa de indirección (formato, interfaz), revisá con respecto a qué cambio siguen acopladas las partes — capaz solo cambiaste el tipo de cambio que las acopla, no lo eliminaste.
- De "Reducir coupling de un tipo aumenta el de otro": no persigas cero coupling — bajar el acoplamiento para un tipo de cambio suele subirlo para otro; parate cuando el tidying deja de pagar más de lo que cuesta.
