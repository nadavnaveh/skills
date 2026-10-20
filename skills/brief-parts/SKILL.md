---
name: brief-parts
description: Writes a five-part brief before the agent starts: a one-line goal, what done looks like, what must not change, the key files, and the test that proves it works. Fixes "I explained the task five times before the agent got it right." Use before you hand any task to an agent or a subagent, when a request is longer than one line, when the agent keeps asking what you meant, guesses wrong or touches files it should not, and whenever you write instructions for a subagent. Also on /brief-parts.
---

# Brief parts

You asked for a change, and then spent an hour answering questions and fixing guesses. The agent did not have what was in your head: the goal, the finish line, what to leave alone, where to look and how to check. This skill writes those five parts down once, before the work starts.

## The principles
1. If the goal does not fit in one sentence, it is not clear yet.
2. Done is a finished result you can describe, not an activity.
3. What must not change is part of the task, so say it.
4. Point to the files, so the agent does not have to search for them.
5. A brief without a check ends in "I think it works."

## Steps
1. **Goal.** Write one sentence the agent can repeat: "goal: let shoppers apply one discount code at checkout." Ask the agent to repeat it back, word for word. If it changes the sentence or adds to it, the goal is not clear yet. Rewrite it.
2. **Done when.** Describe the finished result in one to three lines a stranger could answer yes or no: "done when: a valid code lowers the total" and "an expired code shows an error". Each line says what you will see, not what the agent will do.
3. **What stays.** Name what must not change: a folder, an API, a file, a behavior. "Do not change api/v1." If the work seems to need it, the agent stops and asks instead of changing it.
4. **Key files.** List the files where the work lives: "src/cart.ts". If you do not know them, the agent finds them first and shows you the list before it edits anything.
5. **How to check.** Name the test or command that proves it works, and what a pass looks like: "run the cart tests, 6 of 6 pass". If no test exists, agree on one before the work starts.
6. Put the five parts in one block at the top of the request, show it, and ask "Is this the brief?" Start only after a yes.
7. At the end, run the check and report each done-when line as true or false, with the test output. Say whether anything under "what stays" was touched.

## Rules
- Write the brief once. If a part changes during the work, update the brief and say so.
- The agent never edits what is under "what stays". It asks.
- A subagent gets the same five parts. It cannot see your conversation.
- No "done" without the check output next to it.
