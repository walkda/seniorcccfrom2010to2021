n = int(input())
codes = {}
fs = ''
for i in range(n):
    s = input().split()
    codes[s[0]] = s[1]
string = input()

i = 1
for j in range(len(string)*10):
    if string[0:i] in list(codes.values()):
        for key in codes:
            if codes[key] == string[0:i]:
                fs += key
        ls = list(string)
        del ls[0:i]
        string = ''.join(ls)
        i = 1
    else:
        i += 1
print(fs)
