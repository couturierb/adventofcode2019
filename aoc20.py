from Draw import draw
from threading import Thread

class Graph :
    nodes = {}
    labyrinthe = {}

    def setLabyrintheTile(self, fileInput, x, y) :
        self.labyrinthe[(x, y)] = fileInput[y][x]
        if fileInput[y][x].isalpha() and x > 0 and x < len(fileInput[0]) - 1 and y > 0 and y < len(fileInput) - 1 :
            self.__createNode__(fileInput, x, y)

    def searchPath(self, point = None, labyrinthe = None, step = 0, nodeTravel = []) :
        if point == None : point = self.nodes['AA'][0]
        if labyrinthe == None : labyrinthe = self.labyrinthe
        while True :
            labyrinthe[point] = '#'
            # draw(labyrinthe)

            nodeName = [k for k, v in self.nodes.items() if point in v]
            if len(nodeName) == 1 and not nodeName[0] == 'AA':
                name = nodeName[0]
                if name == 'ZZ' :
                    print(name + ' ' + str(step) + ' ' + str(nodeTravel))
                    break
                portalPoint = self.nodes[name][0]
                if portalPoint == point : portalPoint = self.nodes[name][1]
                nodeTravel.append(name)
                point = portalPoint
                step += 1
            
            voisinsPoint = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
            voisinsPoint = [p for p in voisinsPoint if labyrinthe.get(p, '#') == '.']
            if len(voisinsPoint) == 0 :
                break
            else :
                point = voisinsPoint.pop(0)
                step += 1
    
                for voisinPoint in voisinsPoint :
                    self.searchPath(voisinPoint, labyrinthe.copy(), step, nodeTravel.copy())
                   
    def searchPathOld(self, point = None, labyrinthe = None, step = 0, nodeTravel = []) :
        if point == None : point = self.nodes['AA'][0]
        if labyrinthe == None : labyrinthe = self.labyrinthe.copy()
        labyrinthe[point] = '#'
        voisinsPoint = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
        for voisinPoint in voisinsPoint :
            if labyrinthe.get(voisinPoint, '#') == '.' :
                nodeName = [k for k, v in self.nodes.items() if voisinPoint in v]
                if len(nodeName) == 1 :
                    name = nodeName[0]
                    if name == 'ZZ' :
                        print(name + ' ' + str(step + 1) + ' ' + str(nodeTravel))
                        # draw(labyrinthe)
                        break
                    portalPoint = self.nodes[name][0]
                    if portalPoint == voisinPoint : 
                        portalPoint = self.nodes[name][1]
                    nodeTravel.append(name)
                    self.searchPath(portalPoint, labyrinthe.copy(), step + 2, nodeTravel)
                elif len(nodeName) > 1 :
                    print('NANI ? ')
                    print(nodeName)
                    break
                elif len(nodeName) == 0 :
                    # draw(labyrinthe)
                    voisinsPoint.remove(voisinPoint)
                    voisinsPoint.append(((voisinPoint[0] - point[0]) * 2, ))
                    self.searchPath(voisinPoint, labyrinthe.copy(), step + 1, nodeTravel)

    def __str__(self) :
        draw(self.labyrinthe)
        for key, value in self.nodes.items() :
            print(key + str(value))
        return ''

    def __addNode__(self, nodeName, nodePoint) :
        if nodeName in self.nodes :
            if not nodePoint in self.nodes[nodeName] :
                self.nodes[nodeName].append(nodePoint)
        else : 
            self.nodes[nodeName] = [nodePoint]

    def __createNode__(self, fileInput, x, y) :
        name = fileInput[y][x]
        point = None

        # top
        voisin = fileInput[y - 1][x]
        if voisin.isalpha() :
            name = voisin + name
            point = (x, y+1) if fileInput[y+1][x] == '.' else (x, y-2)

        # bot
        voisin = fileInput[y + 1][x]
        if voisin.isalpha() :
            name += voisin
            point = (x, y-1) if fileInput[y-1][x] == '.' else (x, y+2)

        # right
        voisin = fileInput[y][x + 1]
        if voisin.isalpha() :
            name += voisin
            point = (x - 1, y) if fileInput[y][x-1] == '.' else (x + 2, y)

        # left
        voisin = fileInput[y][x - 1]
        if voisin.isalpha() :
            name = voisin + name
            point = (x + 1, y) if fileInput[y][x+1] == '.' else (x - 2, y)

        self.__addNode__(name, point)

def createGraph():
    fileInput = open("aoc20.data", "r").read().splitlines()
    graph = Graph()

    for y in range(len(fileInput)) :
        for x in range(len(fileInput[0])) :
            graph.setLabyrintheTile(fileInput, x, y)
            
    return graph


graph = createGraph()
print(graph)
graph.searchPath()
