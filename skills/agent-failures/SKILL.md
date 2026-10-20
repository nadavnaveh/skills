---
name: agent-failures
description: Watches a task for the five ways agents fail (Drift, Sure and wrong, Loops, Forgets, Overreach), catches each one at the step where it starts, and steers back with one move per failure. Fixes "the agent went wrong, and I only noticed at the end." Use at the start of any task you hand to an agent, when a session has run long, when the agent says "fixed" or "done", when the same error comes back after a fix, when it ignores something you decided earlier, or when it touches files you never named. Also on /agent-failures.
---

# Agent failures

The agent went wrong, and you only noticed at the end. Each step looked reasonable on its own, so nothing seemed off until the damage was done. Agents fail in five known ways. This skill writes down what each one is measured against before the work starts, then checks for all five while the work runs.

## The principles
1. You can only catch a failure you can name. There are five: Drift, Sure and wrong, Loops, Forgets, Overreach.
2. You catch each failure by comparing the work to something written down: the goal, a check, an error log, a decision, an allowed list.
3. Catch it at the step where it starts, not at the end.

## Steps
1. Before any work, write four things at the top: the goal in one sentence, the files or folders the agent may touch, the decisions already made (for example "use tabs"), and the check that proves it works. Put lasting decisions in CLAUDE.md so they survive a long session and /compact.
2. **Drift: slowly moves off the goal.** Before each new step, ask "does this step serve the goal?" If the goal is login and the step is rewriting the UI, stop and go back to the goal.
3. **Sure and wrong: sounds certain, is wrong.** When the agent says "fixed" or "100% done", run the check. If the tests say three still fail, report the three, not the claim.
4. **Loops: tries the same fix again.** Keep a short log of each error and the fix tried for it. If the same error comes back a second time, stop patching. Say what was tried, then look for a new cause or ask the person.
5. **Forgets: loses what you decided earlier.** Before you hand in work, check it against the list of decisions. If it uses spaces where you decided on tabs, fix it and add the decision to CLAUDE.md. If the session is long, start fresh with /clear and the four things from step 1.
6. **Overreach: goes past what it was allowed.** Before each edit, check that the file is on the allowed list. If it is not, ask first. At the end, run git status and compare every changed file to the list.
7. Report each of the five as caught or clear, with the evidence: the step, the test output, the repeated error, the decision, the file.

## Rules
- A claim is not a check. "Fixed" counts only with the check result next to it.
- The same error twice means stop, not a third patch.
- A file that is not on the allowed list waits for a yes, even if the change looks small.
- Never change the goal, the allowed list or a decision quietly. Say it and ask.
