from ..car.carImpl import CarImpl

from unittest.mock import Mock, patch
import unittest


class TestCar(unittest.TestCase):
    @patch("..car.Car.driveTo")
    @patch("..car.Car.needsFuel")
    def test_willIArive_True(self, needsFuel, driveTo):
        needsFuel.return_value = 300
        driveTo.return_value = 250
        carImpl = CarImpl()
        self.assertEqual(carImpl.willIArive(250), True)

    @patch("..car.Car.driveTo")
    @patch("..car.Car.needsFuel")
    def test_willIArive_False(self, needsFuel, driveTo):
        needsFuel.return_value = 100
        driveTo.return_value = 250
        carImpl = CarImpl()
        self.assertEqual(carImpl.willIArive(250), False)

    @patch("..car.Car.needsFuel")
    @patch("..car.Car.getEngineTemperature")
    def report(self, needsFuel, getEngineTemperature):
        needsFuel.return_value = 300
        getEngineTemperature.return_value = 180
        carImpl = CarImpl()
        self.assertEqual(carImpl.report(), (300, 180))
