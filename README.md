# Skills for running AI like a company

You use AI. I run it like a company.

These are the skills I use to manage the agents that run my work. Each one is small, and each one fixes a failure you have probably already had. They work the same whether you write code or not.

**Install in one line** (Claude Code, Codex, Cursor, Gemini CLI and most other agents):

```bash
npx skills@latest add nadavnaveh/skills -g -y
```

Or just tell your agent: *"Install the skills from github.com/nadavnaveh/skills."* Then type `/to-gantt`, `/what-do-i-want`, `/done-test` or `/agent-patterns`.

## The failures, and the skill for each

### "It did exactly what I asked, and it's not what I wanted."

You said "make it better". The agent picked a meaning and ran. The problem started before the agent: the want was a feeling with a direction, and nobody wrote down where it ends.

**[`/what-do-i-want`](./skills/what-do-i-want/SKILL.md)** reads your want, shows you the two or three ways it could be read, asks the few questions that change the result, and writes one statement with a done-test. The work starts only after your yes. [Docs and a real example](./docs/skills/what-do-i-want.md).

### "The answer looks reasonable, but it misses my world."

The agent was not weak. It was never in the room. Your goal, your audience, what you tried last month and the words your team uses were all in your head.

**`/into-the-room`** (draft, coming next) checks what is in your head and not in the agent's context before you hand off.

### "The agent said it was done, and it wasn't."

"Done" meant "I stopped working", not "it works". Nobody said what works means, so the agent picked a finish line it could reach.

**[`/done-test`](./skills/done-test/SKILL.md)** writes one to three yes/no checks before the work starts, then runs each one at the end and reports pass, fail or not run, with the evidence. No "done" without them. [Docs and a real example](./docs/skills/done-test.md).

### "I run several agents, and they wait on each other or redo each other's work."

More agents do not make you faster until you can see what depends on what. The number of agents is an output of the plan, not the start of it.

**[`/to-gantt`](./skills/to-gantt/SKILL.md)** takes whatever you have (a goal, a list of tasks, notes, a document) and turns it into tickets, marks what each one needs from the others, and draws a Gantt chart: the critical path, what can run in parallel right now, and what waits on whom.

### "I opened five agents and got five messes."

The job's shape decides how agents should work together: side by side, arguing, checking each other, in a chain, or under a manager.

**[`/agent-patterns`](./skills/agent-patterns/SKILL.md)** reads the shape of your task, picks one of five patterns (Parallel, Debate, Pair, Pipeline, Manager), says why, and runs it with subagents: one owner per file, every result checked before it counts.

### "It says it's done. Is it good?"

If you did not decide what good means before the work, you will decide it afterwards, by feel, and argue with the agent about it.

**`/define-good`** (draft) writes the success test first, for code and for everything that is not code.

### "I gave it one big job and it came back a mess."

A big ask needs to be split by what depends on what, so each step knows what it receives and what it hands on.

**`/break-by-dependency`** (draft) does the split.

### "It ran for two hours and failed quietly." / "I keep correcting the same thing."

You either watch every step or find out too late. A failure once is a retry. The same failure twice means the plan is wrong, not the output.

**`/when-to-step-in`** (draft) sets the checkpoints where you come back in.

### "I keep telling it the same things every session."

Every session starts fresh, and the only thing the agent is sure to read is CLAUDE.md. If the file is vague, too long or out of date, your corrections are gone by the next morning.

**[`/claude-md-rules`](./skills/claude-md-rules/SKILL.md)** trims your CLAUDE.md to specific lines, gives each rule its reason, writes down the build, test and lint commands it has seen run, names what to leave alone, and adds a rule whenever you correct the agent on the same thing twice.

### "It started well, and somewhere along the way it stopped doing what I asked."

Long sessions drift a little at a time: the same bug comes back, files you never named get edited, answers grow without saying more, and early decisions fade. Each step looks reasonable on its own, so nobody notices until the agent says "done" and nothing was checked.

**[`/drift-check`](./skills/drift-check/SKILL.md)** checks a session for the five signs of drift (same fix twice, off task, padding, lost decisions, says done), shows the evidence for each one it finds, and steers it back with one move per sign.

### "It started changing things before I knew what it was going to do."

The agent began editing before anyone agreed on the goal, the files it would touch or the step that cannot be undone. By the time you saw the change, it had spread across the project, or something was already gone.

**[`/plan-first`](./skills/plan-first/SKILL.md)** checks whether the task needs a plan, maps the code, agrees the goal, numbers every file, marks the risky steps for your yes, and takes a big refactor one approved step at a time.

