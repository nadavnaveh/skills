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
