T = int(input()) #amount of test cases

for i in range(T):
  N = int(input()) #amount of cars
  finished = []
  postp = [0]
  cars = [0]
  
  for j in range(N):
    cars.append(int(input()))
    
  j = 1
  success = True
  
  while True:
    if cars[len(cars)-1] == j:
      finished.append(cars[len(cars)-1])
      cars.remove(cars[len(cars)-1])
      j += 1
    elif int(postp[len(postp)-1]) == j:
      finished.append(postp[len(postp)-1])
      postp.remove(postp[len(postp)-1])
      j += 1
    elif len(cars)>1:
      postp.append(cars[len(cars)-1])
      cars.remove(cars[len(cars)-1])
    else:
      success = False
      break
    if j - 1 == N:
      break
  if success == False:
    print ("N")
  else:
    print ("Y")
