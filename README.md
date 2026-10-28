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

### "The session got slow and forgetful, and I don't know why."

Every message and every tool result stays in the window, and the agent carries all of it on every turn. When the window fills, compaction keeps a short summary and the details you did not save are gone.

**[`/context-rules`](./skills/context-rules/SKILL.md)** keeps the window small with five rules: every message takes room, every tool call takes room, compact early with a keep list, send big reads to a subagent with its own clean window, and keep the opening the same so it is cached.

### "I gave the agent full access on day one, and it changed things I never agreed to."

Trust usually grows a step at a time, but the agent was given every permission before it had earned any of them. So the first time it got something wrong, the mistake went straight into your files, and then into what you ship.

**[`/access-levels`](./skills/access-levels/SKILL.md)** gives the agent access in five levels (read only, sandbox edits, ask first, safe auto-run and production). It starts at the lowest level that does the job, moves up one level only on your word, and leaves every release for a person to sign off.

### "I explained the task five times before the agent got it right."

The goal, the finish line, what to leave alone, where the work lives and how to check it were all in your head, so the agent asked or guessed. Each question costs a round, and each guess costs a fix.

**[`/brief-parts`](./skills/brief-parts/SKILL.md)** writes the brief once, before the work starts, in five parts: a one-line goal the agent repeats back, what done looks like, what must not change, the key files, and the test that proves it works.

### "I keep telling it to run the tests, and it keeps forgetting."

A rule in CLAUDE.md is a request, and late in a long session the agent can skip it. Anything that must happen every time needs to run without the agent having to remember it.

**[`/hooks-to-add`](./skills/hooks-to-add/SKILL.md)** adds five hooks that run on their own and tests each one: they run the tests after each edit, block risky commands, format every file the agent writes, ping you when it needs you, and log every command it runs.

### "It said the code was done, and nothing had been tested."

The agent read its own change, saw that it looked right, and stopped there. But reading code is not running it, and each kind of break only shows up under its own test.

**[`/tests-to-run`](./skills/tests-to-run/SKILL.md)** runs five tests before anyone says done (unit tests, a type check, lint, one real user flow clicked through like a person, and a test for every fixed bug) and reports each one as pass, fail or not run, with the output.

### "The agent changed main, and I never saw what went in."

The agent went straight from the prompt to the code, with no plan, no branch, no tests and no second look. By the time you saw the change it was already in main, and nobody had said yes to it.

**[`/ship-steps`](./skills/ship-steps/SKILL.md)** takes every change from a prompt to a safe merge in five steps: it agrees the plan, builds in a branch so main stays clean, runs the tests before review, puts the diff in front of you for a second look, and merges only after you say yes.

### "I explain the same thing to every agent, and each one does it its own way."

How your team tests, ships, names things, reviews and writes tickets lives in your head or an old chat. Every new session starts without it, so each agent guesses, and each one guesses differently.

**[`/write-skills`](./skills/write-skills/SKILL.md)** writes each job down once as its own skill (how we test, how we deploy, our code style, how to review, writing a ticket) from what your team really does, tests it in a fresh session, and commits it so every agent follows the same steps.

### "My key ended up somewhere I never meant to send it."

Data slips out through everyday steps: a log line, a screenshot, a tool call, a page the agent obeyed, a commit. Each step looks harmless, and whoever got what was printed, shown, sent or pushed keeps it.

**[`/data-leaks`](./skills/data-leaks/SKILL.md)** checks the five places data leaks (logs, screen captures, prompts to tools, pages it reads and commits), closes each one, and reports each as closed, open or not checked.

### "I automated it, and now I spend more time fixing it than doing it."

The task did not come back often enough to be worth it, nobody could check a run, and the inputs had bad rows in them. When it broke, no alert went out and nobody owned it, so the mistakes piled up quietly.

**[`/automate-questions`](./skills/automate-questions/SKILL.md)** asks five questions before anything is automated (does it repeat, can you check it, what if it fails, who owns it, is the data ready) and builds the job only when every one has an answer.

### "I approved the agent's code after a quick look, and it broke later."

Agent code looks clean and sure of itself, so it gets skimmed instead of read. A big change makes that worse, and the break was waiting at an odd input or in the part no test covered.

**[`/review-habits`](./skills/review-habits/SKILL.md)** reviews agent code with five habits: it keeps the change small, reads every line of the diff, runs it on your machine, tries empty, huge and odd inputs, and lists what no test covers, then reports each one as pass, fail or not run, with the evidence.

### "I connected my tools to the agent, and I don't know what it can reach or what it did with them."

An MCP server hands the agent its whole list of tools at once, and nobody chose which ones it may use. Then the calls and their answers pass by unseen, so a delete looks just like a search.

