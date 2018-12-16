class ThisIsClass:
        def __init__(self, val):
                self.val = val


ob1 = ThisIsClass(0)
ob2 = ThisIsClass(2)
ob3 = ob1
ob3.val += 1
print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"
print(str1 == str2, str1 is str2)
