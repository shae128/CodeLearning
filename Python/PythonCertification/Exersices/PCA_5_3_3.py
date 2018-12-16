class Class:
        def __init__(self, val=1):
                self.__First = val

        def setSecond(self, val=2):
                self.__Second = val


object1 = Class()
object2 = Class(2)
object2.setSecond(3)
object3 = Class(4)
object3.__Third = 5


print(object1.__dict__)
print(object2.__dict__)
print(object3.__dict__)
print(object1._Class__First)
