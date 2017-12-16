# -*- coding: utf-8 -*-
"""
Created on Tues Dec  12 12:40:00 2017

@author: kubz113
"""

def test(test, correctOutput):
    if streamProcessing(test) == correctOutput:
        print(test, " passed")
    else:
        print(test, " failed")



def streamProcessing(stream):
    total = 0
    currentPoint = 0
    garbage = False
    skip = False
    for i in range(len(stream)):
        if not skip:
            if stream[i] == "!":
                skip = True
            elif not garbage:
                if stream[i] == "<":
                    garbage = True
                elif stream[i] == "{":
                    currentPoint +=1
                    total +=currentPoint
                elif stream[i] == "}":
                    currentPoint -= 1
                elif stream[i] == "!":
                    skip = True
            else:
                if stream[i] == ">":
                    garbage = False
        else:
            skip = False
    return total


text_file = open("day9.txt", "r").read()

test("{}", 1)

test("{{{}}}", 6)

test("{<a>,<a>,<a>,<a>}", 1)

test("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9)

test("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)

test("{<{},{},{{}}>}", 1)

test("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9)

print(streamProcessing(text_file))


def removeGarbage(stream):
    totalRemoved = 0
    garbage = False
    skip = False
    for i in range(len(stream)):
        if not skip:
            if stream[i] == "!":
                skip = True
            elif not garbage:
                if stream[i] == "<":
                    garbage = True                
            else:
                if stream[i] == ">":
                    garbage = False
                else:
                    totalRemoved +=1
        else:
            skip = False
    return totalRemoved
                    
def testRemove(test, correctOutput):
    if removeGarbage(test) == correctOutput:
        print(test, " passed")
    else:
        print(test, " failed")


testRemove("<>", 0)

testRemove("<random characters>", 17)

testRemove("<<<<>", 3)

testRemove("<!!>", 0)

testRemove("<!!!>>", 0)

testRemove("<{oqi!a,<{i<a>", 10)

print(removeGarbage(text_file))
