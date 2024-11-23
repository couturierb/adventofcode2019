import math

file = open("aoc2.data", "r")

def tryInput(one):
    indice = 0
    while one[indice] != 99 :
    # value = 0
        if one[indice] == 1 :
            value = one[one[indice+1]] + one[one[indice+2]]
        else :
            value = one[one[indice+1]] * one[one[indice+2]]

        one[one[indice+3]] = value
        indice += 4
    return one[0]

input = [int(i) for i in file.readline().split(',')]
noun = 0
verb = 0
found = False

while not found :
    one = list(input)
    one[1] = noun
    one[2] = verb

    value = tryInput(one)
    print(value)
    if value == 19690720:
        print(noun, verb)
        found = True

    noun+=1
    if noun >= 100:
        noun = 0
        verb+=1
