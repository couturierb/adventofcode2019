from Intcode import Intcode
from os import system

def moved(isEnd) :
    global x
    global y
    if currentDirection == N :
        y -= 1
    elif currentDirection == S :
        y += 1
    elif currentDirection == O  :
        x -= 1
    elif currentDirection == E :
        x += 1

    if isEnd :
        robot[(x, y)] = 'o'
    else :
        robot[(x, y)] = '.'

def mur() :
    if currentDirection == N :
        robot[(x, y-1)] = '#'
    elif currentDirection == S :
        robot[(x, y+1)] = '#'
    elif currentDirection == O :
        robot[(x-1, y)] = '#'
    elif currentDirection == E :
        robot[(x+1, y)] = '#'

def changeDirection() :
    global currentDirection
    if robot.get((x, y-1), '') == '' :
        currentDirection = N
    elif robot.get((x, y+1), '') == '' :
        currentDirection = S
    elif robot.get((x-1, y), '') == '' :
        currentDirection = O
    elif robot.get((x+1, y), '') == '' :
        currentDirection = E
    elif robot.get((x, y-1), '') == '.' or robot.get((x, y-1), '') == 'x' :
        currentDirection = N
    elif robot.get((x, y+1), '') == '.' or robot.get((x, y+1), '') == 'x' :
        currentDirection = S
    elif robot.get((x-1, y), '') == '.' or robot.get((x-1, y), '') == 'x' :
        currentDirection = O
    elif robot.get((x+1, y), '') == '.' or robot.get((x+1, y), '') == 'x' :
        currentDirection = E


def draw() :
    print('-------------------------------------')
    xValues = [key[0] for key in robot]
    yValues = [key[1] for key in robot]
    minX = min(xValues)
    minY = min(yValues)
    maxX = max(xValues)
    maxY = max(yValues)

    for j in range(minY, maxY+1) :
        for i in range(minX, maxX+1) :
            if x == i and y == j :
                print('D', end='')
            else :
                print(robot.get((i, j), ' '), end='')
        print('')
    
file = open("aoc15.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)
N = 1
S = 2
O = 3
E = 4
x = 0
y = 0
currentDirection = N
    # direction = [1, 4, 2, 3]
robot = {(x, y) : 'x'}

while True :
    result = intcode.run(currentDirection)
    if result == 0 :
        mur()
    elif result == 1 :
        moved(False)
    elif result == 2 :
        moved(True)
        break

    changeDirection()
    system('clear')
    draw()
