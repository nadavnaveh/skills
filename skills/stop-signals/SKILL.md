---
name: stop-signals
description: Watches a working session for five signals that it is time to stop (the same error twice, a jump in cost, edits to files nobody asked for, a plan that drifted, and no passing test in 30 minutes), then pauses and re-plans with the person before the work goes on. Fixes "I let it keep going, and it kept getting worse." Use during any long task, when an error comes back after a fix, when the spend climbs fast, when files you did not name show up in the changes, when you can no longer say what the agent is doing, or when many edits have gone by without a test. Also on /stop-signals.
---

# Stop signals

You let it keep going, and it kept getting worse. Each step looked like progress, so nobody stopped to ask if the plan still held. This skill names five signals that mean stop, and what to do at each one: press Esc, then re-plan together.

## The principles
1. Stopping is a step, not a failure. Esc stops the current turn, and the work so far stays.
2. A signal means the plan is wrong, not that the agent should try harder.
3. Re-plan together. The person agrees the next move before the agent goes on.

## Steps
1. Before the work starts, write the task, the files it may touch and the test that shows it works. Each signal is checked against these.
2. Watch for the five signals while the work runs:
   - **Same error twice**: the same error comes back after a fix. Do not try a third fix of the same kind. Try a new approach instead.
   - **Cost jumps**: check /cost now and then. If the spend per hour jumps, for example from $0.40 to $9.80, it is likely a loop. Find the step that repeats.
   - **Unasked edits**: run `git status` to see which files changed. If you asked for auth.ts and billing or infra files changed too, pause and narrow the scope back to the files you named.
   - **The plan drifted**: if you can no longer say what the agent is doing or why, ask it to restate the plan.
   - **No test in 30 minutes**: thirty minutes and 14 edits with no test run is a signal. Ask for one test that passes.
3. When a signal shows, the person presses Esc. If the agent sees the signal first, it stops on its own. Either way, it says which signal it saw, with the evidence: the error text, the cost, the list of files, or the time since the last test.
4. Ask the agent to restate the plan in three lines: the goal, what is done and what is next. Use plan mode (Shift+Tab) so nothing is edited while you re-plan.
5. Agree one next move that fits the signal: a new approach, the repeating step removed, the scope narrowed, or one test that passes. Undo unasked edits with git only after the person says yes.
6. Go on only after the person says go to the restated plan.
7. After the restart, check the same signal again before the next big step.

## Rules
- Two of the same error means a new approach, never a third try of the old one.
- Files outside the agreed list are not kept without the person's yes.
- No progress claim without a test that passed.
- Stop on the first signal. Do not wait for a second one.
