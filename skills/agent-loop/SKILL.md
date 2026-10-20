---
name: agent-loop
description: Runs every task as the agent loop (plan the next step, act with one tool call, observe the result, check that it worked, then stop or go another round) and never skips the check. Fixes "the agent made the change and never checked if it worked." Use on any task that changes something (fix a bug, add a feature, edit a document, change a setting), when an agent is about to report a change as finished without running anything, and when a fix keeps coming back. Also on /agent-loop.
---

# Agent loop

The agent made the change and said it was fixed. Nobody ran the test.
Every agent runs the same loop: plan, act, observe, check, then stop or go again. Most skip step 4, the check, because the edit went through and that feels like success.
This skill runs all five steps in every round, and stops only when a check has passed.

## The principles
1. An edit that went through is not a fix that works. Only the check can say it worked.
2. Every result the agent reads stays in its context window. Read what you need, not everything.
3. The check decides the next move, not how sure the agent feels.
4. A failed check means another round with one change, not a bigger guess.

## Steps
1. **Plan.** Write the next steps as a short list, for example "find the bug, fix it, run the tests". Name the check that will prove it works: a command such as `npm test`, a page to open, or a result to compare. For a larger change, use plan mode (Shift+Tab) and agree the plan before any edit.
2. **Act.** Make one tool call for one step: read a file, edit a line, or run a command. Say which file and which line you are changing.
3. **Observe.** Read what the tool sent back before you make the next move. Did the edit land where you meant it to? Did the command print an error? Keep reads small: search first, then read only the lines around the hit, so the window grows only by what you need.
4. **Check.** Run the check you named in step 1. Report the real output, such as "42 of 42 tests pass", not "it should work". If you cannot run it, say so and give the exact step the person can take to run it.
5. **Next or stop.** If it passed, stop and report the evidence. If it failed, write what failed, change the plan for that one cause, and start the next round at step 1.
6. After three rounds without a pass, stop. Bring the person what you tried, what each check showed, and what you think is wrong with the plan.

## Rules
- Never write "fixed", "done" or "works" without the check result next to it.
- One round, one change. Do not stack three changes and then check once.
- Report each round in one line: the round number, what changed, the check, and pass or fail.
- A round that skipped the check does not count as a round.
