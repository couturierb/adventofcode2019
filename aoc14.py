import functools

class Element() :
    def __init__(self, element, reactifs) :
        self.name = element.split(' ')[1]
        self.reserve = 0
        self.produced = 0
        self.multiplicateur = int(element.split(' ')[0])
        self.reactifStr = reactifs

    def complete(self, elements) :
        self.reactifs = []
        if self.reactifStr == None: return

        for reactif in self.reactifStr.split(', ') :
            name = reactif.split(' ')[1]
            multiplicateur = int(reactif.split(' ')[0])
            element = searchElement(elements, name)
            if element == None : raise NameError('element not found ' + name)
            self.reactifs.append((element, multiplicateur))

    def produce(self, quantiy) :
        while self.reserve < quantiy :
            # howMany = quantiy - self.reserve
            if not self.name == 'ORE' :
                for (reactif, multi) in self.reactifs :
                    reactif.produce(multi)

            self.reserve += self.multiplicateur

        # print('ORE left : ' + str(self.reserve) + ' - used : ' + str(quantiy))
        self.reserve -= quantiy
        self.produced += quantiy

    def produce2(self, quantiy) :
        if self.reserve < quantiy :
            howMany = quantiy - self.reserve
            howMany = (howMany // self.multiplicateur) + (howMany % self.multiplicateur)
            if not self.name == 'ORE' :
                for (reactif, multi) in self.reactifs :
                    reactif.produce(multi * howMany)

            self.reserve += howMany * self.multiplicateur

        self.reserve -= quantiy
        self.produced += quantiy

def searchElement(elements, name) :
    finded = [elem for elem in elements if elem.name == name]
    return finded[0] if len(finded) > 0 else None

def start() :
    file = open("aoc14.data", "r")
    elements = []
    for line in file.read().splitlines() :
        elements.append(Element(line.split(' => ')[1], line.split(' => ')[0]))
    elements.append(Element('1 ORE', None))

    for element in elements :
        element.complete(elements)

    fuel = searchElement(elements, 'FUEL')
    ore = searchElement(elements, 'ORE')

    count = 0
    reserves = []
    while True :
        fuel.produce2(1)
        count += 1
        pouet = [elem.reserve for elem in elements if elem.reserve > 0]
        if pouet in reserves :
            print('same after ' + str(count))
        else :
            reserves.append(pouet)
       
        if count % 100 == 0 :
            print(count)
        # print(reserves)
        # if len(reserves) == 0 :
        #     break
    
    print(count)
    print(ore.produced)

    print(str((1000000000000 / ore.produced) * count)) 
start()