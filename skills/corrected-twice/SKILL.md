---
name: corrected-twice
description: Stops patching the output after the second correction on the same thing. It writes the correction as a rule in CLAUDE.md, finds the step in the plan that went wrong, redoes that step on one file with a check, and starts a fresh session with the new rule loaded. Fixes "I keep correcting the same thing." Use when you correct the agent on the same problem a second time (the same wrong format, the same missed instruction, the same bug coming back), when a fix brings back an error that was already fixed, or when you are about to type "no, again". Also on /corrected-twice.
---

# Corrected twice

You corrected it, and the same mistake came back. Then you corrected it again.
A patch fixes this one output, but the cause sits earlier: a rule nobody wrote down, or a step in the plan that was wrong or too big.
This skill stops the patching, writes the rule, goes back to the plan, and starts again clean.

## The principles
1. Once is a retry. Twice is a pattern. After the second correction, a third fix to the output won't land either.
2. A correction said in chat is gone next session. A correction written in CLAUDE.md is read every time.
3. The mistake started in a step of the plan, not in the last output. Fix the step.
4. Small steps fail small. One file, then a check, then the next.
5. A session full of failed tries keeps pulling the agent the wrong way. Start clean.

## Steps
1. Stop. When the same correction comes a second time, do not patch the output again. Say: "This is the second time for [the problem]. I am stopping to fix the cause."
2. Write the rule. Turn the correction into one specific line for CLAUDE.md, with its reason: "Dates: always ISO (2026-10-20), because the importer rejects other formats." Show the line and ask "Add this to CLAUDE.md?" Add it only after a yes. (/memory opens the file.)
3. Go back to the plan. List the steps that led to the output, in order. If there was no written plan, write down the steps you took. Check each one against the rule, starting from the first, and name the first step that went wrong: "Step 2 passed. Step 3, format, wrote dates with no rule."
4. Make that step smaller. Redo only that step, on one file, not ten at once. Then run a check a stranger could answer yes or no: "every date in this file is ISO". Show the result.
5. Do the next file only after the check passes, and check again. If a check fails, stop and go back to step 3.
6. Start fresh. When the step is fixed, write a short note of where the work stands, then ask "Start a fresh session with /clear?" Clear only after a yes. CLAUDE.md, with the new rule, loads at the start of the new session.
7. In the fresh session, check the first output against the rule. Report pass or fail, with what you saw.

## Rules
- Never fix the same problem a third time in the output. Fix the rule or the plan.
- One rule per correction, specific enough to check: "dates: ISO", not "be careful with dates".
- Never edit CLAUDE.md or clear the session without the owner's yes.
- One file, then a check. Never redo everything at once.
