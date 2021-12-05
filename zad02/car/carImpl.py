from car import Car


class CarImpl:
    def __init__(self):
        self.car = Car()

    def willIArive(self, destination):
        if self.car.driveTo(destination) > self.car.needsFuel():
            return False
        else:
            return True

    def report(self):
        data = (self.car.needsFuel(), self.car.getEngineTemperature())
        return data
