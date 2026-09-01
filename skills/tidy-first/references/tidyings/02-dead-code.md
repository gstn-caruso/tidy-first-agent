# 2. Dead Code

*Tidy First?*, ch. 2, p. 5.

## The move

> Delete it. That's all. If the code doesn't get executed, just delete it.

## Pre-tidying when you're not sure

> Sometimes it's easy to identify dead code. Sometimes, because of extensive use of reflection, it's not so easy. If you suspect code isn't used, pre-tidy it by logging its use. Put the pre-tidying into production and wait until you're confident.

## Step size

> As always, delete only a little code in each tidying diff. That way, if it turns out you were wrong it will be relatively easy to revert the change (see Chapter 28). "A little" is a cognitive measure, not a lines-of-code measure. It could be one clause in a conditional (e.g., you see the condition reduces to true), one routine, one file, one directory.

## Chains into (ch. 17)

> Once you've removed the clutter of dead code, you may be able to see how to sort the code into reading order or cohesion order.
