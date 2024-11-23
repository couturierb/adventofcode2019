from Intcode2 import Intcode
from Draw import draw

file = open("aoc19.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }

def findArea(x, y) :
    LARGEUR = 99
    intcode = Intcode(program.copy())
    intcode.setInputs([x+LARGEUR, y])
    abs = intcode.run()
    intcode = Intcode(program.copy())
    intcode.setInputs([x, y+LARGEUR])
    ord = intcode.run()
    if abs == 1 and ord == 1:
        print("x : " + str(x) + " - y : " + str(y))
        return True

    return False

grid = {}
X_COUNT = 1000
x = X_COUNT
y = 1500
beamFounded = False
while True :
    intcode = Intcode(program.copy())
    intcode.setInputs([x, y])
    out = intcode.run()
    if out == 1:
        grid[(x, y)] = "#"
        beamFounded = True
        if findArea(x, y) :
            break
    else :
        grid[(x, y)] = "."
        if beamFounded :
            x = X_COUNT
            y += 1
            beamFounded = False

    x += 1

# draw(grid)