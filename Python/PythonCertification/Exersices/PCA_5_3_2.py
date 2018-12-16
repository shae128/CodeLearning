class Class:
        def __init__(self, val=1):
                self.First = val

        def setSecond(self, val=2):
                self.Second = val


object1 = Class()
object1.First = 5
object2 = Class(2)
object2.setSecond(3)
object3 = Class(4)
object3.Third = 5


print(object1.__dict__)
print(object2.__dict__)
print(object3.__dict__)
