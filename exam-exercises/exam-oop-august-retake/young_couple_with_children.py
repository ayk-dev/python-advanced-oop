from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = [[TV(), Fridge(), Laptop()], [TV(), Fridge(), Laptop()]]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.children = list(children)

        for _ in range(len(self.children)):
            self.appliances.append([TV(), Fridge(), Laptop()])

        super().__init__(family_name, salary_one + salary_two, 2 + len(children))

        expenses: list = self.appliances + self.children
        self.calculate_expenses(*expenses)

