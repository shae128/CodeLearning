numbers = []

# for n in range(int(input(
#         'Please enter how many numbers you want to compare: '))):
#     numbers.append(int(input('Please enter the {}st number: '.format(n+1))))

while True:
    userInput = input('Please enter a number, when you are finished press (f): ')
    if userInput == 'f' or userInput == "F":
        break
    else:
        numbers.append(int(userInput))
        # elif int(userInput):
        # print('Invalid input!')


maxOfAll = numbers[0]
for n in numbers:
    if n >= maxOfAll:
        maxOfAll = n

print(' ---------------- ')
print('Max number is', maxOfAll)
print(' ---------------- ')
