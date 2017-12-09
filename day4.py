# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:30:23 2017

@author: kubz113
"""

text_file = open("day4.txt", "r")

lines = list(map(str.split, text_file))
notValid= 0

for line in lines:
    for word in line:
        num = line.count(word)
        if num>1:
            notValid+=1
            break

print(len(lines)-notValid)


notValid2 = 0
for line in lines:
    for word in line:
        num = line.count(word)
        if num>1:
            notValid2+=1
            break
        invalid = False
        for wordTwo in line:
            if word != wordTwo:
                charWord = sorted(list(word))
                charWordTwo = sorted(list(wordTwo))
                if charWord == charWordTwo:
                    invalid = True
                    break
        if invalid:
            notValid2+=1
            break
print(len(lines)-notValid2)
        
            
            
 
