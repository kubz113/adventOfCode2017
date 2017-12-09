# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:18:26 2017

@author: kubz113
"""


goal = 347991

startDistance = int(goal**(1/2))
if(startDistance%2 == 0):
    startNumber = (startDistance+1)**2
else:
    startNumber = (startDistance+2)**2
    startDistance +=1
midpoint = int(startDistance/2)

curNumber = startNumber
curDistance = startDistance
subtract = True

while goal!= curNumber:
    curNumber -=1

    if(subtract):
        curDistance -=1
    else:
        curDistance +=1
    if(curDistance == midpoint or curDistance == startDistance):
        subtract = not subtract
    
print(curDistance)


"""Part Two"""
d = {(0,0):1}



segLen = 1

x = 0
y= 0
dx = 0
dy = -1
segPassed = 0

X=1000
Y=1000

for i in range(max(X, Y)**2):
    total = 0;
    if(i!=0):
        if((x-1, y+1) in d):
            total+=d[(x-1,y+1)]
        if((x-1, y) in d):
            total+=d[(x-1,y)]
        if((x-1, y-1) in d):
            total+=d[(x-1,y-1)]
        if((x, y+1) in d):
            total+=d[(x,y+1)]
        if((x, y-1) in d):
            total+=d[(x,y-1)]
        if((x+1, y+1) in d):
            total+=d[(x+1,y+1)]
        if((x+1, y) in d):
            total+=d[(x+1,y)]
        if((x+1, y-1) in d):
            total+=d[(x+1,y-1)]
        if total>347991:
            break
        d[(x,y)] = total
    if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
        dx, dy = -dy, dx
    if abs(x)>X/2 or abs(y)>Y/2:    # non-square
        dx, dy = -dy, dx            # change direction
        x, y = -y+dx, x+dy
    x, y = x+dx, y+dy

print(total)   
    
    
    
