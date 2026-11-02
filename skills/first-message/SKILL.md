---
name: first-message
description: Turns a loose ask into a first message with the files, the exact change and a done test, and keeps one task per conversation. Fixes "My allowance runs out long before my work does." Use before you start a change in Claude Code, Codex or a similar agent, when you are about to send a short general ask like "add a reset button", when your usage limit keeps running out, and when you are about to start a new task in an old conversation. Also on /first-message.
---

# First message

Your allowance runs out before your work does. Every turn sends the conversation again, so the number of turns drains it, not the length of your prompt.
This skill turns a loose ask into a first message with the files and a done test, which saves the agent its search turns.

## The principles
1. Turns cost, not words. In our run (Claude Code, Haiku 5.5, a 2-file change, 3 runs each), a general ask took 10-12 turns and 172K-219K tokens. A precise ask took 6 turns and about 118K. Do not claim the same ratio for big tasks, other models or Codex.
2. A file you name is a search the agent does not have to run.
3. One task per conversation. An old task is sent again on every new turn.

## Steps
1. Check the conversation first. If the ask continues the task here, stay. If it holds another task, ask the user to save what they need in CLAUDE.md or a file, run /clear, and give the ask again.
2. Take the loose ask as it is and run one search for the likely files. If the user already named the files, skip the search.
3. Show the files and ask "Are these the right files?" Go on only after a yes.
4. Write the exact change, one line per file: what is added, removed or changed.
5. Write what counts as done: a test to run, or something the user can see. Then show the whole message and start only after a yes.
   Example: "Add a Reset button to the counter. In src/counter.js add a reset function that sets the count to 0. In src/main.js add a Reset button next to the counter button that calls it. Do not install anything. Done = the Reset button shows on the page and clicking it sets the count to 0."

## Rules
- A path beats a description. "src/main.js" saves a search, "the main file" does not.
- If you cannot write what done means, the task is not ready to send.
- If the task has more than one goal, split it into separate conversations.
- To compare two asks, run each with claude -p and --output-format json, then read num_turns and usage.
