"""
Day13
kubz113
"""


with open("day13.txt") as textFile:
    mappingInput = [line.replace(':','').split() for line in textFile]

intMappingInput = [list(map(int, line)) for line in mappingInput]

testList = [[0,3],[1,2],[4,4],[6,4]]

def immediateSeverity(scannerList):
    severity= 0
    d ={}
    for scanner in scannerList:
        d[scanner[0]] = scanner[1]

    lastScanner = max(d, key = int)
    for i in range(lastScanner+1):
        if i in d:
            if i%(2*(d[i]-1)) == 0:
                severity+= i*d[i]
    return severity



if immediateSeverity(testList) == 24:
    print("Test Passed")
else:
    print("Test Failed")

print(immediateSeverity(intMappingInput))


def safePassage(scannerList):
    d ={}
    for scanner in scannerList:
        d[scanner[0]] = scanner[1]
    lastScanner = max(d, key = int)
    safe = False
    delay = -1
    while safe !=True:
        delay+=1
        for i in range(lastScanner+1):
            if i in d:
                if (i+delay)%(2*(d[i]-1)) == 0:
                    break
            if i == lastScanner:
                safe = True
    return delay
        
if safePassage(testList) == 10:
    print("Test Passed")
else:
    print("Test Failed")

print(safePassage(intMappingInput))
