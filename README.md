# tidy-first-agent

A Claude Code agent that acts as a **tidier** per *Tidy First? A Personal Exercise in Empirical Software Design* (Kent Beck, O'Reilly 2023), with the book's examples extracted **verbatim** as reference material.

Given a file/diff/function — ideally along with the behavior change that comes next — the agent:

1. builds the safety net (tests green, working tree clean),
2. reads as a reader and detects which tidyings from the catalog apply, requiring that the trigger match *exactly*,
3. decides **First / After / Later / Never** (ch. 21) and builds a small plan (ch. 18, 19),
4. applies **one tidying per commit**, running the tests after each one and reverting if anything goes red,
5. reports what it applied, what it reverted, and what's left on the *Fun List*, citing chapter and page.

Never changes behavior. Never mixes.

## Layout

```
agents/tidier.md        the agent (frontmatter + prompt); what gets installed to ~/.claude/agents/
examples/               Part I — the 15 tidyings, one full chapter per file, verbatim from the book
examples/README.md      catalog index
managing/               Part II — Separate Tidying, Chaining, Batch Sizes, Rhythm, Getting Untangled, First/After/Later/Never
managing/README.md      index
theory/                 Part III — design, structure vs. behavior, economics, reversibility, coupling, cohesion, Conclusion
theory/README.md        index; each chapter closes with a "For the tidier" block (the decision rule the agent takes from it)
install.sh              copies the agent to ~/.claude/agents/tidier.md
assets/                 the book (pdf/epub) — gitignored, not pushed; the source everything else was extracted from
```

The agent reports in the language the task was given in, and reads top to bottom: role → *Contract* (seven non-negotiable rules) → *Inputs* → *Workflow* (safety net, read, detect, decide, apply, report) → *Report format* → *Reference* (where the book is and when to read what, a compact catalog of Part I, the forces of Part III).

The three directories hold the book **verbatim** (Parts I–III, chapters 1–33), split under **English** headings. The agent reads `examples/NN-*.md` before applying each tidying to verify the move matches the book's, `managing/21` and `theory/27` when the first/after/later/never decision isn't obvious, and `theory/29` and `theory/32` when the mess is coupling. If the directories aren't present, it works from the catalog and forces table embedded in the prompt, and says so.

## Install

```sh
./install.sh
```

Copies `agents/tidier.md` to `~/.claude/agents/tidier.md`. Claude Code re-reads `~/.claude/agents/` between turns: in an open session, `tidier` shows up in the agent list from the next message on (otherwise, restart the session).

## Use

From a Claude Code session, in a repo with tests:

> Use the `tidier` agent on `src/orders.py`. The behavior change that comes next: support volume discounts in `price_for()`.

Or with no behavior change in sight ("read to understand" mode, more conservative):

> Do a Tidy First pass with `tidier` on `lib/parser.js`.

Or after a change that already landed and exposed the mess (*after* mode, ch. 21):

> I just merged the volume discount into `price_for()`. Tidy after with `tidier`.

What you can hand it: the target, the next behavior change (or the one that just landed), the test command (if not, it detects one), and trailers for the commits.

## What it does NOT do

- Behavior changes, not even a "while I'm at it" bugfix.
- Big refactors: extracting an object/service, new abstractions — the book explicitly puts these out of scope for a tidying (ch. 17), and, for services, marks them as hard to undo (ch. 28).
- Continuing to tidy past what serves the next behavior change: "Save the tidying binge for later" (ch. 33).
- Working on a live Cuis image: there, the shared state is the image, not the working tree; use `cuis-tcr-tdd-driver`.

## Relationship with the skill `tidy-first`

The skill `~/.claude/skills/tidy-first/` is the **inline** guide (theory, when to load it, Java translations). This agent is the **worker**: starts cold, applies, and commits. They're independent; the agent brings its own examples.

## Source

Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023. ISBN 978-1-098-15124-9. Quotes are from the book; the examples are in Beck's original pseudocode.
