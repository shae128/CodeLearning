Countries = ["Iran", "UK", "France", "Italy", 432]

myFile = open("Countries", "w")

for country in Countries:
    myFile.write(str(country) + "\n")


myFile.close()


myFile = open("Countries", "r")
theHoleFile = myFile.read()
print(theHoleFile, end="")
myFile.close()


print("-" * 8)
myFile = open("Countries", "r")
for line in myFile:
    print(line, end="")
