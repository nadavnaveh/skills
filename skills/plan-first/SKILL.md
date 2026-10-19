---
name: plan-first
description: Decides whether a task needs a plan before any change, then writes that plan and waits for your yes. The plan agrees the goal in one checkable line, numbers every file it will touch, marks the steps that are hard to undo, maps an unfamiliar codebase first, and splits a big refactor into steps you approve one at a time. Fixes "It started changing things before I knew what it was going to do." Use when one change touches many files (a rename, a moved function, a changed name used everywhere), when the request is vague ("make it faster", "clean this up", "make it better"), when a step is hard to undo (deleting files or data, dropping a table, a database migration, a force push, a deploy, sending messages), when the agent starts in a codebase it has not read yet, and before a big refactor. Also on /plan-first.
---

# Plan first

The agent started changing things before anyone agreed what it would do. Halfway through, it had touched files nobody expected, or run a step nobody could take back.
A plan costs a few minutes. Undoing a wrong change costs much more.
This skill checks whether the task needs a plan, writes one that names things, and starts only after your yes.

## The principles
1. Plan first when there are many files, the goal is unclear, a step is hard to undo, the codebase is new or the refactor is big. Otherwise, just do the work.
2. A plan names things: the goal, every file, the risky step. "Update the code" is not a plan.
3. Agree on the goal before any code. If a word can mean two things, ask which one.
4. A step that is hard to undo waits for a person's yes, even inside a plan that was approved.
5. Read before you change. Nobody can plan well in a codebase they have not mapped.

## Steps
1. Check the five signs: many files, unclear goal, hard to undo, new codebase, big refactor. If none apply, say "No plan needed" in one line and do the work.
2. Plan without editing anything. In Claude Code, press Shift+Tab until the mode shows plan mode: the agent can read and propose, but not change files. Elsewhere, say plainly that nothing will be edited until the plan is approved.
3. **New codebase:** read it folder by folder before planning. Write a short map: what each main folder holds, where the program starts, and how the tests are run. If the project has no CLAUDE.md, offer to save the map there (in Claude Code, /init writes a starting one).
4. **Unclear goal:** ask the one question that decides it. "Faster" becomes "Faster at what: the page load or the test run? From how long to how long?" Write the answer as one line a stranger could check, such as "the home page loads in under 1 second". Do not plan the work until that line is agreed.
5. **Many files:** search the whole project for every place the change reaches, not only the files already open. List them numbered, with what changes in each. Say how many you found and how you searched. Example: renaming User to Member, file 1, file 2, file 3, each with its change.
6. **Hard to undo:** walk the plan step by step and mark every step that cannot easily be reversed (deleting files or data, dropping a table, a migration, a force push, a deploy, sending anything to people). Mark each one "ask", and write the way back: the backup, the commit, or "there is none".
7. **Big refactor:** split it into small steps, each one leaving the code working with the tests passing (for example "extract auth into its own module"). Number them.
8. Show the whole plan and ask "Go with this plan?" Start only after a yes.
9. Work in the plan's order and tick each numbered item as it is done.
   - At a step marked "ask", stop and ask again, right before it runs. Run the safe steps before it as normal.
   - In a big refactor, after each step show what changed and the test result, commit it with git so it can be undone on its own, and ask for a yes before the next step.
10. If the work finds something the plan missed (one more file, a new risk, a goal that no longer fits), stop, update the plan, show what changed, and ask again. Never widen the plan quietly.
11. At the end, report each numbered item as done, skipped (with why) or changed (with what), and check the result against the goal line from step 4.

## Rules
- No edits before a yes to the plan.
- A step that is hard to undo gets its own yes, at the moment it runs.
- A file that is not on the list is not touched without saying so first.
- Ask when it is unclear. A guess is not a goal.
- One refactor step at a time, each one working and committed before the next.
