import sys
raw_input = sys.stdin.readline


ar = raw_input()

dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D":500, "M": 1000}

s = []

s.append(dic[ar[-2]] * int(ar[-3]))
#s.append(int(ar[0]) * dic[ar[1]])

for i in range(1,len(ar) // 2 ):
    A = ar[(i-1)*2]
    R = ar[((i-1)*2) + 1]
    Ap = ar[(i*2)]
    Rp = ar[(i*2) + 1]
    if dic[Rp] > dic[R]:
        s.append(-1 * (int(A) * dic[R]))
    else:
        s.append(int(A) * dic[R])


print(sum(s))