**[`/mcp-parts`](./skills/mcp-parts/SKILL.md)** walks the five parts of MCP: it lists every tool a server exposes, shows each call and the answer that came back, sets allow, ask or deny for each tool, and adds one shared server that all your agents use.

### "I let it keep going, and it kept getting worse."

Each step looked like progress, so nobody stopped to ask if the plan still held. The signals were there the whole time: the same error back again, a jump in cost, files nobody named, a plan nobody could restate and no test in half an hour.

**[`/stop-signals`](./skills/stop-signals/SKILL.md)** watches for five signals to stop (same error twice, cost jumps, unasked edits, a plan that drifted, no test in 30 minutes), pauses at the first one with the evidence, and re-plans with you before the work goes on.

### "One agent planned it, built it, tested it and approved it, and nobody caught the mistake."

When one agent plays every role, it checks the work against what it meant to build, not against what it actually built. Nobody else looks, so its mistakes go straight into main.

**[`/team-roles`](./skills/team-roles/SKILL.md)** gives each role one job: the planner breaks the goal into numbered steps, the builder writes one step at a time on a branch, the tester runs the tests and flags what fails, a fresh reviewer reads the diff, and the merge waits for your yes.

### "Every new session starts from zero, and it tries what we already ruled out."

The agent only knows what is written where it looks. Your reasons, what was already tried, where the last run stopped and what good looks like were all in your head or an old chat.

**[`/memory-sources`](./skills/memory-sources/SKILL.md)** sets up five sources the agent reads before it starts (a CLAUDE.md that points to the rest, decision notes with their reasons, ticket history of what was tried, a progress file of where the last run stopped, and a folder of good examples) and makes it read them first.

### "The new agent started over, redid finished work and trusted a test nobody ran."

The first agent knew what was done, what was left and what was never tested, but it was all in a session that ended. The next agent read the silence as done and began again.

**[`/handoff-rules`](./skills/handoff-rules/SKILL.md)** writes one HANDOFF.md when an agent stops (what was done, what is open, what was tested and how, and who holds the task now), and the next agent reads it and checks it against git before it acts.

### "I compacted the session, and it forgot what we decided."

Compaction replaces the whole conversation with a summary, and a summary keeps the gist only. Exact numbers get rounded, early decisions fade, and the rules you set at the start lose their hold.

**[`/compact-safely`](./skills/compact-safely/SKILL.md)** saves your decisions and exact numbers to decisions.md before you compact, runs /compact with a line saying what to keep, then reloads CLAUDE.md, pastes the numbers back and asks what the goal is before the work goes on.

### "The agent ported the code, said it works, and it behaves differently."

The agent checked that the new code looked right, not that it does what the old code did. When a test failed, nothing stopped it from changing the test instead of the code.

**[`/tests-as-spec`](./skills/tests-as-spec/SKILL.md)** freezes the old test suite green, ports one module at a time, runs the same tests against the new code, compares old and new answers on the same input, and stops the agent the moment it edits a test.

### "My demo showed my inbox."

A recording catches everything on the screen, not just the part you meant to show. One frame with an email address, a key, a customer's name, a bank tab or a popup is enough, and once the video is posted, other people keep it.

**[`/redact-first`](./skills/redact-first/SKILL.md)** clears the screen before you record (Do Not Disturb on, extra tabs closed, fake names in place and no keys on screen), then checks the recording frame by frame for emails, keys, names, tabs and notifications, and blurs each one before you post.

### "The agent read it last week, and today it knows nothing about it."

What it learned stayed in a session that ended, or went into one giant notes file that nobody can search. Without a source next to each line, you cannot tell what it read from what it guessed.

**[`/agent-wiki`](./skills/agent-wiki/SKILL.md)** files what the agent reads into a wiki folder with one numbered page per topic and a source cited for every claim, edits the right page when you hand it a new article, keeps an index.md that lists every page, and deletes the pages that went stale in a weekly review, after your yes.

### "The tests were green, and the code was still a mess."

Tests check what the code does, not how it is built, so a screen that reads the database directly passes just like one that goes through the API. Files keep growing, the same logic gets copied and names like data2 stay, and no test ever turns red.

**[`/past-green-tests`](./skills/past-green-tests/SKILL.md)** runs four design checks after the tests pass (a check that blocks the UI from importing the database, a warning on files near 3,000 lines, a search for the same logic in several places and a list of names to rename), then gives a person a short list to tick: layers, names and size.

### "I shared my skill, and it broke the first time someone else used it."

It was only tried on a demo, and a demo is picked because it works. Nobody wrote down what it got wrong, so the same miss went out with it.

