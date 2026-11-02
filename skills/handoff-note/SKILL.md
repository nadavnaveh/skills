---
name: handoff-note
description: Writes a four-part handoff note before a session closes, checks each claim against the code and the repo, marks the rest as guesses, then tests the note on a fresh agent. Fixes "The session ended, and everything it understood was gone." Use before you close a session or run /clear, when you stop in the middle of a task, or when another person or agent takes over. Also on /handoff-note.
---

# Handoff note

The session ends and everything it understood is gone. The files stay, but the reasons, the half-done work and the traps lived in the conversation. This is the skill that writes that note, so tomorrow's agent, with no memory, can continue.

## The principles
1. A note is ready when a stranger can use it, not when it reads well.
2. Check first, then write. A claim nobody checked is a guess, and the note says so.
3. An owner decision gets handed over. It does not get made.

## Steps
1. Before closing, draft HANDOFF.md in the project folder with exactly four headings:
   - **Where the code stands**
   - **What was decided and why**
   - **What is half done**
   - **What is dangerous to touch**
2. Check each claim against the code and the repo. Look up the branch, the last commit, any uncommitted changes and whether a remote exists. Run what the note says runs, and open the file behind each claim about code.
3. Correct whatever the check proved wrong. Mark anything you could not check as "guess".
4. Put any owner decision that changes money or customers under "dangerous to touch": what you found, the choice to make and who makes it. Do not act on it, even if the fix looks small.
5. From your checks, write down the right answer to each of the four things. Do this before any fresh agent runs, so the comparison is not made after the fact.
6. Paste the note's text into the prompt of a new subagent or session, one with no memory of this session. Tell it to open nothing else, and ask it the four things.
7. Compare each answer with what you wrote down. If one is wrong, or the agent says the note does not cover it, the note isn't ready: fix it and ask a fresh agent again. Report the four answers, and close only when all four are right.

## Rules
- Four headings, no others. Keep only what tomorrow's agent needs.
- Every claim is either checked or marked "guess". There is no third kind.
- Our run: one small repo, one run, four of four. The check caught the agent's own wrong push offer.
- One run, not a rate. It does not prove time saved or that this works on a long real session.
