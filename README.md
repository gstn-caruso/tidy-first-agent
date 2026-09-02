# tidy-first-agent

A Claude Code **agent** that acts as a tidier per *Tidy First? A Personal Exercise in Empirical Software Design* (Kent Beck, O'Reilly 2023), with the book's 33 chapters extracted **verbatim** as reference material — plus a small skill so the main session can plan without loading any of it.

Given a file/diff/function — ideally along with the behavior change that comes next — the agent:

1. builds the safety net (working tree clean, tests green),
2. reads as a reader and detects which tidyings apply, requiring that the prompt match *exactly*,
3. decides **First / After / Later / Never** (ch. 21),
4. applies **one** tidying as one structural commit, reverting if anything goes red,
5. reports what it applied, what it reverted, what's on the *Fun List*, and what's still pending — citing chapter and page.

One tidying per invocation, then it stops. The batch is the caller's loop; the agent's memory between invocations is the repository, not the conversation. Never changes behavior. Never mixes.

## Layout

```
agents/tidier.md            the agent: contract, workflow, report format, the fifteen prompts
skills/tidier/SKILL.md      the inline guide: decide here, delegate the applying
references/                 chapters 1-33 verbatim, one file per chapter, + java.md
references/README.md        the index and the read map: which chapter answers which question
install.sh                  installs all three into ~/.claude
assets/                     the book (pdf/epub) — gitignored; the source everything was extracted from
```

Chapters 1–15 are the tidyings (prompt, move, caveats, what it chains into), 16–21 the discipline of fitting them into the workflow, 22–33 the theory. Each of 22–33 closes with a **For the tidier** block — the decision rule distilled from that chapter, the only non-verbatim text in the corpus.

## How the pieces spend tokens

The agent's prompt carries only what **every** invocation needs: the contract, the workflow, the fifteen prompts to spot them by, and the false positives that would turn a tidying into a behavior change. Everything used for exactly one of the fifteen — the move, the caveats, the chaining — lives in `references/NN-<slug>.md` and is read at the moment of applying it. Nothing else in the corpus is loaded unless a decision is genuinely unclear.

The rest of the budget is spent the same way: a dirty tree stops the run *before* the target is read, a named symbol or diff is read as that span rather than the whole file, detection stops at three candidates because only one gets applied, the test run is scoped to the target's module or class, and the report's `## Pending` is handed back as `plan` so a follow-up invocation does not pay for detection twice.

## Namespace

Everything this project installs lives under the name `tidier` — the agent, its skill and the references. It depends on nothing else in `~/.claude` and collides with nothing there: drop the repo on any machine, run `./install.sh`, and the agent works in any git repository with a test command.

## Install

```sh
./install.sh
```

Copies the agent to `~/.claude/agents/tidier.md`, the skill to `~/.claude/skills/tidier/SKILL.md`, and the references to `~/.claude/skills/tidier/references/` — one copy, reached by the agent by absolute path and by the skill by relative path. Claude Code re-reads both directories between turns: in an open session they show up from the next message on; otherwise, restart it.

## Use

From a Claude Code session, in a repo with tests:

> Use the `tidier` agent on `src/orders.py`. The behavior change that comes next: support volume discounts in `price_for()`.

Or with no behavior change in sight ("read to understand" mode, more conservative):

> Do a Tidy First pass with `tidier` on `lib/parser.js`.

Or after a change that already landed and exposed the mess (*after* mode, ch. 21):

> I just merged the volume discount into `price_for()`. Tidy after with `tidier`.

What you can hand it: the target, the next behavior change (or the one that just landed), the test command (if not, it detects one), the `## Pending` list from its previous report as `plan`, and trailers for the commits.

Each invocation ends with `## Next`. While it names a tidying, re-invoke; when it says done, the tidying commits are the tidying PR (ch. 16) and the behavior change goes in the next one.

## What it does NOT do

- Behavior changes, not even a "while I'm at it" bugfix.
- Big refactors: extracting an object/service, new abstractions — the book explicitly puts these out of scope for a tidying (ch. 17), and, for services, marks them as hard to undo (ch. 28).
- Continuing to tidy past what serves the next behavior change: "Save the tidying binge for later" (ch. 33).
- Working where the shared state is not a git working tree — a live Smalltalk image, a running notebook kernel. The whole safety net here is `git status` clean plus `git restore` on red; without it there is nothing to revert to.

## Source

Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023. ISBN 978-1-098-15124-9. Quotes are from the book; the examples are in Beck's original pseudocode.
