---
name: teachability-check
description: Asks one cheap question before an agent spends money or hours on a task. The question is what someone can do next week because of this, and whether it will still teach next month. If the source has no answer, the agent writes THIN with the reason and stops. Fixes "I paid for the voice and the render, and the post had nothing to teach." Use before a voice take, a render, a paid API batch or a long build, and whenever an agent picks posts, articles or tickets to turn into content. Also on /teachability-check.
---

# Teachability check

You paid for the voice and the render, and the post had nothing to teach. Nobody asked what it gives before the paid work started, so a reaction or a launch note looked like a lesson. This skill asks one question first and stops the task when the answer is nothing. One night, our agents picked five posts, and this question stopped four of them before any voice was made.

## The principles
1. Ask before you pay. A check that answers after the paid work has started saves nothing.
2. "Nothing" is a valid answer. Do not stretch a thin source with facts from elsewhere to make it pass.
3. It must still teach next month. A launch note or a reaction is news today and nothing next month.
4. It judges what the source gives you, not the author.

## Steps
1. Before the first step that costs money or more than a few minutes, read only the source: the post, the ticket or the brief. No web search, no other files.
2. Answer two yes/no questions:
   - Next week: does the source give one step someone could take next week? Write it in one sentence. A stranger must be able to say yes, that is one step. "Learn about X" or a feeling is a no.
   - Next month: will that step still be useful next month?
3. Quote the line in the source that carries the step. If there is no such line, the answer is no.
4. At the top of the task's notes file, write GO, or write THIN with the reason in one line ("a reaction with no method", "a launch note").
5. On THIN, do not start the paid step. Tell the owner in one line what was skipped and why, then move to the next task.
6. On GO, carry the one-sentence step forward. The finished work must keep that promise.
7. To make it run every time, add one line to CLAUDE.md above the paid steps: "Before any paid or long step, run /teachability-check on the source. THIN means stop." This is a request to the agent, not a hook. For a hard stop, write the check into the task's own steps, ahead of the paid one.

## Rules
- If the answer comes after a script, a proof or a voice take has started, stop at once and say what was already spent.
- Never start the paid step on a check that was not run.
- Read the THIN lines once a week. If one stopped something you wanted, sharpen the next-week question for your kind of work.
- It catches work with nothing to give, not work done badly.
