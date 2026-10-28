---
name: to-gantt
description: Turns whatever you have (a goal, a list of tasks, notes, a chat, a document, a backlog, a messy plan) into a Gantt chart that shows what depends on what, what can run in parallel and what must wait. Fixes "I run several agents and they wait on each other, redo each other's work, or I lose track of who does what." Use when the user types /to-gantt, pastes tasks or notes and wants a plan, asks for a roadmap, timeline, schedule or "what can run in parallel", or is about to open more than one agent or session. Also on /to-gantt.
---

# To Gantt

You opened three agents. Two did the same thing, one waited for something nobody was doing, and you lost track. More agents do not make you faster until you can see what depends on what. This skill takes whatever you already have and turns it into a picture you can manage.

## The principles
1. One board shows what depends on what and what can run in parallel. Read what the user already has before you plan, and keep their words.
2. Every ask an agent brings back (a question, a plan to approve, a diff to read) is a row on the board, with the time it started waiting.
3. You are the bottleneck: whatever waits on you goes first.

## Steps
1. **Read the input and say what you found** in two lines: the goal, how many pieces of work, and any owners, dates or order already in it. If the deadline or who does the work is missing, ask once; otherwise ask nothing.
2. **Make tickets.** One per piece of work, small enough for one agent or person in one go: an id (T1, T2…), the user's own words as the title, an owner, and a done-test a stranger could check yes or no.
3. **Mark dependencies.** For each ticket, which tickets must finish first. A dependency you cannot name is not one. Two tickets that change the same thing are not parallel.
4. **Add a row for every ask that waits on the user**: an agent's question, a plan to approve, a diff to read, with the time it started waiting. Agents stop while they wait, so these rows go at the top.
5. **Draw the board** as text bars, one row per ticket, equal-width time slots, labels aligned over them (███ working, ░░░ not started, ▓▓▓ waiting on you):
   ```
                         22  23  00  01
   T0 You approve plan   ▓▓▓ ▓▓▓ ░░░ ░░░   waiting since 22:20
   T1 Write copy         ███ ███ ░░░ ░░░
   T2 Build page         ░░░ ░░░ ███ ███   needs T0, T1
   ```
6. **Name three things under it:** the waiting rows (oldest first), what can run in parallel right now, and the chain that decides the finish.
7. **Ask "Is this the plan?"** and start nothing until the user says yes. When work lands or an ask is answered, redraw.

## Rules
- Whatever waits on the user goes first; say how long it has waited.
- Never start more agents than there are tickets that can run in parallel now.
- Dates are estimates; mark them so.
