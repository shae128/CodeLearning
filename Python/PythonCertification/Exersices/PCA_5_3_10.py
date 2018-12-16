class Class:
        Attr = 1
        
        def __init__(self, val):
                if val % 2 != 0:
                        self.a = 1
                else:
                        self.b = 2


object = Class(1)
if hasattr(object, 'a'):
        print(object.a)
else:
        print(object.b)

print("-------------------")

print(hasattr(Class, 'Attr'))
print(hasattr(Class, 'pop'))
