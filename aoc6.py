def searchValue(value):
    global values
    if isinstance(values[value], int) :
        return values[value]
    else :
        values[value] = searchValue(values[value]) + 1
        return values[value]

def step1():
    global values
    for line in file.read().splitlines() :
        lineArray = line.split(')')
        if lineArray[0] == "COM" :
            values[lineArray[1]] = 1
        else :
            values[lineArray[1]] = lineArray[0]

    count = 0
    for key, value in values.items() :
        if isinstance(value, str) :
            values[key] = searchValue(value) + 1
            count += values[key]
        else :
            count += value

    print(count)

def searchPath(point) :
    if point == "COM" :
        return []
    else :
        return [point] + searchPath(values[point])

def step2():
    global values
    for line in file.read().splitlines() :
        lineArray = line.split(')')
        values[lineArray[1]] = lineArray[0]

    pathToYou = searchPath(values["YOU"])   
    pathToSan = searchPath(values["SAN"])
    valueIntersect = [value for value in pathToYou if value in pathToSan][0]
    lenYou = len(pathToYou[:pathToYou.index(valueIntersect)])
    lenSan = len(pathToSan[:pathToSan.index(valueIntersect)])
    print (lenSan + lenYou)

    # print(pathToYou.index(valueIntersect))
    # print(pathToSan.index(valueIntersect))

file = open("/Users/myzuno/Google Drive/dev/adventOfCode/aoc6.data", "r")
values = {}
# step1()
step2()
#  < 491
# != 443

# 453 
# 467
# 479
# 445