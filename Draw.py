from os import system

def draw(grid) :
    print('-------------------------------------')
    xValues = [key[0] for key in grid]
    yValues = [key[1] for key in grid]
    minX = min(xValues)
    minY = min(yValues)
    maxX = max(xValues)
    maxY = max(yValues)

    printedStr = ''
    for j in range(minY, maxY+1) :
        for i in range(minX, maxX+1) :
            printedStr += grid.get((i, j), ' ')
        printedStr += '\n'
    print(printedStr)