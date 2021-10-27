#this may have been the easiest s1 ever
n = int(input())
t = s = 0

for i in range(n):
    string = input().lower()
    t += string.count('t')
    s += string.count('s')

if t > s:
    print("English")
elif s > t:
    print("French")
elif t == s:
    print("French")
