---
name: calls-to-keep
description: Marks the five calls a person keeps when an agent works alone (the goal, any step that cannot be undone, the merge into main, spending money or using keys, and the final look before release) and makes the agent stop and ask at each one. Fixes "the agent made a call that should have been mine." Use when you hand an agent a task to run on its own, before it deletes, overwrites or drops anything, before it merges, deploys or pushes to main, before it pays, signs up for a paid plan or touches a key or password, and before anything ships to users. Also on /calls-to-keep.
---

# Calls to keep

The agent made a call that should have been yours. It deleted, merged, paid or shipped because nobody told it where to stop. This skill names the five calls you keep, writes them down, and makes the agent stop and ask at each one.

## The principles
1. The agent does the work. You keep the calls that set the goal, spend money or cannot be taken back.
2. A stop works only if it is written down before the work starts.
3. Asking costs a minute. A missing undo can cost the project.

## Steps
1. **The goal.** Before any work, ask the person to write what done means, in one to three lines a stranger could answer yes or no. Put them at the top as "Done means:". Start only after the person writes or approves them. At the end, check every line and show the result.
2. **No undo.** Before any step that cannot be undone (rm -rf, deleting files, dropping a table, overwriting data, a force push), stop. Say exactly what will be lost. Make a backup first (a copy, a commit or an export) and say where it is. Run the step only after a yes.
3. **Production.** Do the work on a new git branch, never on main. When it is ready, show what changed and ask "Merge into main?" Merge only after a yes. The same goes for a deploy.
4. **Money and access.** Before anything that spends money (a purchase, a paid plan, a paid service), say what it is for and the amount, like "$40 for one month of X", and wait. Do the same before using a key or password or asking for new access. Never paste a key into the chat or into a file that gets committed.
5. **Final check.** Before anything ships (a release, a post, an email to customers), hand it to the person: what it is, where to look, and how each "Done means" line came out. Ship only after they have looked and said yes.
6. Write these five calls into CLAUDE.md under "Calls I keep", so every new session reads them. Add any the person names for this project, like "never email the client list".
7. When you stop at a call, put the question in the first line, say what the step will do, and wait. Keep working on anything that does not depend on the answer.

## Rules
- Silence is not a yes. A yes to one call is not a yes to the next.
- If you are not sure a step can be undone, treat it as one that cannot.
- Never work around a stop with another tool, a new path or smaller steps that add up to the same thing.
- If the person says no, drop that step and say what it leaves undone.
