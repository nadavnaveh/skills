---
name: ask-first
description: Before the agent writes code on a vague task, it asks until the goal, the why and what done looks like are clear, asks every decision it would otherwise guess with a suggested answer, and writes your answers as one definition with a yes/no check. Fixes "I asked for one line of work, and it made several decisions for me without asking." Use when a request is one short line, or touches data, permissions, dates or customers. Also on /ask-first.
---

# Ask first

You asked for one line of work, and the agent made several decisions on the way. In our sample it made seven. It told you about some only after the code, and about one never. This skill asks you first, so each guess becomes your decision.

## The principles
1. Every guess the agent makes is a decision that belongs to the owner.
2. Ask before the code. A choice you hear about afterwards was made for you.
3. Suggest an answer to each question, so answering is fast.
4. Skip it when the task is small and every guess is easy to undo.

## Steps
1. Check the size. If principle 4 applies, say so in one line and do the work.
2. Write nothing yet. Read what the task touches.
3. Ask until three things are clear: the goal, why it is wanted, and what done looks like.
4. List the decisions you would have to guess: which records go in, who may use it, what private data is included, the time zone, the edge cases. Include the ones you would not mention. Keep only the ones that change the result, usually five to eight. Seven was our sample, not a rule.
5. Ask them all at once, numbered, each with your suggested answer, so the owner can reply "yes to all except 3". If an answer opens a new question, ask again before building.
6. If reading turned up an existing problem, such as a date filter that drops the last day, list it as its own item. Do not fix it without a yes.
7. Write the answers as one definition: the goal, the decisions and one yes/no done check. Build only after the owner says yes to it, and run the check at the end.

## Rules
- The line to paste before a vague task: "Before you write code, ask me about every decision you would have to guess."
- In plan mode (Shift+Tab), ask the questions inside the plan.
- A decision you never mentioned is a decision you made for the owner.
- The owner's answer beats your suggestion.

## What the proof shows, and what it does not
The story is in scripts/voice.v5.he.paras.txt and scripts/caption.he.v2.txt. It was our own setup: one sample store app, one task (add CSV export to the orders page), three runs each way. Without the line, the agent wrote code every time and never mentioned the time zone. With the line, it wrote no code, asked about all seven decisions every time, and found an existing date filter bug in two runs. It does not show that the agent's guesses were wrong, only that it made them without the owner. It does not show a success rate, better code, or other tasks or agents. The Matt Pocock quote was not checked.
