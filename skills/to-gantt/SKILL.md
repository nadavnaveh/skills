---
name: to-gantt
description: Turns whatever you have (a goal, a list of tasks, notes, a chat, a document, a backlog, a messy plan) into a Gantt chart that shows what depends on what, what can run in parallel and what must wait. Fixes "I run several agents and they wait on each other, redo each other's work, or I lose track of who does what." Use when the user types /to-gantt, pastes tasks or notes and wants a plan, asks for a roadmap, timeline, schedule or "what can run in parallel", or is about to open more than one agent or session.
---

# To Gantt

You opened three agents. Two did the same thing, one waited for something nobody was doing, and you lost track. More agents do not make you faster until you can see what depends on what. This skill takes whatever you already have and turns it into a picture you can manage.

## The principles
1. Start from where the user is. A list, a goal, a pasted chat: read it before you plan, and keep their words.
2. The shape follows the input. Find the work, the order and the people in what they gave you before you add anything.
3. The dependencies decide the speed. What can run at the same time, runs. What waits, waits for something named.

## Steps
1. **Read the input and say what you found**, in two or three lines: the goal (stated, or the one the items point to), how many pieces of work, any dates, owners or order already in it, and what is missing.
2. **Ask only what changes the chart** (zero to three questions): usually the deadline, who does the work (agents, people, the user), and what "done" means. If the input already answers them, ask nothing and say so. Never plan a guess you could have asked about.
3. **Make tickets.** One per piece of work, small enough for one agent or person in one go. Each gets an id (T1, T2…), the user's own words as its title, a size (S under an hour, M a few hours, L a day; split anything bigger), an owner, and a done-test a stranger could check yes or no.
4. **Mark dependencies.** For each ticket: which tickets must finish first, and what it receives from them. A dependency you cannot name is not one. Two tickets that change the same thing are not parallel.
5. **Draw the Gantt** in the form that fits where the user is:
   - In a terminal or chat, draw it as text bars, one row per ticket, so it reads at a glance. Give each time slot the same width (2 to 4 characters), put the time labels on a header line aligned over their slots, and keep each row short enough not to wrap:
     ```
                       Mon Tue Wed Thu
     T1 Write copy     ███ ███ ░░░ ░░░
     T2 Pick photos    ███ ░░░ ░░░ ░░░
     T3 Build page     ░░░ ░░░ ███ ███   needs T1, T2
     ```
   - Where it renders (GitHub, Notion, most editors), also give a Mermaid `gantt` block with one section per lane.
6. **Name three things under the chart:**
   - **Critical path:** the chain that decides the finish date. Speed here, not elsewhere.
   - **Parallel now:** the tickets that can start right away, each one a separate agent or session.
   - **Waiting:** every blocked ticket and what it waits on. Anything waiting on the user goes first.
7. **Ask "Is this the plan?"** Start nothing until the user says yes. When work lands, redraw: done, moved or blocked, never silently changed.

## Rules
- Never start more agents than there are tickets in "parallel now".
- Dates are estimates; mark them as estimates and move them when they move.
- The user's decisions are tickets too, with a date.
