from abc import ABC

from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal, ABC):
    _FOOD_PREFERENCES = (Vegetable, Fruit, )
    _WEIGHT_GAIN_PER_FOOD = 0.10

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal, ABC):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGHT_GAIN_PER_FOOD = 0.40

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal, ABC):
    _FOOD_PREFERENCES = (Meat, Vegetable, )
    _WEIGHT_GAIN_PER_FOOD = 0.30

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal, ABC):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGHT_GAIN_PER_FOOD = 1.00

    def make_sound(self):
        return 'ROAR!!!'
