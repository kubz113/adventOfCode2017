"""
AoC Day 16
kubz113
fajkhpodibmlcgen
"""
with open("day16.txt") as textFile:
    danceMoves = [x.split(',') for x in textFile]

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p']
endStates = []
cycles = 0
while True:
    for i in danceMoves[0]:
        tempMoves = []
        if i[0] == 's':
            spin = int(i[1:])
            programs= programs[-spin:] + programs[:-spin]

        elif i[0] == 'x':
            instruct = i[1:].split('/')
            A = int(instruct[0])
            B = int(instruct[1])
            programs[A], programs[B] = programs[B], programs[A]
        elif i[0] == 'p':
            A = programs.index(i[1])
            B = programs.index(i[3])
            programs[A] = i[3]
            programs[B] = i[1]
    cycles+=1
    if programs in endStates:
        break
    endStates.append(programs[:])


print(endStates[1000000000%cycles+1])
