---
name: prompt-ways
description: Adds five small habits to a request before the agent starts: one good example, who it is for, a plan first, a check it can run, and a list of what it could not confirm. Fixes "the answer was close, and I still had to fix it myself." Use when you write a request for any task (a piece of writing, a code change, a report, a fix), when an answer came back in the wrong shape or for the wrong reader, when the agent started building before you agreed, or when it said it was right and you could not tell. Also on /prompt-ways.
---

# Prompt ways

The answer came back close, and you still had to fix it yourself. The request left out what was in your head: the shape you wanted, who reads it, and how to tell it works. So the agent guessed. This skill adds five small habits to the request before the work starts.

## The principles
1. One good example says more than a paragraph of description.
2. Every answer is written for someone. Name them, or the agent writes for no one.
3. Agree the plan before anything changes.
4. A check the agent can run beats a promise that it works.
5. What the agent could not confirm matters as much as what it did.

## Steps
1. Read the request and find what is missing: an example, a reader, a plan, a check, a list of unknowns. Fill only what is missing.
2. **Example.** Add one good example of the result, marked `like:`. Use a real one: a past email, a table row, a function the person liked. Ask for the same shape. If there is none, ask the person for one before you start.
3. **Audience.** Add who reads the result, marked `for:`, for example "for: a new customer who has never used the app" or "for: the developer who looks after this code". Write for that reader: their words, their level, and what they need to do next.
4. **Plan first.** For any task that changes files, show a plan before any edit. In Claude Code, plan mode (Shift+Tab) lets the agent read but not change anything. Number each step: read code, the files it will change, how it will be checked. The person ticks each step. Build only the steps that got a yes.
5. **A check.** Name one check the agent can run itself: `npm test`, a script, a page to open, a number that must match. Run it after the change. If it fails, read the failure, fix it and run it again.
6. **Unknowns.** Ask: "What could you not confirm?" End the answer with two lists: checked, each with how it was checked, and `unverified:`, each with why it could not be checked.
7. Report the result, the check output as it came back, and the `unverified:` list.

## Rules
- One example, not five. The answer copies its shape, so pick a good one.
- A step the person did not tick is not started.
- If the check cannot be run, say so and put the result under `unverified:`.
- Nothing moves from `unverified:` to checked without a check that ran.
