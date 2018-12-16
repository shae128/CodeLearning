line = input("Enter numbers, separate them with space \n")

strings = line.split()
sum = 0

for char in strings:

    try:
        num = int(char)
    except:
        num = float(char)

    sum += num

print(sum)
