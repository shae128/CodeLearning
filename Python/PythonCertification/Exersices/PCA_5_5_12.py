class Super:
        def __init__(self, name):
                self.name = name
        def __str__(self):
                return "My name is " + self.name + "."

class Sub(Super):
        def __init__(self, name):
                super().__init__(name)

object = Sub("Andy")
print(object)
