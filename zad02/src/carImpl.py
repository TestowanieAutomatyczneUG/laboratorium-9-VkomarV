from car import Car


class CarImpl:
    def __init__(self):
        self.car = Car()

    def willIArive(self, destination):
        if self.car.driveTo(destination) < 600 and self.car.needsFuel():
            return True
        else:
            return False

    def report(self):
        data = (self.car.needsFuel(), self.car.getEngineTemperature())
        return data
