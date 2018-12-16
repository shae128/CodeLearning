userIncome = float(input('Please input your annual income: '))

if userIncome <= 85528:
    tax = 18 * userIncome / 100 - 556.02
else:
    tax = 32 * (userIncome - 85528) / 100 + 14839.02

if tax <= 0:
    print('You should not pay any tax') 
else:
    print('Your tax is:', round(tax, 0))
