import re

def test(passwordTest) :
    passwordTestText = str(passwordTest)
    length = len(passwordTestText)
    passwordTestText = "AQ" + passwordTestText + "FG"

    for indice in range(2, length+2) :
        if (passwordTestText[indice] == passwordTestText[indice+1]) and \
            not passwordTestText[indice] == passwordTestText[indice-1] and \
            not passwordTestText[indice] == passwordTestText[indice+2] :
                return True

    return False

def increment(passwordTest) :
    passwordTest += 1
    passwordTestStr = str(passwordTest)
    
    for i in range(6) :
        if passwordTestStr[i] == '0':
            passwordTestStr = passwordTestStr.replace('0', passwordTestStr[i-1])

    return int(passwordTestStr)

def start():
    # 125730 - 579381
    passwordTest = 125777
    end = 579381
    count = 0

    while not passwordTest > end:
        if test(passwordTest) :
            count += 1
        passwordTest = increment(passwordTest)

    print(count)

start()