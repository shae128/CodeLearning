myNum = 8


def stampa():
    global myNum
    myNum += 9
    print('inside', myNum)


print('outside', myNum)
stampa()
