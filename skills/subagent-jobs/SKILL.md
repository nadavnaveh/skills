---
name: subagent-jobs
description: Sends the reading-heavy parts of a task (searching code, reading long logs, running the tests, reviewing a draft, researching a question) to a subagent with its own clean window, and takes back only a short summary. Fixes "my session filled up with files and logs, and the agent lost the thread." Use when you are about to read many files to find one thing, open a long log or command output, run a full test suite, ask for a review of work you just wrote, or look something up across several web pages. Also on /subagent-jobs.
---

# Subagent jobs

The main session filled up with files, logs and test output, and the agent lost the thread. Everything it reads stays in its window and is sent again on every turn. This skill hands the heavy reading to a subagent, which works in its own clean window and sends back only a summary.

## The principles
1. A subagent has its own window. What it reads stays there. Only its answer comes back.
2. Ask for the answer, not the material. Forty files in, three lines out.
3. A fresh agent sees what the writer cannot. It never saw the draft, so it sees the gaps.
4. A summary is a claim. It must point to where it came from: a file and line, a test name, a link.

## Steps
1. Before you read anything, look at the size of the job. If it means many files, a long log, the full test suite, a review of your own work or several web pages, send it to a subagent. If it is one known file or one short command, do it yourself.
2. Write the brief: the question, where to look, what it must not change, and the exact shape of the answer (for example "at most 5 lines, each with a file and line number").
3. Pick the job:
   - **Search code**: find where something happens. Return the files and lines, not the files themselves.
   - **Long logs**: read the log. Return the first error, how many times it happens, and the lines around it.
   - **Run the tests**: run the whole suite. Return how many passed and, for each failure, the test name and the error.
   - **A fresh review**: give it only the diff (or the draft) and the goal, not your reasoning. Return the gaps it finds.
   - **Research**: read the sources. Return one answer with a link for each claim, and say where sources disagree.
4. Run jobs that do not depend on each other at the same time, one subagent each.
5. Check the answer before you use it: open one cited line, rerun one failing test, or open one link.
6. Keep only the summary in the main session, and tell the person what came back.

## Rules
- Read-only by default. A subagent that searches, reads or reviews does not edit files.
- The answer length goes in the brief. "Summarize" alone gets an essay.
- The reviewer never gets the writer's notes, only the work and the goal.
- If a subagent's answer has no source, send it back.
