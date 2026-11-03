---
name: stack-compare
description: Runs one small real task three times on each of two options with claude -p, records tokens, turns and cost, builds every result, and prints the median and spread per option. Fixes "My stack choice doubled the tokens, and I never measured it." Use when choosing between two stacks or kits, before switching stacks or when someone quotes one run's tokens. Also on /stack-compare.
---

# Stack compare

The same task can cost an agent twice the tokens in one stack as in another. One run looks like an answer, but the next can land far away. This skill runs three per option and builds every result.

## The principles
1. One run is luck. Run three per option and compare medians.
2. A cheap run that does not work saves nothing.
3. Only the option changes: same task, model and tools every run.
4. One small task does not predict a big one.

## Steps
1. Ask for one small real task as one prompt, the two options (two kits, two folders or two branches), the install command, the build or test command, and one model and tool set for all runs. CLAUDE.md files load in every run, so they affect both options equally. Repeat it back and start after a yes.
2. Make six throwaway copies, one per run, outside the project: copy the folder, or `git worktree add` a branch, then copy in any uncommitted or untracked files the task needs. Run the install command in each copy. Never touch the user's working tree. List every copy.
3. In each copy, run `claude -p "<task>" --output-format json --model <model> --allowedTools "Read,Edit,Write"`. Headless runs cannot ask permission, so unlisted tools are refused. Record `num_turns`, the usage tokens (input, output, cache read, cache creation) and `total_cost_usd`.
4. Run the build or test command in each copy: works or fails, with the exit code. A build shows it compiles, not that it behaves right, so add a yes/no behavior check where the user names one.
5. Print one table per option: median and spread (lowest to highest) of tokens, turns and cost, and runs that worked.
6. Under the tables, say plainly that one run is luck (if the ranges overlap, treat it as no clear gap and add runs), that cost in money can move less than tokens because cache reads are cheap, and that one small task does not predict a big one.

Our run, as an example (Haiku, fresh Vite templates, one todo prompt): React median 176K tokens and 6 turns, plain JavaScript 330K and 9 turns, all 6 runs built. Median cost moved less, $0.012 against $0.0157. A one-button task showed no gap.

## Rules
- Never pick a winner from one run.
- A run that fails the build, errors or stops early is reported with the reason, never dropped.
- Ask before cleanup, then remove only the copies from step 2 (`git worktree remove` for worktrees). Delete nothing else.
