---
name: handoff-rules
description: Writes a HANDOFF.md when one agent stops and the next one takes over. The file records what was done, what is still open, what was tested and how, and who holds the task now. The next agent reads it before it acts. Fixes "the new agent started over, redid finished work and trusted a test nobody ran." Use when a session ends with work still left, before /clear, when you pass a task to a subagent or to another agent, and when you pick up work someone else started. Also on /handoff-rules.
---

# Handoff rules

The new agent started over. It redid finished work, missed what was left and trusted a test nobody ran.
The first agent knew all of it, but none of it was written down.
This skill writes one handoff file when an agent stops, and the next agent reads that file before it does anything.

## The principles
1. If it is not in the handoff file, the next agent does not know it.
2. Write down what is open and what was not tested. A gap in the file reads as done.
3. One agent holds the task at a time. Two holders make two versions.
4. The next agent reads first and acts after.

## Steps
1. Before you stop, write HANDOFF.md in the project folder. Put the task in one sentence at the top, and under it an `owner:` line that names who holds the task now.
2. Under `done:`, write what was done: each change, the files it touched and each decision with its reason. Write only facts the next agent can check.
3. Under `open:`, list the work that is still open, in the order it should be done, and say what blocks each item. If you tried something and dropped it, say what and why, so nobody tries it again.
4. Under `tested:`, list what was tested and how: the command or the steps, and the result. Then list what was not tested, and why. Anything not run is marked not run, never passed.
5. Pass the task. Change the `owner:` line to the next agent, then stop editing. The old session does not touch the files again.
6. The next agent reads HANDOFF.md first and runs `git status` and `git log` to check it. In two lines it says what it understood and what it will do first. Then it acts.
7. Each agent that stops updates `done:`, `open:`, `tested:` and `owner:`.

## Rules
- Write the handoff before /clear. Write it before /compact too, so it holds what the summary might drop.
- Keep the file short enough to read in a minute. Point to logs and files instead of pasting them in.
- If the `owner:` line is unclear, stop and ask the person. Two agents never work on the task at once.
- Before you build on a pass in `tested:`, run that check again yourself.
- If the file and the code disagree, trust the code. Fix the file and say what you changed.
