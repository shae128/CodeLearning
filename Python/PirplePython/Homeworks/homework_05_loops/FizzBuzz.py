"""
I added the numbers to output to make the output more readable
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", ":", i)
    elif i % 3 == 0:
        print("Fizz", ":", i)
    elif i % 5 == 0:
        print("Buzz", ":", i)
    elif i % 2 == 0:
        print(i)
    elif i == 7:
        print("Prime", ":", i)
    elif i % 7 == 0:
        print(i)
    else:
        print("Prime", ":", i)



