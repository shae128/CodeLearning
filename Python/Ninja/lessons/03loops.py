vegMenu = ['pasta', 'calzone', 'salad']
meatMenu = ['hamburgur', 'soda']
tries = 0
meaty = input('Do you eat meat? (y/n): ')
while tries <= 3:
    if tries == 3:
        print('Too many wrong answer')
        break
    if meaty == "y":
        for meal in meatMenu:
            print(meal.upper())
        break
    elif meaty == "n":
        for meal in vegMenu[0:2]:
            print(meal.upper())
        break
    else:
        meaty = input('invalid answer, please provide y/n: ')
        tries += 1
