import sys

sys.path.append('../src')
from car import Car
from carImpl import CarImpl
from unittest.mock import Mock, patch
import unittest


class TestCar(unittest.TestCase):

    def test_willIArive_True(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        car.driveTo = Mock(name='needsFuel')
        car.driveTo.return_value = 250

        carImpl = CarImpl()
        self.assertEqual(carImpl.willIArive(250), True)
