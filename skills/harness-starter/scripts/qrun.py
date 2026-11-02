#!/usr/bin/env python3
"""qrun: a queue for heavy jobs. A job takes a slot and starts only when enough memory is free. Usage: python3 qrun.py [--pool heavy] -- <command>
QRUN_HEAVY_MAX = slots (default 2) · QRUN_MIN_FREE = percent free to start (default 30; 0 = skip the check). macOS and Linux. If it can't read memory it refuses."""
import fcntl, os, re, subprocess, sys, time


def free_pct():
    if os.environ.get("QRUN_TEST_NO_METER"): return None
    if sys.platform == "darwin":
        out = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True).stdout
        m = re.search(r"free percentage:\s*(\d+)", out)
        return float(m.group(1)) if m else None
    try:
        info = dict(re.findall(r"(\w+):\s+(\d+)", open("/proc/meminfo").read()))
        return 100.0 * int(info["MemAvailable"]) / int(info["MemTotal"])
    except (OSError, KeyError, ZeroDivisionError):
        return None


def main():
    args = sys.argv[1:]; pool = "heavy"
    if args[:1] == ["--pool"]: pool, args = args[1], args[2:]
    if args[:1] == ["--"]: args = args[1:]
    if not args: sys.exit("usage: qrun.py [--pool NAME] -- <command>")
    cap = int(os.environ.get(f"QRUN_{pool.upper()}_MAX", "2")); need = float(os.environ.get("QRUN_MIN_FREE", "30"))
    d = os.path.join(os.environ.get("QRUN_DIR") or os.path.expanduser("~/.cache/qrun"), pool); os.makedirs(d, exist_ok=True); t0 = time.time()
    if need > 0 and free_pct() is None:
        print("qrun: can't read free memory, refusing to start. Set QRUN_MIN_FREE=0 to skip the check.", file=sys.stderr); return 3
    while True:
        for i in range(cap):
            fd = os.open(f"{d}/slot{i}.lock", os.O_RDWR | os.O_CREAT, 0o644)
            try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError: os.close(fd); continue
            f = 100.0 if need <= 0 else free_pct()
            if f is not None and f >= need:
                if time.time() - t0 > 1: print(f"qrun: waited {time.time() - t0:.0f}s", file=sys.stderr)
                return subprocess.run(args).returncode   # the lock is held until the job ends
            os.close(fd)   # give the slot back while memory is short
        time.sleep(2)


if __name__ == "__main__": sys.exit(main())
