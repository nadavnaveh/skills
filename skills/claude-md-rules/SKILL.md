---
name: claude-md-rules
description: Writes and trims CLAUDE.md, the file your agent reads at the start of every session. It keeps only specific lines, gives each rule its reason, writes down the exact build, test and lint commands, says what to leave alone, and adds a rule when you correct the agent on the same thing twice. Fixes "I keep telling it the same things every session." Use when you start a project, when CLAUDE.md is missing, long or vague, when the agent ran the wrong command or touched a file it should not have, and whenever you correct the agent on the same thing for the second time. Also on /claude-md-rules.
---

# CLAUDE.md rules

You told the agent to use pnpm yesterday. Today it used npm again.
Every session starts fresh. The only thing it is sure to read is CLAUDE.md, so whatever is not written there is gone.
This skill makes that file short, specific and current, so the agent stops needing the same correction again.

## The principles
1. Keep it short. Every line is read every session. A line earns its place only if the agent would act differently without it. "Write clean code" changes nothing. "Use pnpm, not npm" does.
2. Give the why. A rule with a reason covers cases the rule never named. "No force-push to main" is a rule. "No force-push to main, because others build on it" also tells the agent what to do on any shared branch.
3. Write down its commands. The exact command to build, to test and to lint, so the agent checks its own work the same way you would.
4. Say what is off limits. Name the files and folders to leave alone, so the agent works where it should.
5. Keep it current. Corrected it twice? That is a missing rule. Add it.

## Steps
1. Find the project's CLAUDE.md (in the project's top folder) and read it. If there is none, offer to run /init to make a first draft, or write one with the owner.
2. Keep it short. Go through every line and ask: would the agent do anything differently without it? Mark each line keep, sharpen or cut. Turn vague lines into specific ones ("be careful with the database" becomes "never edit files in migrations/ by hand"). Cut what cannot be made specific.
3. Give the why. Under each rule whose reason is not obvious, add one short reason. If nobody knows the reason, ask the owner. If no one can give one, ask whether the rule still matters.
4. Its commands. Write the exact commands to build, test and lint the project. Run each one and report what happened (for example "npm test: 42 of 42 passed"). Write a command into the file only if it ran. If one fails or you cannot run it, say so and ask the owner for the right one.
5. Off limits. Ask the owner what the agent must leave alone (secret files like .env, generated folders, anything other people own) and list each one with its reason. CLAUDE.md is guidance the agent reads, not a lock. For files that must never be read or changed, also suggest a deny rule in the permission settings (/permissions).
6. Show the new file next to the old one, line by line, and ask "Save these changes?" Write it only after a yes.
7. Keep it current. During any later work, when the owner corrects you on the same thing a second time, stop and propose one line for CLAUDE.md with its reason. Add it after a yes. The owner can also open and edit the file any time with /memory.

## Rules
- No line that would not change what the agent does.
- Every rule that is not obvious carries its reason.
- Never write a command into the file that you did not see run.
- Never put secrets, passwords or keys in CLAUDE.md. Name the file, not its contents.
- Never add, change or remove a rule without the owner's yes.
- One correction is a mistake. The same correction twice is a missing rule.
