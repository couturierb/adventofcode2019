file = open("/Users/myzuno/Google Drive/dev/adventOfCode/aoc5.data", "r")

class Intcode :
    def __init__(self, puzzleinput, index) :
        self.puzzleinput = puzzleinput
        self.__getOpCode__(index)
        self.pointerDelta = None
        self.param1 = puzzleinput[index+1]
        if self.code == 1 or self.code == 2 or self.code == 7 or self.code == 8 :
            self.param2 = puzzleinput[index+2]
            self.param3 = puzzleinput[index+3]
            self.size = 4
        elif self.code == 3 or self.code == 4 :
            self.size = 2
        elif self.code == 5 or self.code == 6 :
            self.param2 = puzzleinput[index+2]
            self.size = 3

    def isTerminated(self) :
        return self.code == 99

    def doAction(self) :
        if self.code == 1:
            self.puzzleinput[self.param3] = self.__getValue1__() + self.__getValue2__()
        elif self.code == 2:
            self.puzzleinput[self.param3] = self.__getValue1__() * self.__getValue2__()
        elif self.code == 4:
            print("printed " + str(self.__getValue1__()) + " for index " + str(self.param1))
        elif self.code == 3:
            self.puzzleinput[self.param1] = input
        elif self.code == 5:
            if not self.__getValue1__() == 0 : self.pointerDelta = self.__getValue2__()
        elif self.code == 6:
            if self.__getValue1__() == 0 : self.pointerDelta = self.__getValue2__()
        elif self.code == 7:
            if self.__getValue1__() < self.__getValue2__() :
                self.puzzleinput[self.param3] = 1
            else :
                self.puzzleinput[self.param3] = 0
        elif self.code == 8:
            if self.__getValue1__() == self.__getValue2__() :
                self.puzzleinput[self.param3] = 1
            else :
                self.puzzleinput[self.param3] = 0

    def __getValue1__(self) :
        return self.param1 if self.mode1 == 1 else self.puzzleinput[self.param1]

    def __getValue2__(self) :
        return self.param2 if self.mode2 == 1 else self.puzzleinput[self.param2]

    def __getOpCode__(self, index) :
        self.code = self.puzzleinput[index] % 100
        self.mode1 = self.puzzleinput[index] // 100 % 10
        self.mode2 = self.puzzleinput[index] // 1000

def start():
    program = [int(i) for i in file.readline().split(',')]
    instructionPointer = 0
    intcode = Intcode(program, instructionPointer)
    while not intcode.isTerminated() :
        intcode.doAction()
        if intcode.pointerDelta == None :
            instructionPointer += intcode.size
        else :
            instructionPointer = intcode.pointerDelta

        intcode = Intcode(program, instructionPointer)

    # print(program)
input = 5
start()
