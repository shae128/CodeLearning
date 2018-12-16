class Class:
        Var = 1

        def __init__(self, val):
                self.Var = val


print(Class.__dict__)
print("-------------------------")
object = Class(2)
print(Class.__dict__)
print("-------------------------")
print(object.__dict__)
