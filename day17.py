"""
Aoc 2017
kubz113
"""

steps = 329

spinLock = [0]
currentLocation = 0
for i in range(1,2018):
    size = len(spinLock)
    index = ((currentLocation+steps)%size)+1
    currentLocation = index
    spinLock.insert(index, i)

i = spinLock.index(2017)+1
print(spinLock[i])
               
spinLockPart2 = []

currentLocation = 0
for i in range(1,50000001):
    if i%100000==0:
        print(i)
    size = len(spinLock)
    index = ((currentLocation+steps)%size)+1
    currentLocation = index
    spinLock.insert(index, i)


i = spinLockPart2.index(0)+1
print(spinLockPart2[i])
               
