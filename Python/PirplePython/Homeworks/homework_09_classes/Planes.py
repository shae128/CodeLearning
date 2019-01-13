from Vehicles import Vehicles
import random


class Planes(Vehicles):
    def __init__(self, Make, Model, Year, Weight):
        Vehicles.__init__(self, Make, Model, Year, Weight)
        self.isFlying = False

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def Flying(self):
        if self.NeedsMaintenance is True:
            return False
        else:
            self.isFlying = True
            return True

    def Landing(self):
        if self.isFlying is True:
            self.isDriving = False
            self.TripsSinceMaintenance += 1

            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True

    def __str__(self):
        return self.Make + " " + self.Model + " " + str(
            self.Year) + " model" + " which weights exactly " + self.Weight


Plane1 = Planes("Boing", "777", 2018, 351500)
Plane2 = Planes("Airbus", "A380", 2018, 390000)


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
