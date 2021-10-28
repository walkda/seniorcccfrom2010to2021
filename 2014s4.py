n = int(input())
t = int(input())
biggest = 2**31
coors = {}
total_area = 0
for i in range(n):
    coor = list(map(int,input().split()))
    
    for y in range(coor[1], coor[3] ):
        for x in range(coor[0], coor[2]):
            if ((x,y),(x+1,y+1)) not in coors:
                coors[((x,y),(x+1,y+1))] = coor[4]
            else:
                coors[((x,y),(x+1,y+1))] += coor[4]

for k in coors:
    if coors[k] >= t:
        total_area += 1

print(total_area)
