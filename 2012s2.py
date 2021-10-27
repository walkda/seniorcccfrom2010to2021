import sys
from math import factorial as f
raw_input = sys.stdin.readline

jn = int(raw_input())
if jn < 4:
    print(0)
elif jn == 4:
    print(1)
else:

    n = jn - 1
    r = 3

    form = (f(n)) // (f(r) * f((n - r))) #nCr formula

    print(form)
