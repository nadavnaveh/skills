---
name: compact-safely
description: Saves your decisions and exact numbers to a file before /compact, tells /compact what to keep, then reloads the rules and asks about the goal before the work goes on. Fixes "I compacted, and it forgot what we decided." Use when a session is long and you are about to run /compact, when Claude Code warns that the context is nearly full, right after any compaction (by hand or automatic), or when the agent starts getting early details wrong. Also on /compact-safely.
---

# Compact safely

You compacted the session, and the agent came back sure of itself and wrong on the details. Compaction replaces the whole conversation with a summary, and a summary keeps the gist only: $39.90 becomes "about $40", and early decisions and rules fade. This skill saves what matters to a file first, tells the compact what to keep, and checks the result before any work goes on.

## The principles
1. A summary keeps the gist only. Exact numbers, names and small decisions are what it drops first.
2. The file survives; the chat doesn't. Anything that must last goes in a file.
3. Don't trust a compacted session until it passes a check. One question about the goal is enough.

## Steps
1. Keep a file called decisions.md in the project. Whenever something is decided, add one line: the decision and why. Don't wait for the compact.
2. Before you compact, find every exact value the work depends on (prices, dates, versions, IDs, file names) and copy it into decisions.md exactly as written.
3. Compact with a focus line that names what must be kept, for example: `/compact keep the API notes and the open bugs`. Without one, the summary decides for you.
4. After compacting, have the agent read CLAUDE.md again, then decisions.md. The rules and decisions then come from the files, not from the summary.
5. Paste the exact numbers back from decisions.md. Look for any value the summary rounded or changed ("~$40" where it should say "$39.90") and correct it.
6. Ask one question: "What's the goal?" Compare the answer with decisions.md. If it matches ("v2 by Friday"), say so and go on. If it doesn't, correct it and ask again before any work.

## Rules
- Never compact before decisions.md is saved.
- Take a number from the file, never from the summary.
- No work starts after a compact until the goal answer matches the file.
- decisions.md holds decisions and exact values, one line each, not a copy of the chat.
