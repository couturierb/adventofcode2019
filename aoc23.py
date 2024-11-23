from Intcode2 import Intcode

file = open("aoc23.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }

class Computer() :
    def __init__(self, address, program, network) :
        self.address = address
        self.intcode = Intcode(program)
        self.intcode.setInputs([address])
        self.network = network

    def givePacket(self, x, y) :
        self.intcode.addInputs([x, y])

    def isInputsEmtpy(self) :
        return len(self.intcode.inputs) == 0

    def run(self) :
        address = self.intcode.runOnce()
        if address == None : return
        x = self.intcode.run()
        y = self.intcode.run()
        self.network.sendPacket(address, x, y)
        return True

class Network :
    natX = natY = None

    def __init__(self) :
        self.computers = []
        for i in range(0, 50) :
            self.computers.append(Computer(i, program.copy(), self))

    def findComputer(self, address) :
        computer = [comp for comp in self.computers if comp.address == address]
        if not len(computer) == 1 :
            print('Non trouvé ou trop : ' + str(address))
        else :
            return computer[0]

    def sendPacket(self, address, x, y) :
        print('give x:' + str(x) + ' and y:' + str(y) + ' to address:' + str(address))
        if int(address) == 255 :
            self.sendToNat(x, y)
        else :
            targetedComputer = self.findComputer(address)
            if not targetedComputer == None :
                targetedComputer.givePacket(x, y)

    def sendToNat(self, x, y) :
        # if not self.yJustSendToNat == None :
            # print(self.yJustSendToNat)
        #     exit()
        # else :
            # self.yJustSendToNat = y
            # self.natX = x
            # self.natY = y
        self.natX = x
        self.natY = y
        
    def start(self) :
        yJustSendToNat = None
        idleCount = 0
        while True :
            for computer in self.computers :
                if computer.run() :
                    yJustSendToNat = None
                    idleCount = 0

            idle = len([comp for comp in self.computers if comp.isInputsEmtpy()]) == 50
            if idle :
                idleCount += 1

            if idleCount > 10000 and self.natX and self.natY :
                print('Idle')
                if not yJustSendToNat == None :
                    print(yJustSendToNat)
                    exit()
                yJustSendToNat = self.natY
                idleCount = 0
                self.sendPacket(0, self.natX, self.natY)
    
network = Network()
network.start()