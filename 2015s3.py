g = int(input())

p = int(input())

docks = 0
ava_docks = list(range(1,g+1))
for i in range(p):
    ith = int(input())
    possible_docks = list(reversed(list(range(1,ith+1))))
    if True not in list([dock in ava_docks for dock in possible_docks]):
        break
    for dock in possible_docks:
        if dock in ava_docks:
            docks += 1
            ava_docks.remove(dock)
            break
    else:
        continue
print(docks)
            
