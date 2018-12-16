person = dict()

print('Plese enter your informations. ')

while True:
    field = input('Enter the filed: ')
    value = input(f'Enter {field} value: ')
    person[field] = value

    decision = input('Wanna continue(y/n)? ')
    if decision == 'n':
        break
    elif decision == 'y':
        continue
    else:
        print('Invalid input')


print('-------------------------')
print("Your informations table")
print('-------------------------')

for key, val in person.items():
    print(f'{key}: {val}')
print('-------------------------')