**[`/dogfood-first`](./skills/dogfood-first/SKILL.md)** runs it on this week's real tasks, logs one line per miss, fixes the miss that keeps coming back, runs the same tasks again to show fewer misses, and shares it only after three tested weeks.

### "It ran for an hour, crashed halfway, and I had to start over."

Nothing was saved along the way, and what was done lived only in the session that crashed. So nobody knew where to restart or which step broke things.

**[`/checkpoints`](./skills/checkpoints/SKILL.md)** commits a clean point before the job, keeps a progress.md of what is done, what runs now and what is next, commits every step on a branch, resumes at the step that crashed and rolls a bad step back with one git reset after your yes.

### "I gave it an hour of video, and it cost a fortune and still missed the part I needed."

An hour of video holds about 100,000 frames, and the agent tried to look at them instead of reading the words. The one minute that mattered got the same quick look as the other fifty-nine.

**[`/long-videos`](./skills/long-videos/SKILL.md)** turns the video into a timed transcript first, searches it for the minute that matters, looks at one frame every 10 seconds, cuts a two-minute clip for a close look, and puts a timestamp on every claim in the notes.

### "The agent tried one idea after another, and we are still stuck."

It chased the first guess, forgot what had already failed and called the last try the answer. Nothing was written down, so the same dead ends came back and nobody could check the fix.

**[`/hard-problems`](./skills/hard-problems/SKILL.md)** writes every guess down, runs one cheap test per guess, logs every try including the failures, keeps only the guess that survived and proves it with a result someone else can rerun.

### "We added AI to the business, and nobody can say what it saved."

It began as one big system for the whole team, so no single step got faster. Nobody counted the hours before, so nobody can count them after.

**[`/ai-in-business`](./skills/ai-in-business/SKILL.md)** maps one process step by step, finds the step done most often, builds a small agent for that step only, measures the hours before and after, and gives the agent a named owner with a weekly check.

### "I ran the agent in a sandbox, and it could still see my keys."

A sandbox limits what the agent can change, not what it can read. A key pasted in chat, printed in a log or left in a file it can open is a key it has.

**[`/keys-and-agents`](./skills/keys-and-agents/SKILL.md)** keeps every key out of the chat, has you type it into hidden input that saves it to a private file, shows each session only the keys its task needs, asks for read-only keys, and has you replace a leaked key the same day.

### "I repeated a vendor's number as fact, and it was only their claim."

A number passes from the company to someone quoting it and then to you, and each step drops a word like "single cluster" or "off-peak". The person quoting it adds their own math, so by the end nobody can tell who said what.

**[`/vendor-claims`](./skills/vendor-claims/SKILL.md)** names who made the claim and who passed it on, keeps what was measured and whose price it uses, separates the vendor's numbers from a commentator's estimate, and writes your line with a name and "unverified" next to every number.

### "I heard my tools were targets, and I still haven't updated anything."

The updates sit in a browser, a computer, a phone, a few apps and the server your agents run on, so each one waits for later. Nobody checks which ones landed, so a missed update looks the same as a done one.

**[`/update-sweep`](./skills/update-sweep/SKILL.md)** walks one sweep in order (browsers, the computer, phones and desktop apps, the box that runs your agents, then a week without random links), checks what it can see is out of date, asks before it installs or restarts anything, and reports each step as done or not done.

### "My server is online, and I don't know which doors are open."

A server has two ways in, the site and the server itself, and both face the whole internet. An SSH key does not stop an exploit in the software, and if you close the wrong door first, you lock yourself out.

**[`/server-lockdown`](./skills/server-lockdown/SKILL.md)** follows @levelsio's routine: it maps the open ports on your server, puts the site behind a Cloudflare Tunnel, connects you through Tailscale, locks the firewall only after you are logged in through Tailscale, and then reports each door before and after.

### "The agent's tests were green, and a user still could not get in."

The agent writes both the code and the tests, so the tests check what it fixed and miss the user it never thought about. Nobody reported that user, so the break shows up only when they try to get in.

**[`/user-path-test`](./skills/user-path-test/SKILL.md)** writes one yes/no test with you before the work starts, for the user the report left out, walking their whole path against the real running app. It breaks the fix on purpose once to prove the test can fail, and holds "done" until the test passes.

### "I asked for one line of work, and it made several decisions for me without asking."

A one-line task leaves gaps, and the agent fills each one with a guess. It tells you about some only after the code, and about some never.

**[`/ask-first`](./skills/ask-first/SKILL.md)** asks until the goal, the why and what done looks like are clear, asks every decision it would guess at once with a suggested answer for each, reports any problem it found on the way, and writes your answers as one definition with a yes/no check before any code.

### "AI designs my pages, and none of them look like me."

The agent has never seen your taste, so it falls back on its own default look. Each correction fixes one page, and the next page starts from the default again.

