---
name: agent-patterns
description: Picks the right way to run several agents on one job (Parallel, Debate, Pair, Pipeline or Manager), says why, and runs it in Claude Code with subagents. Fixes "I opened five agents and got five messes." Use when a task is big enough to split, when you want a second opinion before deciding, when work must be checked before it is called done, or when you are about to start more than one agent. Also on /agent-patterns.
---

# Agent patterns

More agents is not more done. The job's shape decides how agents should work together. This skill reads the shape of the task, picks one of five patterns, and runs it.

## The five patterns
| Pattern | Shape of the task | How it runs |
|---|---|---|
| **Parallel** | Separate pieces that don't touch each other | One subagent per piece, at the same time; each works on its own files (or its own git worktree). You merge at the end. |
| **Debate** | A decision with real trade-offs | Two or three subagents each argue one option with evidence; a judge (you or a fresh subagent) reads all of them and decides. |
| **Pair** | Work that must be right, not just done | One subagent writes, a second one checks against written criteria; the work goes back with the exact problem until it passes. |
| **Pipeline** | Steps that depend on the step before | Each subagent does one step and hands a file to the next (research → plan → build → test). |
| **Manager** | A big goal with many unknown parts | The main session splits the goal into tasks, hands each to a subagent with a clear brief, and checks every result before accepting it. |

## Steps
1. Write the task in one sentence, and what done means as yes/no checks.
2. Read the shape: are the pieces independent (Parallel)? Is it a choice (Debate)? Must it be checked (Pair)? Is it a chain (Pipeline)? Is it big and unclear (Manager)? Patterns can nest: a Manager may run its tasks in Parallel, and each task as a Pair.
3. Say the pattern you picked and why, in two lines. Ask "Run it like this?" and start only after a yes.
4. Give every subagent a brief: the goal, the files it may touch, what it must not change, and how its work will be checked.
5. Never let two agents edit the same file at the same time. Use separate files or separate worktrees.
6. Check every result before you accept it. A subagent's "done" is a claim, not a pass.
7. Report per agent: what it did, the check, pass or fail with evidence.

## Rules
- One owner per file at a time.
- The person decides where it matters: the goal, anything hard to undo, and the final yes.
- If agents keep fixing the same thing twice, stop and go back to the plan instead of adding more agents.
