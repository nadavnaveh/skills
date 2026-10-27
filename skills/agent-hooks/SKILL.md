---
name: agent-hooks
description: Moves one rule the agent keeps breaking from AGENTS.md or CLAUDE.md into a git pre-commit hook that checks the staged diff, refuses the commit and prints the exact fix in words. Fixes "I wrote the rule in AGENTS.md, and the agent keeps breaking it." Use when the agent breaks the same written rule twice, or when a rule must hold on every commit. Also on /agent-hooks.
---

# Agent hooks

You wrote the rule in AGENTS.md, and the agent broke it anyway. A rule in that file is a request, and the agent can skip it. A pre-commit hook runs on every commit, so this skill moves one rule there.

## The principles
1. A rule in CLAUDE.md (or AGENTS.md, if you use it) is a request, and Claude Code reads it at the start. A check that fails the commit is a gate, whichever file holds the rule.
2. One rule per check, starting with the one broken most.
3. The refusal tells the agent what is wrong and the exact fix in words.
4. A gate stops the bad change. It does not make the agent fix it.

## Steps
1. Pick the one rule the agent keeps breaking. Write it in one line with what to do instead: "never call print() directly, use log() from diag.py".
2. Write a check that finds it in the staged diff (`git diff --cached`). A simple grep is enough. Start from scripts/pre-commit.fixed, which refuses any added .py line that calls print(). Change its file glob, its pattern and both message lines together, so the message still matches the rule. A grep also matches comments, strings and method calls such as logger.print(, so test one line it should allow as well as one it should refuse.
3. On a match, the hook prints two lines and runs `exit 1`, so the commit fails. The first line says what was refused and why. The second gives the fix and ends with "commit again".
4. Show the person the hook and ask "Install it like this?" After a yes, copy it to .git/hooks/pre-commit and `chmod +x` it. To share it, commit it as hooks/pre-commit and run `git config core.hooksPath hooks`.
5. Test it both ways. Stage a line that breaks the rule and commit: it must fail and print the message. Fix the line, stage it and run the hook directly: exit 0, no output. Git will not run a hook that is not executable, so this checks that too. Show both outputs, then undo the test change.
6. When the hook refuses a commit, quote its message to the person, leave the change staged, and ask before applying the fix. That is what the agent did in every refused run we tested.

## Rules
- Never use `git commit --no-verify` or edit the hook to get past it. Only the person may skip it. Either one opens the gate, so it is only as strong as the person's control of it.
- Our proof is small: 6 runs (Claude Code 2.1.311, haiku and sonnet). The hook refused all 3 changes that broke the rule, one of them a print() we asked for on purpose. The agent never fixed the code by itself; it quoted the fix and asked. Do not promise more.
- "Ten out of ten" is Geoffrey Huntley's result, as quoted by Simon Willison. Nobody else measured it.
