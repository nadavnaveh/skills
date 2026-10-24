---
name: server-lockdown
description: Takes a rented server (VPS) off the public internet by closing its two doors, following @levelsio's routine. Fixes "My server is online, and I don't know which doors are open." Use when you have a VPS with a site or app on it, when you set up a new VPS, or before you trust an SSH key alone. Also on /server-lockdown.
---

# Server lockdown

Every open door on your server faces the whole internet, and an SSH key does not close one that a software bug opens. This skill closes both doors, the old way in last.

Source: @levelsio on X, https://x.com/levelsio/status/2113587042185576853 (an X post, not verified).

## The principles
1. A server has two doors: the site or app, and the server itself (SSH and any open port). Close both, and it is off the public internet.
2. An SSH key alone is not enough. Per the source, the threat is exploits and vulnerabilities AI is finding.
3. Never close the way in you are using until the new one is proven.

## Steps
1. Map the two doors. Work from the user's computer over their SSH session, with read-only checks: the ports the server listens on, its firewall, and any cloud firewall at the provider, so the map shows what is reachable. Group them: the site door (web ports) and the server door (SSH and every other port). Change nothing.
2. Explain the site door. A bug in the site can open the server, whatever the SSH settings. His example is the PHP exploit in his post, a file upload hack.
3. Close it. Put the site or app behind a Cloudflare Tunnel. Per the source, the default Free Plan has WAF security on by default. Check that the site loads through the tunnel.
4. The server door. Install Tailscale on the server and the user's computer. Have the user open a second session through Tailscale, and keep the current one open.
5. Lock it, only after the user confirms they are logged in through Tailscale. Set the firewall to allow Tailscale and close public SSH and every other open port, web ports 80 and 443 included. Check that the site still loads through the tunnel and a fresh Tailscale session works. If either fails, undo it from the open session.
6. Report. Rerun the read-only checks. Show each door before and after, and what the user must still do by hand: add the domain to Cloudflare, set the DNS records, sign in to Tailscale on each device.

## Rules
- Ask before every change. Say what it does and how to undo it.
- For exact install and setup commands of Cloudflare Tunnel, Tailscale and the firewall, read the official docs for the server's OS at run time, and say so.
- Never close the current way in until the new one is proven, or the user is locked out.
- A step the user did not confirm is reported as not done.
