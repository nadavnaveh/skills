---
name: one-task-gate
description: Builds a gate for one task you give your agent often. It writes what good means as 5 to 8 yes-or-no questions before the work, then a separate checker with no access to the conversation answers each one from the result alone, quoting the line that proves it. Fixes "my agent checks its own work, and it always says it's good." Use when one task keeps coming back (a report, a post, a client email, a page), when you keep finding problems after the agent said it was finished, or when you want a check you do not have to do yourself. Works pasted into any agent. Also on /one-task-gate.
---

# One-task gate

These are instructions you paste into your agent, so it builds you a gate like this for one task. Your agent grades its own work and says it is good, because it checks what it meant to make, not what it made. This gate writes what good means before the work, and a checker that never saw the conversation decides. Use it in Claude Code, Codex, Cursor or any other agent, or on /one-task-gate.

## The principles
1. Good is a list of questions, written before the work. Questions written afterwards describe what was made.
2. A stranger must be able to answer each question from the result alone.
3. The one who did the work does not judge it.
4. A yes needs a quoted line. A no has no override.

## Steps
1. Ask which one task the owner gives you often, and give it a short name. If `checks/<task>.md` exists, read it and start from those questions.
2. Otherwise write what good means as 5 to 8 yes-or-no questions. A stranger must be able to answer each one from the result alone. Not "is it clear?" but "does the first line name who it is for?"
3. Show the questions and ask "Is this what good means?" Wait for the owner's OK. Then save them to `checks/<task>.md`, so next time starts from them.
4. Do the task.
5. Do not judge it yourself. Start a separate checker with no access to this conversation: a fresh subagent. Give it only the result and the questions. The result means the real thing (the file, the page text, the output), never your summary of it. If you cannot start a subagent, say so, and have the owner paste those two things into a new chat. The checker answers each question yes or no and quotes the line that proves it.
6. Any no means not done. Fix only what the no points at, then start a new checker with the same questions. Do this at most twice.
7. If every answer is yes, show the answers with their quotes. If a no remains after the second re-check, stop. Show the question and the line, or say that no line was found.

## Rules
- An answer with no quote counts as no. So does a quote that is not in the result.
- Never change a question to get a yes. If a question is wrong, ask the owner.
- The checker reads and answers. It never fixes.
- Never tell the checker why you made a choice. Reasons are how you win it over.
- Our copy gate stopped at least 88 of 115 scripts over 10 days, before any of us read them. That counts stops, not whether every stop was right.
