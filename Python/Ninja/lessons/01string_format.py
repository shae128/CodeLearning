from random import randint, uniform

num1 = uniform(10, 9000)
num2 = randint(10, 9000)

# Old fashion
print('num1 is', num1, 'and num2 is',  num2)

# Format Method
print('num1 is {0:.3f} and num2 is {1}'.format(num1, num2))

# Using F-Strings
print(f'num1 is {num1:.2f} and num2 is {num2}')
