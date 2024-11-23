import math

file = open("aoc10.data", "r")

class Asteroid() :
    def __init__(self, x, y) :
        self.voisins = {}
        self.x = x
        self.y = y

    def scan(self, espace) :
        for asteroid in espace: 
            if asteroid.x == self.x and asteroid.y == self.y :
                continue

            angle = math.atan2(asteroid.x - self.x, self.y - asteroid.y) * 180 / math.pi
            if angle < 0 : angle = angle + 360
            if angle in self.voisins :
                distanceVoisin = math.fabs(self.voisins[angle].x - self.x) + math.fabs(self.voisins[angle].y - self.y)
                distanceAsteroid = math.fabs(asteroid.x - self.x) + math.fabs(asteroid.y - self.y)
                if distanceAsteroid < distanceVoisin :
                    self.voisins[angle] = asteroid
            else :
                self.voisins[angle] = asteroid
            
        # print("asteroid " + str(self.x) + "-" + str(self.y) + " can see : " + str(count))

    def trier(self) :
        self.voisins = sorted(self.voisins.items(), key=lambda t: t[0])

def start() :
    y = 0 
    espace = []
    base = None
    for line in file.readlines() :
        for x in range(0, len(line) - 1) :
            if line[x] == "#" :
                asteroid = Asteroid(x, y)
                espace.append(asteroid)
                if x == 23 and y == 19 :
                # if x == 8 and y == 3 :
                    base = asteroid
        y += 1

    base.scan(espace)
    base.trier()
    print(base)

start()
# print(math.atan2(0, 3)  * 180 / math.pi)
# print(math.atan2(1, 0) * 180 / math.pi)
# print(math.atan2(0, -1) * 180 / math.pi)
# print(math.atan2(-1, 0) * 180 / math.pi)