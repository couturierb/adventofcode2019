import math

file = open("aoc3.data", "r")

def goToR(value, wireArray):
    global x
    while value > 0:
        x += 1
        wireArray.append((x, y))
        value -= 1

def goToU(value, wireArray):
    global y
    while value > 0:
        y -= 1
        wireArray.append((x, y))
        value -= 1

def goToL(value, wireArray) :
    global x
    while value > 0:
        x -= 1
        wireArray.append((x, y))
        value -= 1

def goToD(value, wireArray) :
    global y
    while value > 0:
        y += 1
        wireArray.append((x, y))
        value -= 1

def createWire(wireInput) :
    wireArray = []
    for wire in wireInput:
        if (wire[:1] == 'R'):
            goToR(int(wire[1:]), wireArray)
        elif (wire[:1] == 'U'):
            goToU(int(wire[1:]), wireArray)
        elif (wire[:1] == 'L'):
            goToL(int(wire[1:]), wireArray)
        elif (wire[:1] == 'D'):
            goToD(int(wire[1:]), wireArray)
    return wireArray
    
wireInput1 = [one for one in file.readline().split(',')]
wireInput2 = [one for one in file.readline().split(',')]
x = 0
y = 0
wireArray1 = createWire(wireInput1)
x = 0
y = 0
wireArray2 = createWire(wireInput2)

foundedValue = 0
for index, wire in enumerate(wireArray1):
    try :
        distance = wireArray2.index(wire) + index + 2
        if foundedValue == 0 or distance < foundedValue:
            foundedValue = distance
    except:
        pass

print("distance: " + str(foundedValue))