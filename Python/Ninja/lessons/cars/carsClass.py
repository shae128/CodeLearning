class Cars:

    shape = 'cube'

    def __init__(self, brand, model, efe, fuel, year):
        self.brand = brand
        self.model = model
        self.efe = efe
        self.fuel = fuel
        self.year = year

    def info(self):
        return f'This is a {self.brand} {self.model} {self.year}'

    @classmethod
    def shapes(cls):
        return f'Any car is often like a {cls.shape}'

    @staticmethod
    def speeds(speed="1km per hour"):
        if speed == "1km per hour":
            return f'Any car should have a speed like at least {speed}'
        else:
            return f'This car has a speed like {speed} per hour'
