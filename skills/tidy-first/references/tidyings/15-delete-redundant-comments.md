# 15. Delete Redundant Comments

*Tidy First?*, ch. 15, pp. 31–32.

## Prompt and move

> When you see a comment that says exactly what the code says, remove it.
>
> The purpose of code is to explain to other programmers what you want the computer to do. Comments and code present different trade-offs for you as a writer and for future readers. You can explain anything you want in prose. On the other hand, there's no mechanism to double-check the accuracy of prose as the system changes, and comments might become redundant as the code evolves.

## Example 2: an earlier tidying made it redundant

> Tidyings often chain together. A previous tidying may have made a comment redundant. For example, the original code might look like this:
> ```
> if (generator)
>     ...a bunch of lines of code to set up the generator...
> else
>     # no generator, return the default
>     return getDefaultGenerator()
> ```
> After tidying with a guard clause, the code looks like this:
> ```
> if (! generator)
>     # no generator, return the default
>     return getDefaultGenerator()
>
> ...a bunch of lines of code to set up the generator...
> ```
> The comment isn't redundant at first. It returns our attention to the current context (no generator present) after reading a bunch of lines of code in a different context (generator present, needs setup). After tidying, however, the comment is a simple restatement of what the code says. So, let's delete it. *Hasta la vista*, *auf wiedersehen*, buh-bye.

## Caveat — only what's *absolutely* redundant (general close of ch. 17)

> I'm going to emphasize once again, since I get accused of being anti-comment, that you should only delete absolutely, completely redundant comments. You should also tidy with an eye toward making comments absolutely, completely redundant.

## Chains into (ch. 17)

> Eliminating the noise of redundant comments can help you see a better reading order or see the chance for explicit parameters.
