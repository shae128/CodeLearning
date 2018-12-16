class Class:
        a = 1

        def __init__(self):
                self.b = 2


object = Class()
print(hasattr(object,'b'))
print(hasattr(object,'a'))
print(hasattr(Class,'b'))
print(hasattr(Class,'a'))
