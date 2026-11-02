---
name: first-message
description: Turns a loose ask into a first message with the files, the exact change and a done test, and keeps one task per conversation. Fixes "My allowance runs out long before my work does." Use before you start a change in Claude Code, when you are about to send a short general ask like "add a reset button", when your usage limit keeps running out, and when you are about to start a new task in an old conversation. Also on /first-message.
---

# First message

Your allowance runs out before your work does. In Claude Code, every model request sends the conversation again, so the back-and-forth costs more than the length of your prompt.
In our run (Claude Code, Haiku 5.5, a 2-file change, 3 runs each), a general ask used about 172K to 219K tokens, and a precise ask about 118K. We measured it on that small task, so do not expect the same saving on big tasks, other models or Codex.
This skill turns a loose ask into a first message with the files and a done test, which saves the agent its searches.

## The principles
1. The back-and-forth costs, not the words.
2. A file you name is a search the agent does not have to run.
3. One task per conversation. An old task is sent again with every new request.

## Steps
1. Take the loose ask as it is and run one search for the likely files. If the user already named the files, skip the search.
2. Show the files and ask "Are these the right files?" Go on only after a yes.
3. Write the exact change, one line per file: what is added, removed or changed.
4. Write what counts as done: a test to run, or something the user can see. Then show the whole message and ask "Is this the right message?"
   Example: "Add a Reset button to the counter. In src/counter.js add a reset function that sets the count to 0. In src/main.js add a Reset button next to the counter button that calls it. Do not install anything. Done = the Reset button shows on the page and clicking it sets the count to 0."
5. Check the conversation. If the ask continues the task here, start after a yes. If this conversation holds another task, keep the message on screen, ask the user to save what they need in CLAUDE.md or a file, run /clear, and paste the message.

## Rules
- A path beats a description. "src/main.js" saves a search, "the main file" does not.
- If you cannot write what done means, the task is not ready to send.
- If the task has more than one goal, split it into separate conversations.
- To compare two asks, run each with claude -p and --output-format json, then read num_turns and usage. A turn is the count Claude Code reports, and one request can hold several: our run took 10-12 turns in 4-5 requests, against 6 turns in 3.
