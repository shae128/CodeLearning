def equall(a, b, c):

    # try to convert input to int if is possible
    try:
        a = int(a)
    except ValueError:
        a = a

    try:
        b = int(b)
    except ValueError:
        b = b

    try:
        c = int(c)
    except ValueError:
        c = c

    # check if any value pair is equall
    if a == b:
        return True
    elif a == c:
        return True
    elif b == c:
        return True
    else:
        return False


print(equall(1, 3, 5))
print(equall(1, 1, 5))
print(equall(1, 3, 1))
print(equall(1, 5, 5))
print(equall(1, "5", 5))
print(equall("sgkasjglah", "5", 5))
