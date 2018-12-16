class Super1:
        pass


class Super2:
        pass


class Sub(Super1, Super2):
        pass


def printbases(cls):
        print('( ', end='')
        for x in cls.__bases__:
                print(x.__name__, end=' ')
        print(')')


printbases(Super1)
printbases(Super2)
printbases(Sub)
