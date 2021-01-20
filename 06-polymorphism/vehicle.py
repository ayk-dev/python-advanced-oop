from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fq, fc):
        self.fuel_quantity = fq
        self.fuel_consumption = fc

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    _CONSUMPTION_INCREASE = 0.9

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self._CONSUMPTION_INCREASE) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _CONSUMPTION_INCREASE = 1.6

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self._CONSUMPTION_INCREASE) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


def test_vehicle_can_be_instantiated():
    Car(10, 5)
    Truck(10, 5)
    print('test passed')

test_vehicle_can_be_instantiated()




