from Draw import draw
from threading import Thread

def createLabyrinthe():
    fileInput = open("aoc18.data", "r").read().splitlines()
    labyrinthe = {}

    for x in range(len(fileInput[0])) :
        for y in range(len(fileInput)) :
            labyrinthe[(x, y)] = fileInput[y][x]

    return labyrinthe

def searchReachableKeys(labyrinthe, point, keys, step=0) :
    labyrinthe[point] = '#'
    voisinsPoint = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    for voisinPoint in voisinsPoint :
        voisin = labyrinthe.get(voisinPoint, '#')
        if voisin == '.' : 
            searchReachableKeys(labyrinthe, voisinPoint, keys, step + 1)
        elif (ord(voisin) >= 97 and ord(voisin) <= 122) :
            keys.append((voisinPoint, voisin, step + 1))

class Path(Thread) :

    def __init__(self, labyrinthe, point, pathFinded, step=0) :
        Thread.__init__(self)
        self.labyrinthe = labyrinthe
        self.point = point
        self.pathFinded = pathFinded
        self.step = step

    def run(self) :
        self.labyrinthe[self.point] = '@'

        reachableKeys = []
        searchReachableKeys(self.labyrinthe.copy(), self.point, reachableKeys)
        if len(reachableKeys) == 0 :
            self.pathFinded.append(self.step)
            # print(self.step)
            return

        for reachableKey in reachableKeys :
            newLabyrinthe = self.labyrinthe.copy()
            newLabyrinthe[reachableKey[0]] = '.'
            doorPoint = [key for key, value in newLabyrinthe.items() if value == reachableKey[1].upper()]
            if len(doorPoint) > 0 : newLabyrinthe[doorPoint[0]] = '.'
    
            newLabyrinthe[self.point] = '.'
            path = Path(newLabyrinthe, reachableKey[0], self.pathFinded, reachableKey[2] + self.step)
            path.start()
            path.join()

def searchPath(labyrinthe, point, pathFinded, step=0) :
    labyrinthe[point] = '@'
    # draw(labyrinthe)

    reachableKeys = []
    searchReachableKeys(labyrinthe.copy(), point, reachableKeys)
    if len(reachableKeys) == 0 :
        pathFinded.append(step)
        return

    for reachableKey in reachableKeys :
        newLabyrinthe = labyrinthe.copy()
        newLabyrinthe[reachableKey[0]] = '.'
        doorPoint = [key for key, value in newLabyrinthe.items() if value == reachableKey[1].upper()]
        # Plusierurs portes ?
        if len(doorPoint) > 0 : newLabyrinthe[doorPoint[0]] = '.'
    
        newLabyrinthe[point] = '.'
        searchPath(newLabyrinthe, reachableKey[0], pathFinded, reachableKey[2] + step)

def searchPathV2(labyrinthe, point, pathFinded, step=0) :
    reachableKeys = []
    searchReachableKeys(labyrinthe.copy(), point, reachableKeys)
    if len(reachableKeys) == 0 :
        pathFinded.append(step)
        return

    for reachableKey in reachableKeys :
        newLabyrinthe = labyrinthe.copy()
        newLabyrinthe[reachableKey[0]] = '.'
        doorPoint = [key for key, value in newLabyrinthe.items() if value == reachableKey[1].upper()]
        # Plusierurs portes ?
        if len(doorPoint) > 0 : newLabyrinthe[doorPoint[0]] = '.'
    
        newLabyrinthe[point] = '.'
        searchPath(newLabyrinthe, reachableKey[0], pathFinded, reachableKey[2] + step)

def step1() :
    labyrinthe = createLabyrinthe()

    playerPoint = [k for k, v in labyrinthe.items() if v == '@'][0]
    pathFinded = []
  
    # searchPath(labyrinthe, playerPoint, pathFinded)

    path = Path(labyrinthe, playerPoint, pathFinded)
    path.start()
    path.join()

    print('min : ' + str(min(pathFinded)))

step1()