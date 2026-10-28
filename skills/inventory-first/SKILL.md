---
name: inventory-first
description: Before any job with several agents, lists what already exists (folders, finished outputs, tickets) with dates and counts, shows you the list and asks what is new, then starts agents only for the new items you approved. Fixes "I sent an agent to do work that was already done." Use before you start more than one agent or any subagent on a batch job (cut clips, process files, write pages, close tickets), when a request says "all", "every" or "the new ones", and when you pick up a job that was started in an earlier session. Also on /inventory-first.
---

# Inventory first

You sent an agent to do work that was already done. Nobody looked at what existed before the agents went out, so finished work looked like new work. This skill lists what is already there, asks you what is new, and starts agents only for that.

## The principles
1. Look before you send. The list comes before the first agent.
2. A list without dates and counts is not an inventory. "Some clips exist" does not tell you what is new.
3. The person says what is new. The agent does not guess it from the request.
4. A date on a file is the last time it changed, not the day it was made. Say so next to the list.

## Steps
1. Before you start any subagent, write the job in one line and name where its work lives: the input folder, the output folder and the tickets.
2. List what already exists in each place. Count the items and group them by last-changed date. Count finished outputs on their own line, apart from the inputs (for example, job folders and the finished files inside them). Use only commands that read, never ones that change.
3. Add what the record says: open and closed tickets for this job, notes in CLAUDE.md or memory, and the git log for these folders.
4. Show the list as a short table: what, how many, which dates. Then ask "Which of these are new?" Start nothing before the answer.
5. Write down the approved new items by name. Anything not on that list is left alone.
6. Start agents only for the approved items. Give each agent its exact items and tell it not to touch finished outputs.

## Rules
- No agent starts before the list is shown and answered.
- If the list cannot be made (a folder is missing or a command fails), say so and stop. A list that failed is not "nothing done".
- If an item looks finished and you are not sure, ask. Do not redo it.
- Our proof is in scripts/PROOF.md and scripts/inventory-run.txt. On 19 Oct an agent was sent to cut clips that were already cut on 5 Oct, and a later listing of the same folder showed 30 job folders and 16 finished clips dated 5 Oct. It does not show what the repeat cost in time or money. The dates are last-change dates, not creation dates. And that agent was stopped by a person, not by a list.
