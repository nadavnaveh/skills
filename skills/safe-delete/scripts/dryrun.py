"""deletecopy01 proof 4: a dry run counts what a cleanup script WOULD delete, and catches a link into the real project.
Stand-in for the Windows junction case (we are on macOS): a temp folder with 3 files and one symlink to a 1,200-file project,
and a cleanup walker that follows links (os.walk followlinks=True), the way the reported script walked through the junctions.
Nothing is deleted: --dry-run only counts. Runs in a fresh temp dir. usage: dryrun.py OUT.txt"""
import os, sys, tempfile, datetime, platform

base = tempfile.mkdtemp(prefix="dryrun-")
proj, tmp = os.path.join(base, "project"), os.path.join(base, "temp")
for i in range(1200):
    d = os.path.join(proj, "src", f"m{i // 100}"); os.makedirs(d, exist_ok=True); open(os.path.join(d, f"f{i}.py"), "w").write(f"x = {i}\n")
os.makedirs(tmp)
for i in range(3): open(os.path.join(tmp, f"cache{i}.tmp"), "w").write("old\n")
os.symlink(proj, os.path.join(tmp, "mirror_link"))

def cleanup(root, dry_run=True):
    """the cleanup walker: every file under root, following links"""
    hits = [os.path.join(d, f) for d, _, fs in os.walk(root, followlinks=True) for f in fs]
    if not dry_run:
        raise SystemExit("this proof never deletes")
    return hits

out = [f"## run {datetime.datetime.now():%Y-%m-%d %H:%M:%S} · macOS {platform.mac_ver()[0]} · Python {platform.python_version()}",
       "$ ls temp                              -> cache0.tmp cache1.tmp cache2.tmp mirror_link -> ../project",
       "$ expected to delete                   -> 3 files"]
hits = cleanup(tmp, dry_run=True)
inside = sum(1 for h in hits if os.path.realpath(h).startswith(os.path.realpath(proj)))
out += [f"$ python cleanup.py temp --dry-run   -> would delete: {len(hits)} files",
        f"$   of them inside the real project   -> {inside}",
        "$ stop: count != expected             -> nothing deleted"]
print("\n".join(out)); open(sys.argv[1], "w").write("\n".join(out) + "\n")
