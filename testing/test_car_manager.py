from .car_manager import Car

import unittest

class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('make', 'model', 1, 5)

    def test_init(self):
        self.assertEqual(self.car.make, 'make')
        self.assertEqual(self.car.model, 'model')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 5)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ''

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ''

    def test_zero_or_negative_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

        with self.assertRaises(Exception):
            self.car.fuel_consumption = -5

    def test_zero_or_negative_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

        with self.assertRaises(Exception):
            self.car.fuel_capacity = -5

    def test_refuel_zero_or_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-42)

    def test_refuel_more_than_capacity(self):
        self.car.refuel(42)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 1)

    def test_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(1000)
        self.assertEqual(str(exc.exception), "You don't have enough fuel to drive!")

    def test_fuel_amount_after_driver(self):
        self.car.refuel(5)
        self.car.drive(5)
        self.assertEqual(self.car.fuel_amount, 4.95)


if __name__ == '__main__':
    unittest.main()


