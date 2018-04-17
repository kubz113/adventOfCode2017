#Day 18
#kubz113

with open("day18test.txt") as textFile:
    instructionInput = [line.split() for line in textFile]

instructionIndex = 0

breakLoop = False
registers={}  

class RecoveredSound(Exception): pass
    

def snd(inputList):
    global instructionIndex
    instructionIndex+=1
    registers[inputList[0]][1] = registers[inputList[0]][0]
    

def setRegister(inputList):
    global instructionIndex
    if inputList[1].isalpha():
        registers[inputList[0]][0] = registers[inputList[1]][0]
    else:
        registers[inputList[0]][0] = int(inputList[1])
    instructionIndex+=1

def addValueToRegister(inputList):
    global instructionIndex
    if inputList[1].isalpha():
        registers[inputList[0]][0] += registers[inputList[1]][0]
    else:
        registers[inputList[0]][0] += int(inputList[1])
    instructionIndex+=1

def multiplyRegister(inputList):
    global instructionIndex
    if inputList[1].isalpha():
        registers[inputList[0]][0] *= registers[inputList[1]][0]
    else:
        registers[inputList[0]][0] *= int(inputList[1])
    instructionIndex+=1

def modulosRegister(inputList):
    global instructionIndex
    if inputList[1].isalpha():
        registers[inputList[0]][0]= registers[inputList[0]][0]% registers[inputList[1]][0]
    else:
        registers[inputList[0]][1]= registers[inputList[0]][0]%int(inputList[1])
    instructionIndex+=1

def recoverLastSound(inputList):
    global instructionIndex
    global breakLoop
    currentVal =  registers[inputList[0]][0]
    if not currentVal == 0:
        print(registers[inputList[0]][1])
        breakLoop = True
    else:
        instructionIndex +=1

def jumpRegister(inputList):
    global instructionIndex
    if registers[inputList[0]][0]!=0:
        if len(inputList[1])==1 and inputList[1].isaplha():
            instructionIndex+= registers[inputList[1]][0]
        else:
            instructionIndex+=int(inputList[1])
    else:
        instructionIndex+=1

functionList = {'snd': snd,
                'set': setRegister,
                'add' : addValueToRegister,
                'mul' : multiplyRegister,
                'mod' : modulosRegister,
                'rcv' : recoverLastSound,
                'jgz' : jumpRegister}

if __name__== "__main__":
   
    
    instructionCount = len(instructionInput)
    
    while instructionIndex<instructionCount:
        
        currentInstruction = instructionInput[instructionIndex]
        currentFun = currentInstruction[0]
        print(currentFun)
        if not (currentInstruction[1]   in registers):
            registers[currentInstruction[1]] = [0,0]
        functionList[currentFun](currentInstruction[1:])
        if breakLoop:
            break
            
      
    print(registers)
