from Intcode import Intcode

lines = open("aoc11.data", "r").readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)
# BLACK = 0
# WHITE = 1
x = y = directionX = 0
color = 1
directionY = -1
painted = {(x, y) : color}

while not intcode.isTerminated() :
    colorToPaint = intcode.run(color)
    directionShouldTurn = intcode.run(color)

    painted[(x, y)] = colorToPaint
    move(directionShouldTurn)
    color = painted.get((x, y), 0)

xValues = [key[0] for key in painted]
yValues = [key[1] for key in painted]
minX = min(xValues)
minY = min(yValues)
maxX = max(xValues)
maxY = max(yValues)

for j in range(minY, maxY+1) :
    for i in range(minX, maxX+1) :
        if painted.get((i, j), 0) == 1 :
            print('#', end='')
        else :
            print(' ', end='')
    print('')
    