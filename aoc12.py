import math
import functools

file = open("aoc12.data", "r")

moonNameNumber = 0

class Moon :
    def __init__(self, line) :
        global moonNameNumber
        self.isXOk = False
        self.velocityX = 0
        self.velocityY = 0
        self.velocityZ = 0
        self.x = int(line[0].split('=')[1])
        self.initialX = self.x
        self.y = int(line[1].split('=')[1])
        self.initialY = self.y
        self.z = int(line[2].split('=')[1])
        self.initialZ = self.z
        self.name = "moon " + str(moonNameNumber)
        self.cycleX = []
        self.cycleY = []
        self.cycleZ = []
        moonNameNumber += 1

    def __str__(self) :
        return "pos = " + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) \
            + ' vel = ' + str(self.velocityX) + ', ' + str(self.velocityY) + ', ' + str(self.velocityZ)

    def applyGravity(self, moons) :
        for moon in moons : 
            if moon.x > self.x : self.velocityX += 1
            elif moon.x < self.x : self.velocityX += -1

            if moon.y > self.y : self.velocityY += 1
            elif moon.y < self.y : self.velocityY += -1

            if moon.z > self.z : self.velocityZ += 1
            elif moon.z < self.z : self.velocityZ += -1

    def applyVelocity(self) :
        self.x += self.velocityX
        self.y += self.velocityY
        self.z += self.velocityZ

    def countCycle(self, currentStep) :
        if self.x  == self.initialX and self.velocityX == 0 :
            self.cycleX.append(currentStep + 1)

        if self.y  == self.initialY and self.velocityY == 0 :
            self.cycleY.append(currentStep + 1)

        if self.z  == self.initialZ and self.velocityZ == 0 :
            self.cycleZ.append(currentStep + 1)

def step1() :
    moons = []
    for line in file.read().replace('<', '').replace('>', '').splitlines() :
        moons.append(Moon(line.split(',')))

    for i in range(0, 1000) :
        for moon in moons :
            moon.applyGravity(moons)

        for moon in moons : 
            moon.applyVelocity()
            # print(moon)

    energy = 0 
    for moon in moons :
        pot = math.fabs(moon.x) + math.fabs(moon.y) + math.fabs(moon.z)
        kin = math.fabs(moon.velocityX) + math.fabs(moon.velocityY) + math.fabs(moon.velocityZ)
        energy += pot * kin

    print(energy)

def findCycles(moons) :
    cyclesX = [v for v in moons[0].cycleX if v in moons[1].cycleX and v in moons[2].cycleX and v in moons[3].cycleX]
    cyclesY = [v for v in moons[0].cycleY if v in moons[1].cycleY and v in moons[2].cycleY and v in moons[3].cycleY]
    cyclesZ = [v for v in moons[0].cycleZ if v in moons[1].cycleZ and v in moons[2].cycleZ and v in moons[3].cycleZ]
    if cyclesX and cyclesY and cyclesZ :
        return [cyclesX[0], cyclesY[0], cyclesZ[0]]
   
def findAllCycle(numbers) :
    return [v for v in moons[0].cycleZ if v in moons[1].cycleZ and v in moons[2].cycleZ and v in moons[3].cycleZ]

def findMultiple(numbers) :
    maxNumber = functools.reduce(lambda a,b : a*b, numbers)
    minNumber = min(numbers)
    for i in range(numbers[2], maxNumber, numbers[2]) :
        if i % numbers[0] == 0 and i % numbers[1] == 0 and i % numbers[2] == 0 :
            print("multiple : " + str(i))
            break

def step2() :
    moons = []
    for line in file.read().replace('<', '').replace('>', '').splitlines() :
        moons.append(Moon(line.split(',')))

    founded = []
    i = 0
    while not founded :
        for moon in moons :
            moon.applyGravity(moons)

        for moon in moons : 
            moon.applyVelocity()
            moon.countCycle(i)

        if not founded :
            founded = findCycles(moons)

        i += 1

    print(founded)
    findMultiple(founded)

step2()