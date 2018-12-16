numbers = [6, 34, 345, 4, 7, 45, 23, 45, 34, 878, 78, 5]
swapped = True

while swapped:
    swapped = False

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            swapped = True
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp

print(numbers)
