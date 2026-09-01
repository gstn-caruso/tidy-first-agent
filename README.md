# tidy-first

A Claude Code plugin for Kent Beck's *Tidy First? A Personal Exercise in Empirical Software Design* (O'Reilly, 2023). It ships:

- **`tidier`**, an agent that applies the book's 15 tidyings to a file, diff or function as separate structural commits — one tidying per commit, tests green before and after, chapter and page cited — after deciding first / after / later / never against the behavior change that comes next. Never changes behavior. Never mixes.
- **`tidy-first`**, an inline skill for the main session: what a tidying is, the catalog, the four questions of ch. 21, and how to hand the work to `tidier`.
- **References**: the parts of the book the agent actually reads, verbatim and trimmed to what a tidier needs — one file per tidying, the decision rules of Part II, the forces of Part III, and per-language notes (Java for now).
- **Evals**: a runner over `claude -p` that measures whether the agent does the right thing on a seeded Java fixture, and what it costs.

## Layout

```
.claude-plugin/plugin.json             the plugin manifest
agents/tidier.md                       the agent (≈ 7.5 KB, read on every run)
skills/tidy-first/SKILL.md             the inline guide (≈ 2.8 KB)
skills/tidy-first/references/
  catalog.md                           the 15 tidyings in one table, with pages
  tidyings/NN-<name>.md                chs. 1–15: prompt, move, before/after, caveats, chaining — read only for the tidyings applied
  deciding.md                          chs. 16–21: separate tidying, chaining table, batch sizes, rhythm, getting untangled, first/after/later/never
  forces.md                            chs. 22–33: the rule the tidier takes from each chapter and the quote it rests on
  languages/java.md                    test command and Java caveats per tidying
evals/                                 cases, fixture, hidden tests, runner, verifier, results summaries
assets/                                the book (pdf/epub) — gitignored, never pushed
```

Every line that starts with `>` under `references/` is the book, verbatim; `evals/scripts/check_verbatim.py` fails if one is altered. The only authored prose in the references is the rule bullets in `forces.md` and the catalog table.

## Install

For one session:

```sh
claude --plugin-dir ~/Code/tidy-first-agent
```

Permanently, as a skills-dir plugin (no marketplace needed):

```sh
ln -s ~/Code/tidy-first-agent ~/.claude/skills/tidy-first
```

Claude Code then loads it as `tidy-first@skills-dir`: the agent is `tidy-first:tidier` (or just `tidier` when unambiguous) and the skill is `/tidy-first:tidy-first`. After editing, `/reload-plugins`.

## Use

In a repo with tests:

> Use `tidier` on `src/main/java/orders/OrderPricer.java`. The behavior change that comes next: volume discounts in `priceFor()`. Tests: `mvn -q test`.

With nothing planned (comprehension mode, more conservative):

> Do a Tidy First pass with `tidier` on `OrderParser.java`.

After a change that just landed (*after* mode, ch. 21):

> I just merged the second date format into `parse()`. Tidy after with `tidier`.

To plan without touching code, ask the main session which tidyings apply; the `tidy-first` skill answers from the catalog and the chapter files.

## What it does not do

- Behavior changes, not even a "while I'm at it" bug fix.
- Refactorings: extracting a class or a service, new abstractions — out of scope for a tidying (ch. 17) and hard to undo (ch. 28). They go on the Fun List.
- Tidying past what serves the next behavior change ("just enough", ch. 33).
- Work on a live Cuis image — there the shared state is the image, not the working tree.

## Evals

See `evals/README.md`. Runs go through `claude -p` under the account's subscription; the cost figures in the summaries are the CLI's own estimates, used only to compare models and iterations.

## Source

Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023. ISBN 978-1-098-15124-9. The examples are in Beck's original pseudocode.
