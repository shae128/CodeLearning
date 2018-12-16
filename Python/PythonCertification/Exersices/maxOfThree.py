numbers = []
for n in range(3):
    numbers.append(int(input(f'Please enter a number {n}: ')))

if numbers[0] >= numbers[1] & numbers[0] >= numbers[2]:
    print('Max= ', numbers[0])
elif numbers[1] >= numbers[0] & numbers[1] >= numbers[2]:
    print('Max =', numbers[1])
else:
    print('Max =', numbers[2])
