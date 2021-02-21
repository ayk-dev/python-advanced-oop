from collections import defaultdict

from project.factory.factory import Factory


class ChocolateFactory(Factory):
    chocolate_ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes: dict = {}
        self.products: dict = defaultdict(int)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.chocolate_ingredients:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}')

        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')

        if ingredient_type not in self.ingredients.keys():
            self.ingredients[ingredient_type] = quantity
            return
        self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError('No such product in the factory')

        if quantity > self.ingredients[ingredient_type]:
            raise ValueError('Ingredient quantity cannot be less than zero')

        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name in self.recipes.keys():
            updated = {recipe_name: recipe}
            self.recipes.update(updated)
            return
        self.recipes[recipe_name] = recipe
        # TODO what does  it mean to update?

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError('No such recipe')

        for ingredient, quantity in self.recipes[recipe_name].items():
            self.remove_ingredient(ingredient, quantity)

        self.products[recipe_name] += 1




