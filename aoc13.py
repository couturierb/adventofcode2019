from Intcode import Intcode
from Draw import draw

lines = open("aoc13.data", "r").readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)

def whichDirection(grid) :
    ball = [key[0]  for (key, value) in grid.items() if value == 4]
    paddle = [key[0]  for (key, value) in grid.items() if value == 3]
    if len(ball) == 0 or len(paddle) == 0 :
        return 0
    elif ball[0] > paddle[0] :
        return 1
    elif ball[0] < paddle[0] :
        return -1
    else :
        return 0

grid = {}
while not intcode.isTerminated() :
    x = intcode.run(whichDirection(grid))
    y = intcode.run(whichDirection(grid))
    tileId = intcode.run(whichDirection(grid))
    if x == None or y == None or tileId == None : break
    grid[(x, y)] = tileId

draw(grid)
print(grid[(-1, 0)])


