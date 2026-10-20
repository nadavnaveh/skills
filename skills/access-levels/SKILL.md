---
name: access-levels
description: Sets how much the agent may do on its own across five levels (read only, sandbox edits, ask first, safe auto-run, production), starts at the lowest level that can do the job, and moves up one level only when the owner says so. Fixes "I gave the agent full access on day one, and it changed things I never agreed to." Use when you start working with a new agent or a new project, before you let it edit, run commands or deploy, when you are about to turn off permission prompts, and whenever it touches something that ships to users. Also on /access-levels.
---

# Access levels

The agent got full access on day one and changed things nobody agreed to. That happens because nothing earned the access first. This skill gives the agent access in five levels, so it gets more as it earns your trust.

## The principles
1. Start at the lowest level that can do the job.
2. Move up one level at a time, and only on the owner's word.
3. A mistake moves the agent down a level, not just the output back.
4. Every release is signed off by a person, at every level.

## Steps
1. Write the task in one sentence and what it needs to touch: files, commands, the live product. Pick the lowest level that covers it, say which level and why, and ask "Start at this level?"
2. **Read only.** The agent looks and suggests. It makes no edits. Use plan mode (Shift+Tab) so it can read files but cannot change them, and it ends with a written suggestion.
3. **Sandbox edits.** Changes stay in a safe copy. Make a new git branch or worktree (`git worktree add ../sandbox -b sandbox`) and let the agent edit only there. Main stays clean. You read the diff before anything merges.
4. **Ask first.** Every command waits for you. Keep the normal permission mode, so each edit and each command stops and asks for your yes. Never answer "yes, and don't ask again" for a command you have not read.
5. **Safe auto-run.** Safe ones run on their own, and the rest ask. Write a short list in `.claude/settings.json`: commands that only read or test (run the tests, the linter, `git status`, `git diff`) go under allow. Push, delete and deploy go under ask. Show the list and start only after a yes.
6. **Production.** A person signs every release. The agent prepares it: the version number, the notes and the check results. Deploy and publish commands go under deny. The release comes to you, and you ship it or say no.
7. Write the current level and the reason in CLAUDE.md. Move up only when the owner says so. After a mistake, move down one level and note what went wrong.

## Rules
- If you are not sure which level a task needs, use the lower one.
- A command that is not on the allow list asks. It never runs on its own.
- The agent never raises its own level or edits its own permission list.
- No level lets the agent deploy, publish or release without a person's yes.
