from cars.carsClass import Cars

tesla = Cars('Tesla', 'Model 3', 'Elec', 'hatchback', 2019)
print(tesla.info())

print('--------------------')

cClass = Cars('Mercedes', 'C Class', 'Sedan', 'Gas', 2018)

print(f'{cClass.model} fuel is {cClass.fuel}')
print(cClass.info())
print(Cars.shapes())
print(cClass.shapes())
print(Cars.speeds())
print(cClass.speeds(300))
