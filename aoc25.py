from Intcode2 import Intcode
from os import system
import pprint

def step1() :
    while not intcode.isTerminated() :
        out = intcode.run()
        print(chr(out), end='')
        if out == 63 :
            print()
            ins = input()
            inArr = [ord(i) for i in ins]
            intcode.setInputs(inArr + [10])
            

def step2() :
    inputs = ['C',',','A',',','C',',','A',',','B',',','B',',','A',',','C',',','A',',','B','\n', \
    'R',',','8',',','R',',','5',',','5',',','R',',','6',',','6','\n', \
    'L',',','1','0',',','R',',','1','2',',','R',',','8','\n', \
    'L',',','1','2',',','L',',','1','0',',','R',',','8',',','L',',','1','2','\n', \
    'n','\n']

    inputs = [ord(value) for value in inputs]

    intcode.setInputs(inputs)
    
    while not intcode.isTerminated() :
        result = intcode.run()
        if result == None:
            break
        print(result)
        # datas[(x, y)] = chr(result)
      
file = open("aoc25.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)

step1()
# step2()