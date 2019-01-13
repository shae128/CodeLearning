myUniqueList = []
myLeftovers = []


def addValue(val):
    if not val in myUniqueList:
        myUniqueList.append(val)
        return True
    else:
        myLeftovers.append(val)
        return False


addValue(6)
addValue(7)
addValue(6)
addValue(8)
addValue(8)
addValue(8)
addValue(9)

print(myUniqueList)
print(myLeftovers)
