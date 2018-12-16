numbers = [6, 34, 345, 4, 7, 45, 23, 45, 34, 878, 78, 5]
toFind = 4
position = 0

for i in numbers:
    founded = i == toFind
    
    if founded:
        break
    
    position += 1
    
if founded:
    print(toFind, "is founded on", position,)
else:
    print(toFind, "not founded")