### "A web page told my agent what to do, and it did it."

The agent reads pages, emails and files as text, and a hidden line in that text can look just like an order. If the agent can reach your keys, run any command and send without asking, that one line is enough.

**[`/injection-guards`](./skills/injection-guards/SKILL.md)** sets five guards: it reads pages as data and not as orders, cannot see your keys, runs only the commands you named, asks before it emails, posts or pays, and works inside a sandbox, then it tests each guard and shows you the result.

### "My tokens run out, and the session gets slower the longer I work."

Every message sends the whole conversation again: each file read, each long answer and each old task. So what you add once keeps costing on every turn after it.

**[`/token-savers`](./skills/token-savers/SKILL.md)** keeps the session small with five habits: clear between tasks, search before reading, read only the lines around the hit, ask for the length you need, and keep the opening the same so it is cached.

### "I typed one line and got a generic answer back."

The agent filled every gap in that line with a guess: who reads it, what shape it takes, what actually broke. Strong users close those gaps before the agent starts.

**[`/prompt-upgrades`](./skills/prompt-upgrades/SKILL.md)** upgrades your request with five habits: talk instead of typing, let the agent ask who it is for, pick one of three options, give the shape of the answer, and paste the real source instead of your summary.

### "My session filled up with files and logs, and the agent lost the thread."

Everything the agent reads stays in its window and is sent again on every turn. Search results, long logs and test output crowd out the task itself.

**[`/subagent-jobs`](./skills/subagent-jobs/SKILL.md)** sends five reading jobs (search code, read long logs, run the tests, review with fresh eyes, research) to a subagent with its own clean window, and takes back only a short summary that points to its sources.

### "It sounded right, I used it, and it was wrong."

The agent sounds just as sure when it guessed as when it checked, so asking "are you sure?" only gets a yes. An answer agreeing with itself is not proof, and only a check from outside the conversation can catch the error.

**[`/answer-checks`](./skills/answer-checks/SKILL.md)** checks an answer before you use it in five ways: it opens the source, makes the agent argue against itself, asks a fresh session that never saw the answer, runs the method on a case with a known result, and sets how hard to check by what an error would cost.

### "I changed the prompt, and I can't tell if it got better or worse."

You tried the change on one task and judged it by feel. One good answer can hide the two tasks it broke.

**[`/build-an-eval`](./skills/build-an-eval/SKILL.md)** turns ten of your real past tasks into an `evals/` folder, writes the right answer for each one before any run, and scores the agent pass or fail out of ten on every change, so a drop shows before you ship it.

### "The agent found ten bugs, and most of them were not real."

A finding reads like a fact, so it gets fixed like one, even when nobody made it happen. Some are guesses, some are expected behavior, and several are one bug reported three times.

**[`/bug-triage`](./skills/bug-triage/SKILL.md)** reproduces every finding, has a second agent try to disprove it, merges the ones with one cause, writes what a user sees when it breaks, and fixes each real bug only after a test for it fails first.

### "I keep correcting the same thing."

Each correction patches one output, so the cause stays where it was: a rule nobody wrote down, or a step in the plan that was wrong or too big. A third fix to the output won't land either.

**[`/corrected-twice`](./skills/corrected-twice/SKILL.md)** stops at the second correction, writes it as a rule in CLAUDE.md, finds the step in the plan that went wrong, redoes it on one file with a check, and starts a fresh session with the new rule loaded.

### "I changed one small thing in old code, and something far away broke."

Nobody knew what called that code, where its data went or that it had no tests. The agent changed it the way you would change new code, blind.

**[`/code-map`](./skills/code-map/SKILL.md)** maps the code before anyone touches it: where every request starts, where the data goes hop by hop, who calls the function you want to change, which parts are risky and what is tested, then asks for your yes before any edit.

### "I left the agent running, and I couldn't tell from my phone what it was doing or stop it from changing things."

On a small screen you cannot review a diff or watch every step, so the agent either waits on a question you cannot read or changes things you never saw. The rules for what it may do alone have to be set before you leave the desk.

**[`/phone-rules`](./skills/phone-rules/SKILL.md)** sets five rules for the road: reads run without asking, every change waits for your tap, reports come in three lines you can read while walking, a notification arrives when the job ends, and deploy is refused until you are back at your desk.

### "The report said nothing new, and it never read the source."

A blocked page and a quiet day look the same in a summary. The agent writes about what it got and says nothing about what it did not get.

