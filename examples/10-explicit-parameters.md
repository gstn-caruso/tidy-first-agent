# 10. Explicit Parameters

*Tidy First?*, cap. 10, p. 21.

## Disparador

> You're reading some code you want to change, and you notice that some of the data it works on wasn't passed explicitly to the routine. How do you make the inputs clear?

## Movimiento

> Split the routine. The top part gathers the parameters and passes them explicitly to the second part.
>
> It's common to see blocks of parameters passed in a map. This makes it hard to read and understand what data is required. It also opens up the horrific abuse of modifying the parameters for (implicit) use later.

## Antes

> ```
> params = { a: 1, b: 2 }
> foo(params)
>
> function foo(params)
>     ...params.a... ...params.b...
> ```

## Después

> Make the parameters explicit by splitting foo:
> ```
> function foo(params)
>     foo_body(params.a, params.b)
>
> function foo_body(a, b)
>    ...a... ...b...
> ```

## El otro caso: variables de entorno

> Another case for explicit parameters is when you find the use of environment variables deep in the bowels of the code. Make the parameters explicit, then be prepared to push them up the chain of calling functions. This will make your code easier to read, test, and analyze.

## Encadena con (cap. 17)

> After making parameters explicit, you may be able to group a set of parameters into an object and move code into that object. This is out of the scope of tidying, but be on the lookout for new abstractions revealed as you tidy. Some of the most powerful abstractions you will ever discover derive from running code. You would never have created them on speculation.
