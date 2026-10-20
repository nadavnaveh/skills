---
name: hooks-to-add
description: Adds five Claude Code hooks, small commands that run by themselves at the right moment. They run the tests after each edit, block risky commands before they run, format every file the agent writes, ping you when the agent needs you, and log every command it runs. Then it tests each one. Fixes "I keep telling it to run the tests, and it keeps forgetting." Use when you repeat the same reminder every session, when the agent ran a command you did not want, when edits leave messy code or broken tests, when you step away and miss its questions, or when you cannot tell what it ran. Also on /hooks-to-add.
---

# Hooks to add

You asked the agent to run the tests after every edit. It did for a while, and then it forgot. A line in CLAUDE.md is a request the agent can skip, but a hook is a command Claude Code runs by itself at a set moment, every time. This skill adds five hooks, fires each one, and shows you the result.

## The principles
1. If it must happen every time, make it a hook, not a reminder.
2. Each hook does one small job at one moment: before a command, after an edit, or when the agent is waiting for you.
3. A hook you have not seen fire is not set up yet.

## Steps
1. Find the project's test command and formatter. Hooks go in `.claude/settings.json` for this project, or in `~/.claude/settings.json` for every project. Show the owner each hook you plan to add, with its exact command, and ask "Add these hooks?" Start only after a yes.
2. **Run the tests.** Add a `PostToolUse` hook with the matcher `Edit|Write` that runs the test command. If the full suite is slow, run only the fast tests.
3. **Block danger.** Add a `PreToolUse` hook with the matcher `Bash`. It reads the command and exits with code 2 if the command is on a list you agree with the owner, such as `rm -rf`, `git push --force` or dropping a database. Exit code 2 stops the command and tells the agent why.
4. **Format on save.** Add a `PostToolUse` hook with the matcher `Edit|Write` that runs the project's formatter, such as Prettier or Black, on the file that was just written.
5. **Notify me.** Add a `Notification` hook that sends a ping when the agent needs your permission or is waiting for you. On a Mac this can be `osascript`, and on Linux it can be `notify-send`.
6. **Log what it ran.** Add a `PreToolUse` hook with the matcher `Bash` that adds each command and its time to `commands.log`, one line per command.
7. Fire each hook once on purpose: make a small edit, try a blocked command, wait for a ping, and read the log. Report each hook as **working**, with what you saw, or **not working**, with what happened instead. Then show the owner the list with `/hooks`.

## Rules
- Hooks run on your machine with your permissions. Show the owner every command before you add it.
- A hook gets the file path or the command as JSON on its input. Read it from there and do not guess.
- Only exit code 2 blocks. If the block hook crashes, the command still runs, so test it with a command that should be blocked.
- Keep every hook fast. A slow hook slows down every edit.
