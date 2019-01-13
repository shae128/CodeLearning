"""
I have a list and I just want to track how many time any element
is repeated

"""

CountryList = [
    "Iran",
    "USA",
    "Iran",
    "UK",
    "France",
    "Italy",
    "UK",
    "France",
    "Iran"
]


CountryDict = dict()

for country in CountryList:
    if country in CountryDict:
        CountryDict[country] += 1
    else:
        CountryDict[country] = 1


print(CountryDict)