**[`/taste-skill`](./skills/taste-skill/SKILL.md)** collects your look from two or three pages you like, writes it as short yes/no rules including what is never allowed, saves them as a skill the agent loads whenever it designs, and has the agent check every design against those rules before you see it.

### "I let the agent clean up, and it deleted my project."

The agent wrote its own delete script and ran it on the real folder, so a link inside that folder led it straight into the project. The .git folder was on the same machine, so the history was deleted along with everything else.

**[`/safe-delete`](./skills/safe-delete/SKILL.md)** makes sure your work is pushed to a remote before the agent starts, runs every delete first as a dry run that only counts and stops when the count is far off, and rehearses the delete on a copy before the real folder is touched.

### "The agent said production was restored, and users still got errors."

The success line comes from the script or the agent, not from the site, so it can say "restored" while the old build or an error page is still live. Only the live address shows what users get.

**[`/live-check`](./skills/live-check/SKILL.md)** opens the live address itself, reads which version is really running there from the site, and walks one real user path start to end before anyone calls it restored.

### "The agent sent an email in my name without asking."

The agent was allowed to send, not only to write drafts, so nothing stood between its guess and your outbox. Reply and forward send too, and when one route is closed an agent may offer another.

**[`/draft-only-mail`](./skills/draft-only-mail/SKILL.md)** keeps read and draft, denies every tool and route that sends in Claude Code's permission settings, and checks in a fresh session that the send tools are gone before you trust it.

### "The agent made the code much faster, and it gave wrong answers on inputs nobody tried."

A fast rewrite is often correct only inside a range of sizes, types or values. Outside that range it returns a wrong answer with no error, and nobody tried an input out there before approving.

**[`/speedup-guard`](./skills/speedup-guard/SKILL.md)** runs the old and new code on the same inputs, edges included, finds where the fast version stops being correct, and adds a guard that sends every input outside those bounds back to the original.

### "I opened my project, and my files were empty."

The editor emptied the files as the project opened, and only what was committed had a copy to come back from. One developer on the Cursor forum was hit this way 25 times in 17 days and lost nothing that was committed.

**[`/save-points`](./skills/save-points/SKILL.md)** commits before the agent starts and before you close the laptop, keeps no agent edits waiting for review in Cursor, and runs git status when you open the project, so emptied files come back with one git restore.

### "I wrote the rule in AGENTS.md, and the agent keeps breaking it."

A rule in AGENTS.md is a request, and the agent can skip it. Writing it again only narrows the gap for a while, and it drifts back.

**[`/agent-hooks`](./skills/agent-hooks/SKILL.md)** moves one rule into a git pre-commit hook that checks the staged diff, refuses the commit when the rule is broken, prints the exact fix in words and is tested both ways before you trust it.

### "I built a Supabase app with an agent, and anyone can read my tables."

The public key ships inside the app on purpose, so only Row Level Security and a rule on each table keep a stranger out. When that switch is off, nothing looks wrong until a stranger reads the data.

**[`/stranger-test`](./skills/stranger-test/SKILL.md)** reads every table with the public key and no login, lists each one that sent back rows, and closes it with Row Level Security and one rule per table after your yes.

### "The agent ignores a rule I wrote, as if it never saw it."

Claude Code loads only the start of the memory index, and the cut comes from the end with no error. So the newest rules are the first ones the agent never sees.

**[`/memory-trim`](./skills/memory-trim/SKILL.md)** counts the lines and bytes of MEMORY.md against what loads, lists the rules past the cut, and rebuilds the index as one short line per rule, most important first, with the detail moved into topic files.

### "My agent waited for my approval, and the post missed its slot."

The agent stopped to ask before each step, so every slot depended on when you happened to answer. One late answer can hold a post past more than one slot.

**[`/day-gate`](./skills/day-gate/SKILL.md)** puts all of the day's packages (video, cover, caption) in one list, gets one yes from you for the whole day, runs each approved item at its slot without asking and holds anything you did not approve.

### "I sent an agent to do work that was already done."

Nobody looked at what existed before the agents went out, so finished work looked like new work. The request said what to do, and nothing in it said what was already done.

**[`/inventory-first`](./skills/inventory-first/SKILL.md)** lists what already exists (folders, finished outputs and tickets) with dates and counts before any job with several agents, asks you which items are new, and starts agents only for the ones you approved.

### "I approved the agent's change, and it edited one more line after."

An approval looks the same after an edit as it did before, so nobody notices that it now covers files that are gone. You, the agent and the next step all keep trusting a yes that was given to different files.

**[`/stamp-check`](./skills/stamp-check/SKILL.md)** saves a fingerprint of the files each check judged, compares it with the files right before anything ships, and if even one word changed, the check expires and runs again.

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
