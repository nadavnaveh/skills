---
name: redact-first
description: Checks a screen recording, demo or screenshot for the five things that leak (email addresses, API keys, real names, open tabs and notifications), clears them before you record, and blurs or replaces anything left before you post. Fixes "my demo showed my inbox." Use before you record a demo, take a screenshot for a post, share your screen or post any video or image of your work, and whenever a recording shows a terminal, an inbox, a CRM or a browser. Also on /redact-first.
---

# Redact first

Your demo showed your inbox. Nobody looked at the screen the way a stranger would, one frame at a time. This skill clears the screen before you record, then checks every frame before you post, and blurs whatever is still there.

## The principles
1. One frame is enough to leak. A key that is on screen for half a second has been posted.
2. Clean the screen before you record. Blurring afterwards is the backup, not the plan.
3. Real people stay out of frame. Their names are not yours to share.
4. Check what was recorded, not what you meant to record.

## Steps
1. Before recording, list what will be on screen: which apps, which windows, which pages and which terminal commands.
2. Clear the screen:
   - Turn on Do Not Disturb or a Focus mode, so no message pops up mid-recording.
   - Close every tab and window the demo does not need, your bank first. When you can, record one window instead of the whole screen.
   - Swap real customer names and email addresses for fake ones, or use a demo account.
   - Never run `cat .env` or print a key on screen. Show the variable's name, not its value.
3. Show this as a short checklist and ask "Ready to record?" Start only after a yes.
4. After recording, check it frame by frame. If ffmpeg is installed, pull frames from the video and look at each image. Look for five things: email addresses, keys and tokens, real names, open tabs and notifications.
5. List every hit with its frame number and what it shows, for example "frame 212: an email address in the To field".
6. Fix each hit: blur it, replace it with [redacted] or cut those frames. A key that was on screen has leaked, so rotate it even after you blur it.
7. Check the fixed version again from the start. Report each of the five as clear, fixed (with the frame numbers) or not checked. Say "ready to post" only when all five are clear or fixed.

## Rules
- Never post a recording that nobody checked frame by frame.
- A blurred key still gets rotated.
- If you cannot check a frame yourself, say so and give the owner the exact frames to look at.
- A fixed frame counts only after it has been checked again.
