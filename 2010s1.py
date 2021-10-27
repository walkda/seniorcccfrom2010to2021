n = int(input())
f = []
cn = []
if n == 0:
    print("")
elif n == 1:
    s = input().split()
    print(s[0])
else:
    for i in range(n):
        s = input().split()
        cn.append(s[0])
        f.append((s[0], 2 * int(s[1]) + 3 * int(s[2]) + int(s[3])))



    f.sort(key=lambda x: x[1])
    f.reverse()
    del f[2:]

    if f[0][1] == f[1][1]:
        f.sort(key=lambda x: x[0])
        


    for c in f:
        print(c[0])
