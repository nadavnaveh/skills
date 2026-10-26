---
name: taste-skill
description: Turns your design taste into a Claude Code skill. It collects the look from two or three pages you already like, writes it as short yes/no rules (including what is never allowed), saves them as a skill the agent loads whenever it designs, and adds a self-check the agent runs on every design before it shows you. Fixes "AI designs my pages, and none of them look like me." Use when you build landing pages, sites, slides or posters with an agent, when every result comes out in the same generic style, or when you keep correcting the same colors, fonts or spacing. Also on /taste-skill.
---

# Taste skill

AI designs your pages, and none of them look like you. Your taste lives in your head, so the agent falls back on its own default look. This skill writes your taste down once as a skill, so every new page comes out in your look, even when you are not there to correct it.

Inspired by @elayadesigns on X, who builds landing pages with Claude and Cursor and their own designer skill: https://x.com/elayadesigns/status/2114049200749175174

## The principles
1. If your taste is not written down, the agent cannot use it.
2. A rule is a line someone can check yes or no. "Clean and modern" is not a rule. "Two fonts at most" is.
3. What is never allowed matters as much as what is. Our own rules: purple and white stay, green only for a result, red only for a rejection, never yellow.
4. A rule with no check is a wish. The agent checks every design before you see it.

## Steps
1. Collect the taste. Ask for two or three pages the person already likes, either their own or references they choose. For each one, write down the colors (exact values), the fonts and sizes, the spacing and the feel in a few words. Ask what they never want to see.
2. Write the rules as short lines, one rule per line, each one checkable yes or no. Group them under colors, type, spacing, layout and never allowed. Show the list and ask "Is this your taste?" Change it until the answer is yes.
3. Save it as a skill. Ask before writing any file. Then write `.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter. The description says when to load it, for example "Use whenever you design or change a page, slide or poster", so the agent loads it when it designs.
4. Add a self-check to the skill: every rule as a yes/no question the agent answers on each design before it shows it. If any answer is no, the agent fixes the design and checks again. It never shows a design that failed. Our poster skill works this way: when text had to shrink to fit, it refuses the render until the layout is fixed.
5. Use it on the next page. Show the self-check with the design: each rule, yes or no.
6. When the person corrects the same thing twice, turn that correction into a new rule or a sharper one. Add it to the check and show them the change.

## Rules
- Ask before writing or changing any file.
- Never invent the person's taste. Every rule comes from their pages or their words.
- Exact values beat adjectives: a color code, a font name, a size.
- Keep the skill short. If a rule never gets checked, cut it.
