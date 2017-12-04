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

dx = 1
dy = 0

segLen = 1

x = 0
y= 0 
segPassed = 0

for i in range(0,goal):
    total = 0
    x+=dx
    y+=dy
    segPassed+=1
    
    #Searhing the dictionary for already calcualted neighbors
    if(d.get(x-1, y+1) !=None):
        total+=d.get(x-1,y+1)
    if(d.get(x-1, y) !=None):
        total+=d.get(x-1,y)
    if(d.get(x-1, y-1) !=None):
        total+=d.get(x-1,y-1)
    if(d.get(x, y+1) !=None):
        total+=d.get(x,y+1)
    if(d.get(x, y-1) !=None):
        total+=d.get(x,y+1)
    if(d.get(x+1, y+1) !=None):
        total+=d.get(x+1,y+1)
    if(d.get(x+1, y) !=None):
        total+=d.get(x+1,y)
    if(d.get(x+1, y-1) !=None):
        total+=d.get(x+1,y-1)
    if total>goal:
        break
    d[(x,y)] = total
    
    
    if(segPassed == segLen):
        segPassed = 0
        buffer = dx
        dx = -dy
        dy = dx
        if(dy == 0):
            segLen+=1
    
    
print(total)   
    
    
    