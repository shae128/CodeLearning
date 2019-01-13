# import vehicle class to use as parent for cars class
from Vehicles import Vehicles

# import random
import random


# define Planes class which is a subclass of Vehicles
class Planes(Vehicles):
    def __init__(self, Make, Model, Year, Weight):
        Vehicles.__init__(self, Make, Model, Year, Weight)
        self.isFlying = False

    # repair method
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    # Flying method
    def Flying(self):
        # if the plans needs maintenance
        # it won't be able to fly until
        # repairing
        if self.NeedsMaintenance is True:
            return False
        else:
            self.isFlying = True
            return True

    # Landing method
    def Landing(self):
        # if plane is flying so it
        # will land and trips will
        # increment by one
        if self.isFlying is True:
            self.isFlying = False
            self.TripsSinceMaintenance += 1

            # if trips exceed 100 the plan needs repairing
            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True

    # override str
    def __str__(self):
        return self.Make + " " + self.Model + " " + str(
            self.Year) + " model" + " which weights exactly " + self.Weight


# initialize two instances of Planes class
Plane1 = Planes("Boing", "777", 2018, 351500)
Plane2 = Planes("Airbus", "A380", 2018, 390000)


# test flight planes
def testFlight(plane):
    for i in range(random.randrange(130)):
        if plane.Flying():
            plane.Landing()
        else:
            print("Because this", plane.Make, plane.Model,
                  "needs repair you can not attempt to flight!!!")
            while True:
                desicion = input(
                    "Do you proceed to repairing process  (y/n): ")

                if desicion is "y":
                    plane.Repair()
                    print(plane.Make, plane.Model,
                          "has been repaired and is ready to flight again!")
                    break
                elif desicion is "n":
                    print("Sorry your are not able to fly until repairing!!!")
                    break
                else:
                    print("Please just answer with \"y\" or \"n\"!!!")

            return

    print("This", plane.Make, plane.Model, "completed",
          plane.TripsSinceMaintenance, "flights successfully!!!")


print("--------------------")
testFlight(Plane1)
print("--------------------")
testFlight(Plane2)
print("--------------------")
