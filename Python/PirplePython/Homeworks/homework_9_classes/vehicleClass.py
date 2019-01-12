import random


class Vehicle:
    def __init__(self, Make, Model, Year, Weight):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = str(Weight) + "KG"
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # setters
    def defineMake(self, Make):
        self.Make = Make

    def defineModel(self, Model):
        self.Make = Model

    def defineYear(self, Year):
        self.Make = Year

    def defineWeight(self, Weight):
        self.Make = Weight

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False


class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        isDriving = False

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        if self.isDriving is True:
            self.isDriving = False
            self.TripsSinceMaintenance += 1

            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True

    def __str__(self):
        return self.Make + " " + self.Model + " " + str(self.Year) + " Model"


Car1 = Cars("Mercedes", "SLR722S", 2010, 1724)
Car2 = Cars("Mercedes", "AMG-GT", 2019, 1615)
Car3 = Cars("Mercedes", "GLE", 2018, 2226)


def testDrive(car):
    for i in range(random.randrange(130)):
        car.Drive()
        car.Stop()

    if car.NeedsMaintenance:
        print(car.Make, car.Model, "Needs Repair because it\'s trips are",
              car.TripsSinceMaintenance)

        while True:
            desicion = input("Do you want to repair it? (y/n): ")

            if desicion is "y":
                car.Repair()
                print(car.Make, car.Model + "\'s trips are reset to",
                      car.TripsSinceMaintenance)
                break
            elif desicion is "n":
                print("Be careful!!!!!")
                break
            else:
                print("Please just answer with \"y\" or \"n\"")

    else:
        print(" This", car,
              "Does not need repair yet \n because it\'s trips are",
              car.TripsSinceMaintenance)


testDrive(Car1)
print("--------------------")
testDrive(Car2)
print("--------------------")
testDrive(Car3)
