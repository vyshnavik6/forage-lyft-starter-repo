import unittest
from datetime import datetime, date

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.today = date.today()

    def create_car(self, car_class, last_service_date, current_mileage, last_service_mileage, *args, **kwargs):
        return car_class(last_service_date, current_mileage, last_service_mileage, *args, **kwargs)

    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = self.create_car(Calliope, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Glissade, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Palindrome, last_service_date, False)
        self.assertTrue(car.needs_service())

        car = self.create_car(Rorschach, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Thovex, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = self.create_car(Calliope, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Glissade, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Palindrome, last_service_date, False)
        self.assertFalse(car.needs_service())

        car = self.create_car(Rorschach, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Thovex, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30001
        last_service_mileage = 0

        car = self.create_car(Calliope, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Glissade, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Palindrome, last_service_date, True)
        self.assertTrue(car.needs_service())

        car = self.create_car(Rorschach, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        car = self.create_car(Thovex, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30000
        last_service_mileage = 0

        car = self.create_car(Calliope, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Glissade, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Palindrome, last_service_date, False)
        self.assertFalse(car.needs_service())

        car = self.create_car(Rorschach, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

        car = self.create_car(Thovex, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
