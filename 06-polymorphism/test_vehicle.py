from .vehicle import Vehicle, Car, Truck

import unittest


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(10, 1.1)

    # def test_car_is_initiated(self):
    #     self.assertEqual(self.car.fuel_quantity, 10)
    #     self.assertEqual(self.car.fuel_consumption, 1.1)

    def test_not_enough_fuel_to_drive_car(self):
        self.car.drive(100)
        self.assertEqual(self.car.fuel_quantity, 10)

    def test_car_drive(self):
        self.car.drive(1)
        self.assertEqual(self.car.fuel_quantity, 8)

    def test_car_refuel(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_quantity, 15)


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = Truck(10, 0.4)

    # def test_truck_is_initiated(self):
    #     self.assertEqual(self.truck.fuel_quantity, 10)
    #     self.assertEqual(self.truck.fuel_consumption, 0.4)

    def test_drive_truck_not_enough_fuel(self):
        self.truck.drive(100)
        self.assertEqual(self.truck.fuel_quantity, 10)

    def test_truck_drive_enough_fuel(self):
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 8)

    def test_truck_refuel(self):
        self.truck.refuel(5)
        self.assertEqual(self.truck.fuel_quantity, 14.75)


if __name__ == '__main__':
    unittest.main()
