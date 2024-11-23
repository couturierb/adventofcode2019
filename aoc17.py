from Intcode2 import Intcode
from os import system
import pprint

def step1() :
    datas = {}
    x = y = 0

    while not intcode.isTerminated() :
        result = intcode.run(0)
        if result == None:
            break
        elif result == 10 :
            y += 1
            x = 0
        else :
            datas[(x, y)] = chr(result)
            x += 1
    step1 = 0
    for key, value in datas.items() :
        if value == '#' and \
            datas.get((key[0], key[1]+1), '') == '#' and \
            datas.get((key[0], key[1]-1), '') == '#' and \
            datas.get((key[0]+1, key[1]), '') == '#' and \
            datas.get((key[0]-1, key[1]), '') == '#' :
                datas[key] = 'O'
                step1 += key[0] * key[1]
    draw(datas)
    print('step 1 : ' + str(step1))

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

        
    
file = open("aoc17.data", "r")
lines = file.readline().split(',')
program = { i : int(lines[i]) for i in range(0, len(lines)) }
intcode = Intcode(program)

# step1()
step2()