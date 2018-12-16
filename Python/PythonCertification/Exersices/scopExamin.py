# in this file i'm going to examin scope for list

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 3, 4, 5]
list5 = [1, 2, 3, 4, 5]

for sk in range(5):
    print(" dsfkjs")


# this will test just modification inside the function
def test1(lst):
    print("Test 1 lst", lst)
    lst = [1, 2]
    print("Test 1 modified lst:  ", lst)
    print("Test 1 list:", list1)


print("----------TEST 1----------")
test1(list1)
print("outside", list1)


# now lets test list modification via methods inside the function
def test2(lst):
    print("Test 2 lst", lst)
    lst.append(6)
    print("Test 2 modified lst:  ", lst)
    print("Test 2 list:", list2)


print("----------TEST 2----------")
print("outside before function invocation:", list2)
test2(list2)
print("outside:", list2)


# now lets test list modification via methods outside the function
def test3(lst):
    print("Test 3 lst", lst)
    list3.append(6)
    print("Test 3 lst after modifing list3 :  ", lst)
    print("Test 3 list:", list3)


print("----------TEST 3----------")
print("outside before function invocation:", list3)
test3(list3)
print("outside:", list3)


# Test list modification without passing as argument via methods
def test4():
    list4.append(6)
    print("Test 4 list:", list4)


print("----------TEST 4----------")
print("outside before function invocation:", list4)
test4()
print("outside:", list4)


# Test list modification without passing as argument without methods
def test5():
    list5 = [1, 2]
    print("Test 5 inside function list5 :", list5)


print("----------TEST 5----------")
print("outside before function invocation list5:", list5)
test5()
print("outside after invocation list5:", list5)


# def test6():
#     lst.append(6)
#     print(lst)


# test6()
