k = int(input())

s = []
for i in range(k):
    b = int(input())
    if b == 0:
        s.pop(-1)
    else:
        s.append(b)
print(sum(s))
