class Class:

        Counter = 0

        def __init__(self, val=1):
                self.__First = val
                Class.Counter += 1


object1 = Class()
print(object1.__dict__, object1.Counter)
print("--------------------")

object2 = Class(2)
object3 = Class(4)
print(object1.__dict__, object1.Counter)
print(object2.__dict__, object2.Counter)
print(object3.__dict__, object3.Counter)
