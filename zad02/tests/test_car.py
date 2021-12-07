import sys

sys.path.append('../src')
from car import Car
from carImpl import CarImpl
from unittest.mock import Mock, patch
import unittest


class TestCar(unittest.TestCase):

    def test_willIArive_Poland(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = "Poland"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.willIArive("Poland"), "You drive to Poland")

    def test_willIArive_False(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.willIArive("Poland"), "Where are you driving?")

    def test_alert_True(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.alert(), "NEED FUEL")

    def test_alert_False(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.alert(), "It's ok")

    def test_getTemp_360(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 360
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.getTemp(), "360 F")

    def test_getTemp_False(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.getTemp(), "404 Engine Not Found")