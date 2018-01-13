"""
AoC Day 15
kubz113
"""

genANum = 116
genBNum = 299

genANumTwo = 116
genBNumTwo = 299


genAFactor = 16807
genBFactor = 48271
matching = 0

for i in range(40000001):
  if i%1000000 == 0:
    print(i)
  genABin = format(genANum , '016b')
  genBBin = format(genBNum, '016b')
  genANum = (genANum*genAFactor)%2147483647
  genBNum=(genBNum * genBFactor)%2147483647
  if genABin[-16:] == genBBin[-16:]:
      matching+=1
print(matching)


genAReturnVals =[]
genBReturnVals = []

while len(genAReturnVals)<5000001 or len(genBReturnVals)<5000001:
  if genANumTwo%4 == 0:
    genAReturnVals.append(format(genANumTwo , 'b'))
  if genBNumTwo%8 == 0:
    genBReturnVals.append(format(genBNum, 'b'))
  genANumTwo = (genANumTwo*genAFactor)%2147483647
  genBNumTwo=(genBNumTwo * genBFactor)%2147483647

matchingTwo = 0
for i in range(5000000):
  if genAReturnVals[i][-16:] == genBReturnVals[i][-16:]:
    matchingTwo+=1

print(matchingTwo)
