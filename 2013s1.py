import sys

rw = sys.stdin.readline

y = int(rw())

def dd(n):
    return len(set(list(str(n)))) == len(list(str(n)))
for i in range(1,2**31):
    if dd(y+i):
        print(y+i)
        break
