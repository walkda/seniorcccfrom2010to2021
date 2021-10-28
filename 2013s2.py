import sys

rw = sys.stdin.readline

w = int(rw())
n = int(rw())

cars = []
bridge = []
cc = 0
for i in range(n):
    car = int(rw()) 
    cars.append(car)

for car in cars:
    if len(bridge) == 4:# [50] cc > 1 [30,50] > 2
        bridge.pop(-1)
    bridge.insert(0,car)
    if sum(bridge) > w:
        print(cc)
        break
    else:
        cc += 1
        continue
    
#everytrhing works but 1 problem :/
