class Super:
        SupVar = 1


class Sub(Super):
        SubVar = 2


object = Sub()
print(object.SubVar)
print(object.SupVar)
