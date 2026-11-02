---
name: rejections-to-tests
description: Turns every result you reject into one sentence on what was wrong and why, turns that sentence into a yes/no question someone else could answer, and has the agent run all the questions on every new result before you look. Fixes "I keep rejecting the same mistake, and the agent keeps making it." Use when you reject or correct a result, when the same mistake comes back, and before the agent shows you any result. Also on /rejections-to-tests.
---

# Rejections to tests

You rejected the result, and the next one had the same mistake.
The reason stayed in your head. A test the agent writes for itself checks what it meant to make, not what you wanted.
This skill turns each rejection into a question someone else could answer, and runs every question before you look.

## The principles
1. The test comes from your rejection, not from the agent. An agent that writes its own test grades its own work.
2. A rejection with no reason cannot become a test. Write what was wrong and why.
3. A question is a test only if someone else would give the same yes or no.

## Steps
1. Every time the person rejects a result, write one sentence: what was wrong and why, in their words. If the reason is missing, ask for it. Do not guess it.
2. Turn the sentence into a yes/no question someone else could answer without asking the person. "Is it good?" is not a question. "Does the opening claim something that did not happen?" is.
3. Run the question on the rejected result. It must fail. If it passes, it is not testing the rejection: rewrite it.
4. Ask "Is this the test you meant?" After a yes, save the question, its sentence and its date in `tests/rejections.md`, and add one line to CLAUDE.md: "Before showing any result, run tests/rejections.md."
5. Before the person sees any new result, run every question. A question code can answer (a banned phrase, a word count) runs as a small script. Every other question goes to a fresh subagent that did not make the result, with only the question and the result.
6. Fix what failed and run again. Report each question as pass, fail or not run, with the line that decided it.

## Rules
- The agent never writes, edits or deletes a question without the person's yes, and never changes one to make a result pass. When a result that passed every question is still rejected, a test is missing: go back to step 1.
- A question that was not run is reported as not run.
- "Every question passed" is not the person's yes. They still look.
