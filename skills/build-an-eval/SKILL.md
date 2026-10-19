---
name: build-an-eval
description: Builds a small test from ten of your own past tasks, writes the right answer for each one before any run, and scores the agent pass or fail out of ten every time you change something. Fixes "I changed the prompt, and I can't tell if it got better or worse." Use when you are about to change a prompt, CLAUDE.md, a skill or the model, when an agent does the same kind of job again and again, or when someone says a change "feels better". Also on /build-an-eval.
---

# Build an eval

You changed the prompt, tried it once, and it felt better. Then a task that used to work broke, and nobody saw it.
One try and a feeling is not a test. This skill builds a test from ten of your own past tasks, writes the answers first, and scores every change pass or fail.

## The principles
1. Your own past tasks are the best test. Use real ones from last month, not made-up examples.
2. Write the right answer before the run. An answer written after the run describes what the agent did, not what was wanted.
3. Each task is pass or fail. Yes or no, not a feeling.
4. Same tasks, every change. A score only means something next to the score before it.

## Steps
1. Collect ten real tasks from last month: old sessions, the git log, tickets, emails. Include the ones that went wrong. Make an `evals/` folder with one file per task, numbered `task-01.md` to `task-10.md`. Paste the real input as it was. Do not tidy it.
2. Write the answer first. In each file, under the input, write `want:` and the answer you expect, for example `want: 412`. When there is no single answer, write a yes/no check a stranger could answer, like "names the late invoice". Show the ten wants and ask "Are these the right answers?" Run nothing before a yes.
3. Make one way to run all ten. For code, the agent writes a small script, for example `evals/run.sh`. For other work, write in `evals/README.md` what "run evals" means: each task goes to a fresh subagent that gets the input only, never the want.
4. Run the agent on all ten. Compare each result with its want and mark it **pass** or **fail**, with what came back next to what was wanted. Give the total, for example 8/10.
5. Save the score in `evals/results.md`: the date, what changed, the total, and which tasks failed.
6. Rerun on every change: a new prompt, a CLAUDE.md edit, a new skill, another model. Show the score before and after, side by side. If it dropped, name each task that went from pass to fail, and stop before the change ships. The owner decides.

## Rules
- Never change a want after a run to make it pass. If a want was wrong, say so and let the owner fix it.
- A task that did not run is not a pass. Say it was not run.
- Report a drop plainly, task by task. Never average it away.
