---
name: write-the-check
description: Writes one test with you before the agent starts (one exact command, with examples you chose or approved), adds the rule "don't say done until it passes", then has the agent run it and fix the cause of every failure. Fixes "The agent said done, and it only tested itself on examples it picked." Use before you hand an agent a task a command can test (a function, a script, a bug fix, a data change), when you are about to ask for a build, and when an agent says done and you want to know against which check. Also on /write-the-check.
---

# Write the check

Your agent said done. Ask it: against which check? If it wrote its own check, it also picked the examples, so it graded itself. This skill writes the check with you before the agent starts, and holds the word "done" until the check passes.

## The principles
1. Whoever writes the check decides what gets checked.
2. An agent grading itself uses examples it picked. We ran one small task six times (hours and minutes to seconds). Three runs got only the task, and each said done after checking itself this way.
3. Not yet is information, and it may point at the tooling, not the code. Our other three runs got a test and the rule. They said not yet and found a broken tool on our machine that crashed the check before it started. When we checked all six ourselves, the code was right in every one, so the first three's done was right by luck.

## Steps
1. Before any work, ask the person what the task must do, and for a few examples with the right answer for each ("1h 30m gives 5400"). If they have none, suggest some and get a yes on each one. Write no code yet.
2. Turn those examples into one test and one exact command that runs it, such as `python3 -m pytest test_duration.py`. The command must end in a clear pass or fail.
3. Show the examples and the command. Ask "Is this the check?" Start only after a yes.
4. Write the rule plainly at the top of the task: "Don't say done until this command passes." Put the command under it.
5. Do the work, then run the exact command.
6. If it passes, say done and show the output.
7. If it says not yet, read why. Quote the real error, name the cause in one line, fix the cause and run the same command again. If the cause is the tooling and the fix is outside this task, stop and show the person the error and what you need.

## Rules
- Never reword, weaken or skip the check to get a pass. Only the person can change it.
- A crash, or a run with no tests, is a not yet.
- Never write "done" without the passing output next to it.
- A pass proves what the examples cover and nothing more. Say so if a case was left out.
