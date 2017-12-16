# -*- coding: utf-8 -*-
"""
Created on Tues Dec  12 10:30:23 2017

@author: kubz113
"""
import operator

operators = {'<' : operator.lt,
             '<=': operator.le,
             '==': operator.eq,
             '!=': operator.ne,
             '>': operator.gt,
             '>=': operator.ge}

with open("day8.txt") as f:
    steps = [line.split() for line in f]

highestValueEver = 0
values = {}
for i in range(len(steps)):
    if steps[i][0] not in values:
        values[steps[i][0]] = 0



for i in range(len(steps)):
    if operators[steps[i][5]](values[steps[i][4]], int(steps[i][6])):
        if steps[i][1] == "inc":
            values[steps[i][0]] += int(steps[i][2])
        else:
            values[steps[i][0]] -= int(steps[i][2])
        if values[steps[i][0]]> highestValueEver:
            highestValueEver = values[steps[i][0]]

print(max(values.values()))
print(highestValueEver)
