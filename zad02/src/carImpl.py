from car import Car


class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def willIArive(self, destination):
        if self.car.driveTo(destination):
            return "You drive to {}".format(str(self.car.driveTo(destination)))
        return "Where are you driving?"

    def alert(self):
        if self.car.needsFuel():
            return "NEED FUEL"
        return "It's ok"

    def getTemp(self):
        if self.car.getEngineTemperature():
            return str(self.car.getEngineTemperature()) + " F"
        return "404 Engine Not Found"