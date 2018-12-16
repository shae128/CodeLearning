class Class:
        __Counter = 0

        def __init__(self, val=1):
                self.__First = val
                Class.__Counter += 1


object1 = Class()
object2 = Class(2)
object3 = Class(4)

print(object1.__dict__, object1._Class__Counter)
print(object2.__dict__, object2._Class__Counter)
print(object3.__dict__, object3._Class__Counter)
