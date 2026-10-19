---
name: agent-patterns
description: Picks the right way to run several agents on one job (Parallel, Debate, Pair, Pipeline or Manager), says why, and runs it in Claude Code with subagents. Fixes "I opened five agents and got five messes." Use when a task is big enough to split, when you want a second opinion before deciding, when work must be checked before it is called done, or when you are about to start more than one agent. Also on /agent-patterns.
---

# Agent patterns

You opened five agents and got five messes. Adding agents does not finish the job faster. The shape of the job decides how the agents should work together. This skill reads the shape of the task, picks one of five patterns, and runs it with subagents.

## The principles
1. The shape of the job picks the pattern. The number of agents comes after.
2. One owner per file at a time.
3. A subagent's "done" is a claim, not a pass.

## Steps
1. Write the task in one sentence.
2. Ask these five questions and pick the pattern that fits best:
   - **Parallel**: are there separate pieces that do not touch each other? One subagent per piece, all at the same time, each on its own files or its own git worktree. You merge at the end.
   - **Debate**: is it a choice with real trade-offs? Two or three subagents each argue one option with evidence. A judge (you or a fresh subagent) gets only the written arguments, in shuffled order, so the first one does not win by going first. The judge decides.
   - **Pair**: must it be right, not just done? One subagent writes. A second one checks the work against written criteria and sends it back with the exact problem. If it has not passed after three rounds, stop and ask the person.
   - **Pipeline**: does each step need the one before it? Each subagent does one step and hands a file to the next: research, then plan, then build, then test.
   - **Manager**: is the goal big and unclear? The main session splits it into tasks, gives each task to a subagent, and checks every result.
3. Say which pattern you picked and why, in two lines. Ask "Run it like this?" and start only after a yes.
4. Give every subagent a brief: the goal, the files it may touch, what it must not change, and how its work will be checked.
5. Never let two agents edit the same file at the same time. Give them separate files or separate worktrees.
6. Check every result yourself before you accept it.
7. Report on each agent: what it did, how it was checked, and whether it passed or failed, with the evidence.

## Rules
- Patterns can nest: a Manager may run its tasks in Parallel and run each task as a Pair.
- The person decides where it matters: the goal, anything hard to undo, and the final yes.
- If a Pair has not passed after three rounds, it goes back to the person, not into a fourth round.
- If agents keep fixing the same thing, stop and go back to the plan instead of adding more agents.
