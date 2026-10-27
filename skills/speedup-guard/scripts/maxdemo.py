"""doubleAI's own example (heymaxwell.ai): original() double loop vs replacement() n*(n-1)/2 in 64-bit integers, with their stated condition 0 <= n <= 3037000500"""
import time, numpy as np
def original(n):
    s = 0
    for i in range(n):
        for j in range(i):
            s += 1
    return s
def replacement(n):                      # the Rust i64 version, emulated with numpy int64 (wraps on overflow like release-mode Rust)
    with np.errstate(over="ignore"):
        n = np.int64(n); return int(n * (n - np.int64(1)) // np.int64(2))
def guarded(n):
    return replacement(n) if 0 <= n <= 3037000500 else n * (n - 1) // 2   # outside the proven range: back to the exact math (stands in for the original)
# 1) equal on every n from 0 to 2000 (the loop itself)
t = time.time(); bad = [n for n in range(2001) if original(n) != replacement(n)]; t1 = time.time() - t
print("n 0..2000: mismatches", len(bad), f"({t1:.1f} s for the loops)")
# 2) speed at n = 3000
t = time.time(); a = original(3000); to = time.time() - t
t = time.time(); b = replacement(3000); tr = time.time() - t
print(f"n=3000: original {to*1000:.1f} ms, replacement {tr*1e6:.1f} us, equal {a == b}, x{to/tr:,.0f}")
# 3) at the edge of the proven range, against exact math (Python ints never overflow)
for n in (3037000500, 3037000501, 4000000000):
    exact = n * (n - 1) // 2
    print(f"n={n}: exact {exact}, replacement {replacement(n)}, equal {replacement(n) == exact}, guarded equal {guarded(n) == exact}")
