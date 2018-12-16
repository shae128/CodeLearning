age = int(input("Please enter your age: "))

if age < 10:
    print('You are too young')
elif age < 40:
    print('You are getting old')
else:
    print("I'm affraid of but you are about to get old")

meaty = input('Do you eat meat? (y/n): ')

if meaty == "y":
    print("Good for you!")
elif meaty == "n":
    print("Good for your body")
else:
    print("please enter y/n")
