---
name: gantt
description: Turns one goal into tickets, marks what depends on what, and draws a Gantt chart that shows which agents can run in parallel and which must wait. Fixes "I run several agents and they wait on each other, redo each other's work, or I lose track of who does what." Use when a goal is bigger than one task, when you are about to open more than one agent or session, when the user asks for a plan, a roadmap, a timeline or "what can run in parallel", or on /gantt.
---

# Gantt

You opened three agents. Two did the same thing, one waited for something nobody was doing, and you lost track. More agents do not make you faster until you can see what depends on what. This skill turns one goal into a picture you can manage.

## The principles
1. Start from the goal, not from the agents. The number of agents is an output of the plan.
2. A ticket is small enough for one agent in one go, and it says what it needs and what it hands on.
3. The dependencies decide the speed. What can run at the same time, runs. What waits, waits for something named.

## Steps
1. Write the goal in one sentence, with how you will know it is done. If it is unclear, ask first (one to three questions), and do not plan a guess.
2. Break it into tickets. Each one gets: an id (T1, T2…), a title, a done-test a stranger could check yes or no, a size (S = under an hour, M = a few hours, L = a day; split anything bigger), and who does it (an agent, a person, or the owner).
3. Mark dependencies: for each ticket, which tickets must finish first, and what exactly it receives from them. A dependency you cannot name is not one.
4. Draw the Gantt as a Mermaid `gantt` block (it renders on GitHub, in Notion and in most editors), with one section per lane, so tickets in different lanes run at the same time. Under it, the same plan as a plain table: ticket · lane · needs · done-test.
5. Name three things under the chart:
   - **Critical path:** the chain of tickets that decides the finish date. Speed here, not elsewhere.
   - **Parallel now:** the tickets that can start right away, each one a separate agent or session.
   - **Waiting:** every ticket that is blocked, and on what. Anything waiting on the owner goes first.
6. Ask "Is this the plan?" Start only after a yes. When work lands, update the chart: done, moved, or blocked, never silently changed.

## Rules
- Never start more agents than there are tickets in "parallel now".
- Two tickets that change the same file or the same thing are not parallel. Put them in one lane.
- Dates are estimates. Mark them as estimates, and move them in the chart when they move.
- The owner's decisions are tickets too, with a date. A plan blocked on an unasked question is late already.
