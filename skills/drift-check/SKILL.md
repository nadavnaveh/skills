---
name: drift-check
description: Checks a working agent session for five signs of drift (the same fix twice, edits to files you never named, padding, a lost decision, and "done" before any check), shows the evidence for each one it finds, and steers it back with one move per sign. Fixes "it started well, and somewhere along the way it stopped doing what I asked." Use when a long session starts to feel off, when the same error comes back after a fix, when the agent changes files the task did not name, when answers get longer but say nothing new, when it goes against something you already decided, when it says "done" or "fixed", and before you accept the result of any long session. Also on /drift-check.
---

# Drift check

The session started well and then slowly stopped doing what you asked. Drift is quiet. Each step looks reasonable on its own, and as the conversation grows, the task and your early decisions get buried under newer messages. This skill checks five signs, shows the evidence for each one it finds, and makes one move to steer each one back.

## The principles
1. Drift shows up in the record, not in a feeling. Every sign has something you can point at: an error, a file list, a word count, a decision, a test result.
2. The same fix twice means the plan is wrong. A third patch will not fix it.
3. The task names the files. A change to a file the task did not name is a question for the owner, not an edit to make quietly.
4. Decisions belong in a file, not only in the chat. A choice made early in a long conversation can fade.
5. Done means the checks ran. "Done" with none of the checks run is only a claim.

## Steps
1. Write down three things: the task in one line, the files it names, and the decisions made so far (for example "use Postgres"). If you cannot find one of them, ask the owner.
2. **Same fix twice.** Look at the errors in this session. If the same error came back after a fix, stop patching. Say how many times it came back. Then go back to the cause: read the code around it, write what you think is causing it, and agree a new plan with the owner before the next change. Plan mode (Shift+Tab) helps here.
3. **Off task.** Run `git status` and `git diff --stat` to list every changed file. Mark each one as named by the task, needed by the task, or neither. For each file marked neither, show what changed and ask the owner to keep it or undo it.
4. **Padding.** Compare your last few answers. If each one got longer without adding a new fact, decision or result, say so with the word counts, rewrite the latest answer as the point alone, and keep answers that short from now on.
5. **Lost decisions.** Check recent work against each decision from step 1. If anything goes against one (the decision says Postgres, the new code says MySQL), show both, and fix it after the owner says yes. Then offer to write the decisions into the project's CLAUDE.md (the owner can open it with /memory), so they are still there after /compact or /clear.
6. **Says done.** If you said, or are about to say, "done", "fixed" or "works", list the checks and how many of them ran. If none ran, run them now and report each one as pass or fail with the evidence, or as not run with the reason.
7. Report one line per sign: clear, or found, with the evidence and the move you made. If three or more signs are found, suggest a fresh start: write the task, the decisions and what is left into a short note, then /clear and continue from the note.

## Rules
- Every sign you report comes with its evidence: the repeated error, the file, the word counts, the decision and the line that broke it, the number of checks run.
- Undo, revert or delete nothing without the owner's yes.
- Never change a decision quietly. Changing it is the owner's call, and the new one gets written down.
- No "done" when zero checks have run.
