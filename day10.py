# -*- coding: utf-8 -*-
"""
Created on Tues Dec  13 10:50:00 2017

@author: kubz113
"""

lengths = [106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36]

def testPartOne(testLengths, size, result):
    if knotHash(testLengths, size) == result:
        print(testLengths, " Test passed")
    else:
        print(testLengths, " Test failed")


def knotHash(lengthList, size):
    modifiedArray = list(range(size))
    pointer = 0
    leftOver = 0
    skipLevel = 0
    for i in range(len(lengthList)):
        if (pointer+lengthList[i]>=size):
            leftOver = (pointer+lengthList[i])-size
            tempArray = modifiedArray[pointer:]+modifiedArray[0:leftOver]
            tempArray = tempArray[::-1]
            modifiedArray[pointer:] = tempArray[0:(size-pointer)]
            modifiedArray[0:leftOver] = tempArray[(size-pointer):]
            if leftOver + skipLevel >= size:
                pointer = leftOver+skipLevel - size
            else:
                pointer = leftOver + skipLevel 
            skipLevel +=1
        else:
            tempArray = modifiedArray[pointer:pointer+lengthList[i]]
            tempArray = tempArray[::-1]
            modifiedArray[pointer:pointer+lengthList[i]] = tempArray[:]
            if lengthList[i]+pointer + skipLevel>=size:
                pointer = lengthList[i]+pointer + skipLevel - size
            else:
                pointer = lengthList[i]+pointer + skipLevel
            skipLevel +=1
        
    return modifiedArray[0]*modifiedArray[1]




testPartOne([3,4,1,5], 5, 12)
print(knotHash(lengths, 256))
    
