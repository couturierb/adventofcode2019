from Draw import draw

class Grid() :
    def __init__(self):
        self.bio = {}
        self.bioNext = {}
        self.outerGrid = None
        self.innerGrid = None
        for y in range(0, 5) :
            for x in range(0, 5) :
                if not (x == 2 and y == 2) :
                    self.bio[(x, y)] = '.'

    def setInnerGrid(self, innerGrid) :
        if self.innerGrid == None :
            innerGrid.name = self.name + 1
            self.innerGrid = innerGrid
            innerGrid.setOuterGrid(self)

    def setOuterGrid(self, outerGrid) :
        if self.outerGrid == None :
            outerGrid.name = self.name - 1
            self.outerGrid = outerGrid
            outerGrid.setInnerGrid(self)

    def initBase(self) :
        self.name = 0
        y = 0
        file = open("aoc24.data", "r")
        for line in file.readlines() :
            for x in range(0, 5) :
                if not (x == 2 and y == 2) :
                    self.bio[x, y] = line[x]
            y += 1

    def __getInnerVoisins__(self, keys) :
        if self.innerGrid == None : return []
        voisins = []
        if keys[0] == 1 and keys[1] == 2 : # gauche
            voisins = [v for k, v in self.innerGrid.bio.items() if k[0] == 0]
        elif keys[0] == 3 and keys[1] == 2 : # droite
            voisins = [v for k, v in self.innerGrid.bio.items() if k[0] == 4]
        elif keys[0] == 2 and keys[1] == 1 : # haut
            voisins = [v for k, v in self.innerGrid.bio.items() if k[1] == 0]
        elif keys[0] == 2 and keys[1] == 3 : # bas
            voisins = [v for k, v in self.innerGrid.bio.items() if k[1] == 4]
        return voisins

    def __getOuterVoisins__(self, keys) :
        if self.outerGrid == None : return []
        voisins = []
        if keys[0] == 0 : # gauche
            voisins.append(self.outerGrid.bio.get((1, 2), ''))
        if keys[0] == 4 : # droite
            voisins.append(self.outerGrid.bio.get((3, 2), ''))
        if keys[1] == 0 : # haut
            voisins.append(self.outerGrid.bio.get((2, 1), ''))
        if keys[1] == 4 : # bas
            voisins.append(self.outerGrid.bio.get((2, 3), ''))
        return voisins

    def generate(self) :
        self.bioNext = self.bio.copy()
        for keys, value in self.bio.items() :
            voisins = []
            voisins.append(self.bio.get((keys[0]-1, keys[1]), ''))
            voisins.append(self.bio.get((keys[0]+1, keys[1]), ''))
            voisins.append(self.bio.get((keys[0], keys[1]-1), ''))
            voisins.append(self.bio.get((keys[0], keys[1]+1), ''))
            voisins += self.__getOuterVoisins__(keys)
            voisins += self.__getInnerVoisins__(keys)

            bugs = len([v for v in voisins if v == '#'])
            if value == '#' and not bugs == 1 : self.bioNext[keys] = '.'
            if value == '.' and (bugs == 1 or bugs == 2) : self.bioNext[keys] = '#'

    def apply(self) :
        self.bio = self.bioNext

    def checkInnergrid(self) :
        if self.innerGrid == None :
            bugs = [bug for bug in self.bio.values() if bug == '#']
            if len(bugs) > 0 :
                newGrid = Grid()
                self.setInnerGrid(newGrid)
                return newGrid

    def checkOuterGrid(self) :
        if self.outerGrid == None :
            bugs = [bug for bug in self.bio.values() if bug == '#']
            if len(bugs) > 0 :
                newGrid = Grid()
                self.setOuterGrid(newGrid)
                return newGrid

grids = []

grid = Grid()
grid.initBase()
grids.append(grid)
   
innerGrid = Grid()
grid.setInnerGrid(innerGrid)
grids.append(innerGrid)

outerGrid = Grid()
grid.setOuterGrid(outerGrid)
grids.append(outerGrid)

for i in range(0, 200) :
    for grid in grids :
        grid.generate()
    
    newGrids = []
    for grid in grids :
        grid.apply()
        newInner = grid.checkInnergrid()
        if not newInner == None : newGrids.append(newInner)
        newOuter = grid.checkOuterGrid()
        if not newOuter == None : newGrids.append(newOuter)
    grids = grids + newGrids

    # print("step " + str(i+1))
    # grids = sorted(grids, key=lambda t: t.name)
    # for grid in grids :
    #     print(grid.name, end='  ')
    #     draw(grid.bio)

howMany = 0
for grid in grids :
    # grids = sorted(grids, key=lambda t: t.name)
    # print(reduce(lambda a,b: b == '#', grid.bio.values()))
    howMany += len([v for v in grid.bio.values() if v is '#'])

print(howMany)