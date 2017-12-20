"""
Day12
Kubz113
"""


with open("day12.txt") as textFile:
    mappingInput = [line.replace('<->','').replace(',','').split() for line in textFile]

intMappingInput = [list(map(int, line)) for line in mappingInput]




def zeroNetworkSize(mapping):
    zeroNetwork = mapping[0][:]
    for i in zeroNetwork:
        if i !=0:
            for j in range(1,len(mapping[i])):
                if not (mapping[i][j] in zeroNetwork):
                    zeroNetwork.append(mapping[i][j])

            
    return len(zeroNetwork)

testList = [[0,2], [1,1], [2,0,3,4], [3,2,4],[4,2,3,6],[5,6],[6,4,5]]


print(zeroNetworkSize(testList))

print(zeroNetworkSize(intMappingInput))

def numNetworks(mapping):
    networks = 0
    foundPrograms = []
    currentNetwork = []
    notInNetwork = list(range(len(mapping)))
    for y in range(len(mapping)):
        if not (y in foundPrograms):
            foundPrograms.append(y)           
            currentNetwork = mapping[y][:]
            for x in currentNetwork:
                if not x in foundPrograms:
                    foundPrograms.append(x)
            for i in currentNetwork:
                if i !=0:
                    for j in range(1,len(mapping[i])):
                        if not (mapping[i][j] in currentNetwork):
                            currentNetwork.append(mapping[i][j])
                            foundPrograms.append(mapping[i][j])
                        
            networks+=1
    return networks

print(numNetworks(testList))
print(numNetworks(intMappingInput))
        
