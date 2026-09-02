# Java notes for the tidier

Read once per run when the target is `.java`. Adds to the catalog in the tidier's prompt; the book's prompt still has to be met exactly.

## Safety net

- Test command detection: `pom.xml` → `mvn -q test 2>&1 | tail -20`; `gradlew` → `./gradlew test -q 2>&1 | tail -20`; `build.gradle` without wrapper → `gradle test -q`. To scope to one class: `mvn -q -Dtest=<Class> test` / `./gradlew test --tests <FQCN> -q`. Compile errors are red. Judge by the exit status (`mvn -q test >/dev/null 2>&1; echo exit=$?`) or by `[ERROR]` / `FAILURE` / `Tests run: …, Failures: N` lines — Maven's own JDK warnings (`sun.misc.Unsafe…`) are noise, not red.
- What is not in git: `target/`, `build/`, `.idea/` — never commit them; if `git status` shows them, they are dirt (stop, as the contract says).

## Per tidying

| # | Tidying | In Java |
|---|---|---|
| 1 | Guard Clauses | Early `return`/`throw`. Don't create a guard when the wrapped block sits inside `try`/`finally` or `synchronized`, or when the tail after the `if` would change what's returned. Keep the same exception types. |
| 2 | Dead Code | What only LOOKS dead: reflection (`getDeclaredMethod`, `Class.forName`), Spring/DI (`@Component`, `@Bean`, `@EventListener`, `@Scheduled`), JPA/serialization callbacks, `main`, `equals`/`hashCode`/`toString`, a library module's public API, `@Deprecated` with external callers. Beck's own caveat: unsure → pre-tidy by logging its use. An unused import left behind by a deletion is part of the same commit. |
| 3 | Normalize Symmetries | Null handling (`== null` vs `Optional` vs `Objects.requireNonNull`) and lazy-init forms — pick one, convert one variant at a time. Enum↔enum mappers: a switch that maps 1:1 except for a hidden asymmetry — make the asymmetry visible (`case A, B ->` grouped + an Explaining Comment saying where the distinction really lives); don't replace the switch with `valueOf(name())` — that changes failure behavior and needs a bijection test, so it's a behavior change → Fun List. |
| 5 | Reading Order | Member order is free for methods and most fields; static initializer blocks and field initializers run in textual order, and enum constants' order is behavior (`ordinal()`, `values()`) — those stay put. Keep the file's existing convention (fields → constructors → public → private) if it has one. |
| 7 | Move Declaration and Initialization Together | `var`/`final` at first use; watch definite assignment across branches and variables used after a `try`. |
| 8 | Explaining Variables | `final var` (or an explicit type) named for intent. Extracting a subexpression of a `BigDecimal` chain must keep the same operation order and scale. Pulling the operands of a `&&`/`||` chain into variables evaluates them all eagerly and loses the short-circuit: if any operand can throw (a dereference the earlier operand used to guard) or has a side effect, that is a behavior change, and the existing tests will not catch it. Extract only operands that are total, or name the whole condition with Extract Helper instead. |
| 9 | Explaining Constants | `private static final` UPPER_SNAKE; keep the literal's exact form (`0.21` stays a `double` — switching to `BigDecimal` is a behavior change). Same literal, different meanings → different constants. |
| 10 | Explicit Parameters | Values pulled from `Map<String, …>`, `Properties`, `System.getenv`/`getProperty`, `@Value` → explicit parameters on a private body method; push them up the call chain later. |
| 11 | Chunk Statements | Blank lines only — don't run a formatter; formatter noise makes a mixed diff. |
| 12 | Extract Helper | Private method, same class; `static` when it touches no instance state. Extracting into a NEW class/interface is a refactoring, not a tidying → Fun List. |
| 13 | One Pile | Inline private methods called once; keep the survivor's visibility. |
| 14/15 | Comments | Javadoc that repeats the signature (`@param x the x`) is redundant; a `// TODO` that's done is redundant; keep `@throws`/`@param` only when they add information. |

## Not tidyings in Java (put them on the Fun List)

- Records with hand-written `withX` methods repeating every component, Lombok `@With`, builders — design changes, not tidyings.
- Extracting a class/service, introducing an interface, changing exception types, `double` → `BigDecimal`, adding or changing tests, changing visibility of public API, reordering enum constants.

## Commit hygiene

- One tidying per commit; `mvn -q test` (or the Gradle equivalent) green before and after; message `refactor(tidy): <Tidying> in <Class.method>` with `Tidy First? ch. N, p. M`.
