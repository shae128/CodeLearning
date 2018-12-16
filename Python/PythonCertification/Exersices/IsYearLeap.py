def IsYearLeap(year):
    if year % 4 != 0:
        isLeap = False
    elif year % 100 != 0:
        isLeap = True
    elif year % 400 != 0:
        isLeap = False
    else:
        isLeap = True

    return isLeap


def daysInMonth(year, month):
    global months
    if IsYearLeap(year):
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return months[month-1]


def dayOfYear(year, month, day):
    daysInMonth(year, month)
    sum = 0

    if month > 12 or month < 1:
        return "Invalid month"

    if not IsYearLeap(year) and month == 2 and day > 28:
        return f'{year} is not a Leap year so Feb has 28 days!'

    if day > months[month-1]:
        return "invalid day"

    if month == 1:
        return sum + day
    else:
        for i in range(1, month):
            sum += daysInMonth(year, i)
        return sum + day

print(dayOfYear(1900, 2, 29))
print("--------------")
print(dayOfYear(2000, 2, 29))
print("--------------")
print(dayOfYear(2000, 1, 29))


# print(dayOfYear(2000, 2, 29))

# testyears = [1900, 2000, 2016, 1987]
# testmonths = [2, 2, 1, 11]
# testresults = [28, 29, 31, 30]

# for i in range(len(testyears)):
#     yr = testyears[i]
#     mo = testmonths[i]
#     print(yr, mo, "->", end="")
#     result = daysInMonth(yr, mo)

# if result == testresults[i]:
#     print("OK")
# else:
#     print("Failed")
