from abc import ABC, abstractmethod


class Factory(ABC):
    name: str
    capacity: int
    ingredients: dict # (name of the ingredient for key and quantity of the ingredient as a value)

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {} # TODO is this protected or private (we use property for it)

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        return value + sum(self.ingredients.items()) <= self.capacity

