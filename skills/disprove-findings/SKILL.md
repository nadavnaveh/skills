---
name: disprove-findings
description: Hands an agent's bug list to a fresh agent without the first one's history, has it try to prove each finding is not a bug by opening the code, and reports each one as not a bug, almost certainly fine or still standing, with the evidence. It fixes nothing. Fixes "the agent found bugs, and I started fixing before anyone checked them." Use when an agent or a code review hands you a list of bugs or suspicions, before you fix any of them, and especially before a release. Also on /disprove-findings.
---

# Disprove findings

Your agent found bugs, and you are already fixing them. Some of them may not be real, and the agent that found them cannot tell you, because an agent that grades itself approves what it found. This skill runs the check first: a fresh agent tries to disprove each finding in the code, and you keep only what it could not disprove.

## The principles
1. The finder never grades its own findings. The idea comes from Cloudflare's own account of its harness, where hunters find and a separate agent tries to disprove: "If a Hunter is allowed to grade its own homework, it will confidently validate everything it outputs." (blog.cloudflare.com/build-your-own-vulnerability-harness)
2. Ask it to disprove, not to agree.
3. A finding stands or falls on a line of code someone opened, not on how sure it sounds.
4. Checking comes before fixing. This skill only checks.

## Steps
1. Stop. Fix nothing yet. Write the whole list out and number each finding, with its file and what it claims.
2. Open a fresh agent: a new subagent with its own clean window, or a new session. Give it the numbered list and the project. Do not give it the first agent's reasoning or chat.
3. Tell it: "For each finding, try to prove it is not a bug. Open the code. Quote the file and line that decides it. Change nothing."
4. Give each finding one verdict:
   - **Not a bug**: the quoted line shows the claim is false.
   - **Almost certainly fine**: the code points that way, but something was read and not run or checked. Say what.
   - **Still standing**: it could not be disproved. Give the file and the line.
5. Report every finding with its verdict and its evidence: the file, the line, and one sentence on what that line shows.
6. Keep only the findings still standing, each with its line of code. Stop there. The owner decides what gets fixed.

## Rules
- Fix nothing here, not even a bug that looks obvious.
- A verdict without a quoted line does not count. The finding stays still standing.
- If the code cannot be opened, the finding stays still standing, and the report says why.
- Never claim a rate. Our run was one review with 2 suspicions and 0 left. That is one run, and your list may come back with every finding still standing.
