---
name: stop-rule
description: An instruction you paste into your agent, so it stops itself after two rounds with no progress. It writes what done looks like, says after each round what closed, stops after two rounds with no progress, and shows you the draft, the failing checks and what changed in each round. Fixes "The agent kept working, and nothing moved." Use at the start of any task that may take several rounds, when an agent keeps rewriting the same draft, when each fix opens a new problem, or when tasks open faster than they close. Works pasted at the start of a task or kept in a rules file such as CLAUDE.md, in any agent. Also on /stop-rule.
---

# Stop rule

The agent kept working, and nothing moved. In one week we opened 165 tickets, and when we counted, 15 were marked done (our own tickets, and a ticket can be done without being closed). One agent rewrote the same draft five times, and the score ended lower than it started.

Rounds look like work even when they move nothing. This is an instruction you paste into your agent, so it stops itself after two rounds with no progress.

## The principles
1. Progress means something closed toward "done". Opening a task is not progress.
2. Rounds that move nothing still look like work, so write the limit before the work starts.
3. Two rounds, then a person looks.
4. When each fix opens another problem, look at the check too. In our case the problem was in the check, not the draft.

## Steps
Here's the instruction. Paste it into your agent at the start of a task (or keep it in its standing instructions file, e.g. CLAUDE.md):

---

Stop rule for every task:

1. Before you start, write in one sentence what "done" looks like for this task, and show it to me.
2. After each round of work, write one line: what closed in this round, and did it move us toward "done". Opening a new task does not count as progress.
3. If two rounds pass with no progress toward "done", stop. Do not start a third round.
4. When you stop, show me side by side: the current draft, the checks that still fail, and what changed in each round.
5. If one fix solves a problem and opens another, say so plainly. That's a sign the problem may be in the check, not the work.

---

That's it. Two rounds, then a person looks.

On /stop-rule, apply these five steps to the task at hand and show step 1 first.

## Rules
- Write the one line after every round, including a round that closed nothing.
- After two rounds with no progress, there is no small extra round.
- After a stop, the person decides what comes next. The agent waits.
- Step 5 is a sign, not a verdict. Not every loop is a broken check.
