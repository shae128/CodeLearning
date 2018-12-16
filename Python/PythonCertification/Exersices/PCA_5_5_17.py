class Level0:
        Var = 100

        def fun(self):
                return 101


class Level1(Level0):
        Var = 200

        def fun(self):
                return 201


class Level2(Level1):
        pass


object = Level2()
print(object.Var, object.fun())
