from Intcode2 import Intcode 
    
file = open("aoc21.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)

def setInput(command) :
    inArr = [ord(i) for i in command]
    inArr.append(10)
    intcode.addInputs(inArr)

def step1() :
    while not intcode.isTerminated() :


 
 



        setInput('NOT C J')
        setInput('AND D J')
        setInput('AND H J')
        setInput('NOT B T')

        setInput('AND D T')
        setInput('OR T J')
        setInput('NOT A T')
        setInput('OR T J')

        setInput('RUN')
        out = intcode.run()
        if out < 122 :
            print(chr(out), end='')
        else :
            print(out)
    

step1()