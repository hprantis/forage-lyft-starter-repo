import unittest
from datetime import datetime
from refactor.batteries.SpindlerBattery import SpindlerBattery
from refactor.tires.CarriganTire import CarriganTire
from refactor.tires.OctoprimeTire import OctoprimeTire


class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date, today)

        self.assertFalse(battery.needs_service())


class TestCarriganTire(unittest.TestCase):

    def test_tires_should_be_serviced(self):
        wear_array = [0.9, 0.8, 0.8, 0.8]
        tire = CarriganTire(wear_array)

        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):
        wear_array = [0.2, 0.2, 0.2, 0.2]
        tire = CarriganTire(wear_array)

        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):

    def test_tires_should_be_serviced(self):
        wear_array = [0.9, 0.9, 0.9, 0.9]
        tire = OctoprimeTire(wear_array)

        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):
        wear_array = [0.3, 0.3, 0.3, 0.3]
        tire = OctoprimeTire(wear_array)

        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
