"""
Day 11
Kubz113
"""

directions = open("day11.txt", "r").read().split(',')

def shortestDist(dirs):
    north = 0
    south = 0
    east = 0
    west = 0

    for i in dirs:
        if i == 'n':
            north +=1
        elif i == 's':
            south +=1
        elif i == 'ne':
            north+=.5
            east+=.5
        elif i == 'nw':
            north +=.5
            west+=.5
        elif i == 'se':
            south +=.5
            east+=.5
        elif i == 'sw':
            south+=.5
            west+=.5

    return abs(north-south)+abs(east-west)


def shortestDistTest(dirs, result):
    if shortestDist(dirs)==result:
        print(dirs, " Test Passed")
    else:
        print(dirs, " Test Failed")

print(shortestDist(directions))

shortestDistTest(['ne','ne','ne'],3)
shortestDistTest(['se', 'sw', 'se', 'sw','sw'],3)



def longestDistReached(dirs):
    north = 0
    south = 0
    east = 0
    west = 0
    longest = 0

    for i in dirs:
        if i == 'n':
            north +=1
        elif i == 's':
            south +=1
        elif i == 'ne':
            north+=.5
            east+=.5
        elif i == 'nw':
            north +=.5
            west+=.5
        elif i == 'se':
            south +=.5
            east+=.5
        elif i == 'sw':
            south+=.5
            west+=.5
        if longest<abs(north-south)+abs(east-west):
            longest = abs(north-south)+abs(east-west)
    return longest

print(longestDistReached(directions))
