---
name: context-rules
description: Shows how the context window fills and keeps it small. It compacts early with a keep list, sends big reads to a subagent, keeps the opening the same so it is cached, and counts the room each tool call takes. Fixes "the session got slow and forgetful, and I don't know why." Use when a session has run long, when the agent forgets an earlier decision, before reading a big file, log or search result, or when tokens run out fast. Also on /context-rules.
---

# Context rules

The session started sharp and turned slow and forgetful. Nothing broke. The window filled up.
Every message and every tool result stays in the window, and the agent carries all of it on every turn.
This skill shows what is in the window and keeps it small enough for the work.

## The principles
1. Every message takes room. The used part of the window only shrinks when it is compacted or cleared.
2. Every tool call takes room too. One file read, search or log can fill more than the whole conversation.
3. Compaction keeps a summary and drops the details. Decide what the summary keeps before it happens.
4. A subagent gets its own clean window. Only its answer comes back into yours.
5. A start that repeats is cached and costs about a tenth. A start that changes pays in full again.

## Steps
1. Before a big step, ask the person to run /context and tell you how full the window is, in percent.
2. Before a tool call that may return a lot, ask if you need all of it. Search first, then read only the lines around the hit.
3. When a job needs many reads but only one answer (search the code, read the logs, run the tests), give it to a subagent. Ask for a short answer that names its sources.
4. Claude Code also compacts on its own near the limit, so do not wait for it. Well before the window is full, write the keep list: the goal, the decisions, the files changed and what is left. Ask the person to run /compact with it, for example "/compact keep the goal, the decisions and the failing test". Then read the summary and add back, in one line, anything it dropped. If the next task is unrelated, ask the person to run /clear.
5. Keep your opening instructions and CLAUDE.md the same during a session. Add new notes in a later message. Changes made now apply to the next session.

## Rules
- Details dropped by compaction do not come back. If one matters, write it down first.
- Never paste a whole file or log when a few lines will do.
- Ask a subagent for the answer, not the transcript.
- When the window is nearly full, compact or clear before you start new work.
