from collections import defaultdict

from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    name: str
    chocolate_factory: ChocolateFactory
    egg_factory: EggFactory
    paint_factory: PaintFactory
    storage: dict

    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = defaultdict(int)  # product name as key and quantity of the product as value

    def add_chocolate_ingredient(self, type_chocolate: str, quantity: int):
        self.chocolate_factory.add_ingredient(type_chocolate, quantity)

    def add_egg_ingredient(self, type_egg: str, quantity: int):
        self.egg_factory.add_ingredient(type_egg, quantity)

    def add_paint_ingredient(self, type_color: str, quantity: int):
        self.paint_factory.add_ingredient(type_color, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):

        if (egg_type in self.egg_factory.products and self.egg_factory.ingredients[egg_type] >= 1) and \
                (color in self.paint_factory.products and self.paint_factory.ingredients[color] >= 1):

            painted_egg = f'{color} {egg_type}'
            self.storage[painted_egg] += 1
            self.egg_factory.remove_ingredient(egg_type, 1)
            self.paint_factory.remove_ingredient(color, 1)

        else:
            raise ValueError('Invalid commands')

    def __repr__(self):
        result = f'Shop name: {self.name}\n' + 'Shop Storage:\n'
        for product, quantity in self.storage.items():
            result += f'{product}: {quantity}\n'

        return result.stripr('\n')