**[`/report-endings`](./skills/report-endings/SKILL.md)** makes every report list what it read, name each source that failed and why, show only what changed since the last run, list what it skipped and why, and put the one decision that needs you at the top.

### "The agent made the change and never checked if it worked."

Every agent runs the same loop: plan, act, observe, check, then stop or go again. The edit went through, so the agent felt done and skipped the check, which is the one step that shows whether it worked.

**[`/agent-loop`](./skills/agent-loop/SKILL.md)** runs every task as plan, act, observe, check, and then stop or go another round, makes one change per round, and stops only on a check that passed, or after three rounds it hands back to you.

### "I gave it a thousand pages, and it skimmed the start and guessed the rest."

One agent cannot hold that much at once, so the late pages get less attention and the findings lose their source. A list without page numbers cannot be checked, so you either trust it or read it all again yourself.

**[`/big-archive`](./skills/big-archive/SKILL.md)** splits the archive into numbered parts, reads them in parallel with one subagent per part, makes every finding cite its page, merges the lists so duplicates are gone, and opens two cited pages at random to check the citations hold.

### "The answer was close, and I still had to fix it myself."

The request left out the shape you wanted, who reads it and how to tell it works, so the agent guessed. It also sounds just as sure about what it never checked.

**[`/prompt-ways`](./skills/prompt-ways/SKILL.md)** adds five small habits to every request: one good example, who it is for, a plan before it starts, a check it can run, and a list of what it could not confirm.

### "I trusted the agent's work, and it broke the first time someone used it."

The agent that did the work checks what it meant to build, not what it built, so its "it works" sounds the same whether it checked or not. Only a check from outside the agent's own word can catch the break before a user does.

**[`/check-ways`](./skills/check-ways/SKILL.md)** checks the work in five ways before you trust it: it runs the tests, has a second agent review the diff, sets a gate that refuses the commit while tests fail, reads every changed line, and clicks through it the way a user would.

### "The agent went wrong, and I only noticed at the end."

Agents fail in five known ways: they drift off the goal, sound sure when they are wrong, loop on the same fix, forget what you decided and touch what they were not allowed to touch. Each step looks reasonable on its own, so nobody catches the failure until the damage is done.

**[`/agent-failures`](./skills/agent-failures/SKILL.md)** writes down the goal, the allowed files, your decisions and the check before the work starts, then watches for each of the five failures at the step where it begins and reports each one as caught or clear, with the evidence.

### "The agent made a call that should have been mine."

Nobody wrote down where the agent must stop, so it treated a delete, a merge, a payment and a release like any other step. By the time you saw it, the files were gone, main had changed or the money was spent.

**[`/calls-to-keep`](./skills/calls-to-keep/SKILL.md)** keeps five calls with you: you write what done means, nothing that cannot be undone runs before a backup and your yes, work merges into main only on your word, spending and keys wait for you, and you look at the release before it ships.

### "The safety check broke, and the agent went ahead anyway."

A guard that crashes, a test run that finds no tests and a question nobody answered all make no noise. The agent reads that silence as a yes and carries on.

**[`/fail-closed`](./skills/fail-closed/SKILL.md)** makes every guard lock the door when it fails: a crashed hook blocks the action, zero tests run is not a pass, no answer means nothing ships, a command not on the list is refused, and a missing key stops the work until you answer.

Drafts live in [`skills/in-progress/`](./skills/in-progress/). They are not installed by the plugin until they are ready.

## Where these come from

Each skill is one practice I use every day to run my work with AI agents. Each skill states the principles behind it, so you can see the reasoning and disagree with it.

## Install

Pick one way. Installing two ways gives you every skill twice.

### Any agent: `npx skills` (recommended)

```bash
npx skills@latest add nadavnaveh/skills -g -y                 # all skills, every agent it finds
npx skills@latest add nadavnaveh/skills -s to-gantt -g -y     # one skill
```

**Updates:** `npx skills@latest update -g -y` pulls the newest versions. No git.

### Claude Code plugin

```
/plugin marketplace add nadavnaveh/skills
/plugin install nadavnaveh-skills@nadavnaveh
```

**Updates:** in `/plugin`, open Marketplaces → `nadavnaveh` and turn on auto-update, so new skills and fixes arrive by themselves. Or run `/plugin marketplace update nadavnaveh`.

Then type `/to-gantt` followed by your list, or `/what-do-i-want` followed by what you want, or just ask and let the agent reach for the right skill.

## Credits

- Built on the [Agent Skills](https://code.claude.com/docs/en/skills) format and the Claude Code plugin format.

## License

[MIT](./LICENSE). Use them, change them, make them yours.
