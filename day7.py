# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:02:47 2017

@author: jakub
"""
str = open('day7.txt', 'r').read()
str = str.replace(',', '')
compareList = str.split()

with open("day7.txt") as textFile:
    lines = [line.replace(',', '').split() for line in textFile]
    
    

found = False
base=""
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if j !=1:
            if compareList.count(lines[i][j])==1:
                base = lines[i][j]
                found = True
                break
    if found:
        break
    
    
print(base)             
            
            
with open("day7.txt") as textFile:
    stacks = [line.replace(',', '').replace('->', '').split() for line in textFile]
    
print(stacks)