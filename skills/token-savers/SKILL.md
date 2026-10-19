---
name: token-savers
description: Keeps a session small and cheap with five habits: a new session for each new task, search before reading, read only the lines needed, short answers, and an opening that stays the same so it is cached. Fixes "my tokens run out and the session gets slow the longer I work." Use when you start a new task in an old session, before opening a file to find one thing, when you are about to read a whole large file, when you want a short answer, and before you switch models or edit CLAUDE.md in the middle of a session. Also on /token-savers.
---

# Token savers

The tokens ran out halfway through the day, and the session got slower with every message. Each message sends the whole conversation again: every file read, every long answer and every old task. This skill keeps that conversation small, so each message costs less.

## The principles
1. Each message re-reads it all. Anything in the session is paid for again on every turn, so what you add once keeps costing.
2. New task, new session. An old task left in the session is paid for on every message of the new one.
3. Find the line, then read it. Search for the word first, then read only the lines around it: 40 lines, not 4,000.
4. Ask for the length you need. Five lines that answer cost less than a page that also answers.
5. Keep the start the same. The opening of a session (the instructions, CLAUDE.md, the tools) is cached when it repeats, and a cached read costs about a tenth of the full price. The cache lapses after a few minutes idle, and a changed opening is paid in full again.

## Steps
1. Clear often. When the person starts a task that does not need the earlier conversation, say so and suggest they type /clear first. If something from the old task must carry over, write it to a file (a note, or a line in CLAUDE.md) before the clear, and read that file in the new session.
2. Grep first. To find something in the code, search for the word (a function name, an error message, a label) before opening any file. Note the file and the line number the search returns, for example auth.ts line 88.
3. Read line ranges. Read only the lines around the hit, about 10 before and 10 after (for line 88, lines 80 to 100). Read more only if those lines are not enough, and say why. Read a whole file only when it is short or the task really needs all of it.
4. Skip the essay. When the person asks for a length ("in 5 lines"), answer in exactly that length and stop.
5. Keep the start. Do not switch models or add tools in the middle of a session: either one breaks the cache, and the opening is paid in full again. Edits to CLAUDE.md are read when a new session starts, so make them between tasks, right before a /clear.

## Rules
- Never open a large file to find one thing. Search first.
- Never read a whole file when a range will answer the question, and say when you do.
- A length the person asked for is a limit, not a suggestion.
- Suggest /clear at every change of task; the person types it, not you.
