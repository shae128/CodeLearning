def isPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


for i in range(20):
    if isPrime(i):
        print(i)
