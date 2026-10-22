---
name: update-sweep
description: Walks one update sweep in order (browsers, the computer, phones and desktop apps, the box that runs your agents, then a careful week online), checks what it can see is out of date, asks before it installs or restarts anything, and reports each step as done or not done. Fixes "I heard my tools were targets, and I still haven't updated anything." Use after news of security holes, when someone says "update everything", or before you leave agents running on a server. Also on /update-sweep.
---

# Update sweep

You heard your tools are targets, and you still have not updated anything. The updates sit in a browser, a computer, a phone, a few apps and a server, so each one waits for later. This skill walks one sweep with you, in order, and reports what got done.

Source: @Eito_Miyamura on X, https://x.com/Eito_Miyamura/status/2112901351370047766 (unverified).

## The principles
1. Update everything. A patch protects you only once it is installed.
2. Patch every place you work, including the box your agents run on.
3. Until the patches go through, stay inside walled gardens online.

## Steps
1. **Browsers.** Start with Chrome, then Firefox: the user installs the update from the browser's menu and relaunches. Safari updates with macOS, in step 2.
2. **The computer.** Mac: run `softwareupdate --list`; by hand it is System Settings, General, Software Update. Linux: run `sudo apt update`, then `apt list --upgradable`. Windows: the user opens Windows Update in Settings. Show the list and ask "Install these now?" Ask again before any restart.
3. **Phones and desktop apps.** The user updates the phone, then each desktop app (Slack, Cursor, Discord and the rest) from its own menu, and ticks each one.
4. **The box that runs your agents.** Ask about any remote home server or agent box (the source names Openclaw and hermes boxes). Connect the way the user already does and run the same apt checks. If it does not use apt, ask for its update command and run only its check form. Ask before you upgrade or restart, then run the check again.
5. **This week.** Ask the user to stay inside walled gardens like X and YouTube, and not to click random links until the patches go through.
6. **Report.** List the five steps as **Done** (the output you saw or the user's tick) or **Not done** (why, and the user's next step). Then list what you could not check: the phone, browser relaunches, app menus.

## Rules
- Before the user's yes, run only checks that install nothing: `softwareupdate --list`, `sudo apt update`, `apt list --upgradable`. `sudo apt update` may ask for a password; if it will not run, the user runs it.
- Nothing installs or restarts without the user's yes.
- A step nobody checked is not done. What you could not see, the user ticks.
- Facts about why come only from the source above, and it is unverified.
