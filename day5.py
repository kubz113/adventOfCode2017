# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:30:23 2017

@author: kubz113
"""

with open("day5.txt") as f:
    steps = [int(line) for line in f]
    

steps2 = steps[:]
i = 0
jumps = 0
while i<len(steps) and i>=0:
    increment = steps[i]
    steps[i] = 1 + increment
    i+=increment
    jumps +=1

print(jumps)

j = 0
jumps2 = 0
while j<len(steps2) and j>=0:
    increment = steps2[j]
    if increment <3:
        steps2[j] = 1 + increment
    else:
        steps2[j] = increment-1
    j+=increment
    jumps2 +=1

print(jumps2)
