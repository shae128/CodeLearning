# import vehicle class to use as parent for cars class
from Vehicles import Vehicles

# import random
import random


# define Cars class which is a subclass of Vehicles
class Cars(Vehicles):
    def __init__(self, Make, Model, Year, Weight):
        Vehicles.__init__(self, Make, Model, Year, Weight)
        self.isDriving = False

    # repair method
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    # Drive method
    def Drive(self):
        self.isDriving = True

    # Stop Method
    def Stop(self):
        # firstly checks if isDriving is True
        # then change it to False and increments
        # Trips by one. If isDriving is not True
        # won't do anything
        if self.isDriving is True:
            self.isDriving = False
            self.TripsSinceMaintenance += 1

            # if Trips exceed 100 the needs to be repair
            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True

    # override str
    def __str__(self):
        return self.Make + " " + self.Model + " " + str(self.Year) + " Model"


# initialize three instances of Cars class
Car1 = Cars("Mercedes", "SLR722S", 2010, 1724)
Car2 = Cars("Mercedes", "AMG-GT", 2019, 1615)
Car3 = Cars("Mercedes", "GLE", 2018, 2226)


# This function will test drive each car
def testDrive(car):
    # drive car for a random trips
    for i in range(random.randrange(130)):
        car.Drive()
        car.Stop()

    if car.NeedsMaintenance:
        print(car.Make, car.Model, "Needs Repair because it\'s trips are",
              car.TripsSinceMaintenance)

        # take user desicion
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
            # if user respond anything else other than y/n
            else:
                print("Please just answer with \"y\" or \"n\"")

    else:
        print(" This", car,
              "Does not need repair yet \n because it\'s trips are",
              car.TripsSinceMaintenance)


# test drive cars
print("--------------------")
testDrive(Car1)
print("--------------------")
testDrive(Car2)
print("--------------------")
testDrive(Car3)
print("--------------------")
