---
name: plan-first
description: Decides whether a task needs a plan before any change, writes that plan and waits for your yes. It maps a new codebase, agrees the goal, numbers every file, marks the steps that are hard to undo, and splits a big refactor into steps you approve one at a time. Fixes "It started changing things before I knew what it was going to do." Use when one change touches many files, when the goal is vague ("make it faster"), when a step is hard to undo (deleting data, dropping a table, a deploy), when the agent starts in a codebase it has not read, or before a big refactor. Also on /plan-first.
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
2. Plan without editing anything. In Claude Code, press Shift+Tab until the mode shows plan mode; elsewhere, say plainly that nothing will be edited yet. Build the plan with the steps below that apply, show it, and ask "Go with this plan?" Start only after a yes.
3. **New codebase:** read it folder by folder. Write a short map: what each main folder holds, where the program starts, and how the tests run. If the project has no CLAUDE.md, offer to save the map there (in Claude Code, /init writes a starting one).
4. **Unclear goal:** ask the one question that decides it. "Faster" becomes "Faster at what: the page load or the test run? From how long to how long?" Write the answer as one line a stranger could check, such as "the home page loads in under 1 second". Plan the work only after that line is agreed.
5. **Many files:** search the whole project for every place the change reaches, not only the files already open. List them numbered, with what changes in each, and say how many you found. Example: renaming User to Member lists 3 files, each with its change. Tick each one as it is done.
6. **Hard to undo:** walk the plan and mark every step that cannot easily be reversed (deleting files or data, dropping a table, a migration, a force push, a deploy, sending anything to people) with "ask". Run the safe steps before it as normal. At the "ask" step, stop and ask again, right before it runs.
7. **Big refactor:** split it into small numbered steps, each one leaving the code working with the tests passing (for example "extract auth into its own module"). After each step, show what changed and the test result, and ask for a yes before the next. A git commit per step makes each one easy to undo.

## Rules
- No edits before a yes to the plan.
- A step that is hard to undo gets its own yes at the moment it runs, with the way back named: the backup, the commit, or "there is none".
- A file that is not on the list is not touched without saying so first.
- If the work finds something the plan missed, stop, update the plan and ask again. Never widen it quietly.
- Ask when it is unclear. A guess is not a goal.
