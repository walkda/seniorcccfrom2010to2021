n = int(input())

l1 = input().split()
l2 = input().split()
pair = {}
bad = False

for i in range(n):
    if l1[i] == l2[i]:
        bad = True
    else:
        pair[l1[i]] = l2[i]


if all([name == pair[pair[name]] for name in pair]) and (not bad):
    print("good")
else:
    print("bad")
