#!/usr/bin/env python3
"""qrun: a slot cap + a free-memory check before any heavy job starts (macOS)."""
import fcntl, os, re, subprocess, sys, time
def free_pct():
    out = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True).stdout
    m = re.search(r"free percentage:\s*(\d+)", out)
    return float(m.group(1)) if m else 100.0
def main():
    args = sys.argv[1:]; pool = "heavy"
    if args[:1] == ["--pool"]: pool, args = args[1], args[2:]
    if args[:1] == ["--"]: args = args[1:]
    cap = int(os.environ.get(f"QRUN_{pool.upper()}_MAX", "2")); need = float(os.environ.get("QRUN_MIN_FREE", "30"))
    d = os.path.expanduser(f"~/.cache/qrun/{pool}"); os.makedirs(d, exist_ok=True); t0 = time.time()
    while True:
        for i in range(cap):
            fd = os.open(f"{d}/slot{i}.lock", os.O_RDWR | os.O_CREAT, 0o644)
            try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError: os.close(fd); continue
            if free_pct() >= need:
                if time.time() - t0 > 1: print(f"qrun: waited {time.time()-t0:.0f}s", file=sys.stderr)
                return subprocess.run(args).returncode   # the lock is held until the job ends
            os.close(fd)   # give the slot back while memory is low
        time.sleep(2)
if __name__ == "__main__": sys.exit(main())
