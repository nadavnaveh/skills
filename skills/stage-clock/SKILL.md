---
name: stage-clock
description: Writes a start and end time for every stage of one job in one file, splits each stage into working and waiting time, sorts the stages by minutes and fixes only the slowest one. Fixes "my agents take hours on one job, and I don't know which step is slow." Use when a chain of agents is slow, before you add agents or a faster machine, or when work sits waiting between stages. Also on /stage-clock.
---

# Stage clock

Your agents take hours on one job, so you guess which step to speed up, and you usually guess wrong. Nobody timed the stages, so the agents get the blame. This skill puts a clock on every stage, sorts the stages by minutes and fixes only the slowest one.

## The principles
1. Measure before you speed anything up. A guess usually picks the wrong step.
2. The slowest stage sets the pace of the whole chain, so it is the only one worth fixing.
3. Every stage has working time and waiting time. Often the waiting is the slow part, so the fix is a rule, not a faster machine.

## Steps
1. Write the stages of the chain in order, for example: write, check, build, render. Make one file, `stage-clock.md`, with one line per stage: stage, start, end.
2. Fill in the start and end of each stage. On a job that is running, write the time into the file when each stage starts and when it ends. On a job that already finished, take the times from real records: git commit times, file save times, log times, chat message times. When there is no record, ask the owner. If they only know roughly, write their answer and mark it "estimated". Never make up a time.
3. Split each stage into working time (an agent or a person is doing it) and waiting time (it sits for a reply, for rules that changed during the run, for a re-check of work that was already done, or in a queue).
4. Sort the stages by total minutes, slowest first, in one table: stage, working, waiting, total, share of the job. A row looks like this: `Writing | 50 min working | 6 h 10 min waiting | 7 h | 85%`. Then say in one line which stage is slowest and whether it is mostly working or mostly waiting.
5. Suggest one change for the slowest stage only:
   - Mostly waiting: change the rule. For example, settle the rules before the run starts, or do not re-check work that already passed.
   - Mostly working: change the work. For example, split it, or run its parts in parallel.
   Ask "Try this?" and start only after a yes.
6. Run the job again with the same clock and show the old and new numbers side by side. The stage that is slowest now is the next one to fix.

## Rules
- Never add agents or a faster machine before the clock shows the work itself is the slow part.
- Every time has its source next to it, or the word "estimated".
- One change per round, so you know which change moved the clock.
- Waiting on a person is a stage too. Time it like any other, without blame.
