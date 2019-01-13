# Vehicles class
class Vehicles:
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

    # repair method
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False
