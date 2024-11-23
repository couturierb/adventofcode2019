class Intcode :
    def __init__(self, puzzleinput) :
        self.puzzleinput = puzzleinput
        self.relativeBase = 0
        self.instructionPointer = 0
        self.output = None
        self.code = None

    def isTerminated(self) :
        return self.code == 99

    def initParam(self) :
        self.pointerDelta = None
        self.params = {}
        self.modes = {}
        self.__getOpCode__(self.instructionPointer)
        self.params[1] = self.puzzleinput.get(self.instructionPointer+1)
        if self.code == 1 or self.code == 2 or self.code == 7 or self.code == 8 :
            self.params[2] = self.puzzleinput.get(self.instructionPointer+2)
            self.params[3] = self.puzzleinput.get(self.instructionPointer+3)
            self.size = 4
        elif self.code == 3 or self.code == 4 or self.code == 9 :
            self.size = 2
        elif self.code == 5 or self.code == 6 :
            self.params[2] = self.puzzleinput.get(self.instructionPointer+2)
            self.size = 3

    def __doAction__(self) :
        if self.code == 1:
            self.puzzleinput[self.__getPositionValue__(3)] = self.__getValue__(1) + self.__getValue__(2)
        elif self.code == 2:
            self.puzzleinput[self.__getPositionValue__(3)] = self.__getValue__(1) * self.__getValue__(2)
        elif self.code == 4:
            self.output = self.__getValue__(1)
        elif self.code == 3:
            self.puzzleinput[self.__getPositionValue__(1)] = self.input
        elif self.code == 5:
            if not self.__getValue__(1) == 0 : self.pointerDelta = self.__getValue__(2)
        elif self.code == 6:
            if self.__getValue__(1) == 0 : self.pointerDelta = self.__getValue__(2)
        elif self.code == 7:
            if self.__getValue__(1) < self.__getValue__(2) :
                self.puzzleinput[self.__getPositionValue__(3)] = 1
            else :
                self.puzzleinput[self.__getPositionValue__(3)] = 0
        elif self.code == 8:
            if self.__getValue__(1) == self.__getValue__(2) :
                self.puzzleinput[self.__getPositionValue__(3)] = 1
            else :
                self.puzzleinput[self.__getPositionValue__(3)] = 0
        elif self.code == 9 :
            self.relativeBase += self.__getValue__(1)

    def runOnce(self, input) :
        self.input = input
        self.initParam()
        self.__doAction__()
        if self.pointerDelta == None :
            self.instructionPointer += self.size
        else :
            self.instructionPointer = self.pointerDelta
        return self.output

    def run(self, input) :
        self.input = input
        self.output = None
        while not self.isTerminated() and self.output == None:
            self.initParam()
            self.__doAction__()
            if self.pointerDelta == None :
                self.instructionPointer += self.size
            else :
                self.instructionPointer = self.pointerDelta

        return self.output

    def __getPositionValue__(self, paramNumber) :
        mode = self.modes.get(paramNumber, 0)
        if mode == 1 :
            raise Exception("NANI ?")
        elif mode == 2 :
            return self.params[paramNumber] + self.relativeBase
        else :
            return self.params[paramNumber]
        
    def __getValue__(self, paramNumber) :
        if self.modes.get(paramNumber, 0) == 1 :
            return self.params[paramNumber]
        else :
            return self.puzzleinput.get(self.__getPositionValue__(paramNumber), 0) 

    def __getOpCode__(self, index) :
        self.code = self.puzzleinput[index] % 100
        self.modes[1] = self.puzzleinput[index] // 100 % 10
        self.modes[2] = self.puzzleinput[index] // 1000 % 10
        self.modes[3] = self.puzzleinput[index] // 10000