# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:30:23 2017

@author: kubz113
"""

memoryBlockText = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

memoryBlockArray = list(map(int, memoryBlockText.split("\t")))

memoryBlockPastStates = []
memoryBlockLen = len(memoryBlockArray)
totalRuns = 0

while not (memoryBlockArray in memoryBlockPastStates):
    memoryBlockPastStates.append(memoryBlockArray[:])
    blocks = max(memoryBlockArray)
    maxIndex = memoryBlockArray.index(blocks)
    memoryBlockArray[maxIndex]=0
    for i in range(1,blocks+1):
        nextIndex = (maxIndex+i)%memoryBlockLen
        memoryBlockArray[nextIndex] +=1
    totalRuns+=1
print(totalRuns)

loopArray =memoryBlockArray[:]
loopRuns = 0
while True:
    blocks = max(memoryBlockArray)
    maxIndex = memoryBlockArray.index(blocks)
    memoryBlockArray[maxIndex]=0
    for i in range(1,blocks+1):
        nextIndex = (maxIndex+i)%memoryBlockLen
        memoryBlockArray[nextIndex] +=1
    loopRuns+=1
    if loopArray == memoryBlockArray:
        break

print(loopRuns)
        


