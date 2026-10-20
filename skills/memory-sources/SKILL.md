---
name: memory-sources
description: Sets up the five places an agent reads before it starts (the CLAUDE.md rules file, decision notes, ticket history, a progress file and a folder of good examples) and makes it read them first. Fixes "every new session starts from zero, and it tries what we already ruled out." Use at the start of a project, when a task will run over more than one session, when the agent repeats a fix that already failed or undoes a choice you made, or when its work does not match your style. Also on /memory-sources.
---

# Memory sources

Every new session starts from zero, and it tries what you already ruled out. The agent is not forgetful. It only knows what is written where it looks. This skill sets up five sources the agent reads before it starts, and makes sure it reads them.

## The principles
1. If it is not written down, the next session does not know it.
2. CLAUDE.md is loaded at the start of every session, so it points to the rest.
3. Write the reason, not just the choice. A choice without its reason gets undone.
4. Show what great looks like. One good example beats a page of style rules.

## Steps
1. **A rules file.** Check which sources the project has: CLAUDE.md, DECISIONS.md, ticket history, PROGRESS.md and an examples/ folder. List what is missing. Keep CLAUDE.md short and specific, and for each other source say which file to read and when. A line with just @DECISIONS.md loads that file into every session. A plain line such as "Before you change how data is saved, read DECISIONS.md" works only if the agent follows it.
2. **Decision notes.** For each choice the work depends on, add one entry to DECISIONS.md: the date, what was chosen, why, and what was turned down. If you do not know the reason, ask the owner. Never guess one.
3. **Ticket history.** Before you work on a ticket, read it and every comment on it. Use the ticket tool you have (gh issue view, a Trello or Jira connection) or ask the owner to paste it. List what was already tried and how it failed, and make the next try different. When you finish, add what you tried and what happened.
4. **A progress file.** On any task with steps, keep PROGRESS.md: the numbered steps, which are done, which is next, and anything left half done. Update it after every step. A new session reads it first and starts at the next step, not at step 1.
5. **Good examples.** Ask the owner for two or three pieces of work they call great, and put them in examples/. Before you write, read them and match their style, length and shape. Say which example you followed.
6. Show the owner what you added or changed in each source and ask "Is anything here wrong?" Then offer to commit the files with git, so every session and every agent reads the same ones.

## Rules
- Never write a decision, a reason or an example the owner did not give or approve.
- If a source says one thing and the request says another, ask. Do not pick one quietly.
- Keep each file short.
