"""wipes01 proof: what a commit saves when a tool zeroes your files. 210 committed files + 1 file with an uncommitted edit;
every file is truncated to 0 bytes (what the Cursor bug did on startup); git restore brings back what was committed.
Runs in a fresh temp dir. usage: zero_run.py OUT.txt"""
import os, subprocess, sys, tempfile, datetime, platform, time
base = tempfile.mkdtemp(prefix="wipes-"); out = []
def sh(c): return subprocess.run(c, cwd=base, shell=True, capture_output=True, text=True).stdout.strip()
def say(s): print(s); out.append(s)
say(f"## run {datetime.datetime.now():%Y-%m-%d %H:%M:%S} · macOS {platform.mac_ver()[0]} · {sh('git --version')}")
os.makedirs(os.path.join(base, "src"))
for i in range(210): open(os.path.join(base, "src", f"m{i}.dart"), "w").write(f"// module {i}\nint v{i} = {i};\n")
sh("git init -q -b main && git add -A && git commit -qm 'work, committed'")
open(os.path.join(base, "src", "m0.dart"), "a").write("// today's change, not committed yet\n")
say(f"$ git status --short | wc -l            -> {len(sh('git status --short').splitlines())} file with an uncommitted change")
for f in os.listdir(os.path.join(base, "src")): open(os.path.join(base, "src", f), "w").close()   # the wipe: every file to 0 bytes
empty = sum(1 for f in os.listdir(os.path.join(base, "src")) if os.path.getsize(os.path.join(base, "src", f)) == 0)
say(f"$ (startup wipe) files at 0 bytes         -> {empty}")
t = time.time(); sh("git restore ."); dt = time.time() - t
back = sum(1 for f in os.listdir(os.path.join(base, "src")) if os.path.getsize(os.path.join(base, "src", f)) > 0)
say(f"$ git restore .                          -> {dt:.2f} s, {back} files back")
say(f"$ grep \"today's change\" src/m0.dart       -> {'found' if 'today' in open(os.path.join(base, 'src', 'm0.dart')).read() else 'gone (it was never committed)'}")
open(sys.argv[1], "w").write("\n".join(out) + "\n")
