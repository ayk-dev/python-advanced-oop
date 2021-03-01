from project.medicine.medicine import Medicine
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    survivors: list
    supplies: list
    medicine: list
    food: list
    water: list
    painkillers: list
    salves: list

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply']
        if len(result) == 0:
            raise IndexError('There are no food supplies left!')
        return result

    @property
    def water(self):
        result = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']
        if len(result) == 0:
            raise IndexError('There are no water supplies left!')
        return result
    
    @property
    def painkillers(self):
        result = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if len(result) == 0:
            raise IndexError('There are no painkillers left!')
        return result

    @property
    def salves(self):
        result = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if len(result) == 0:
            raise IndexError('There are no salves left!')
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if not survivor.needs_healing:
            return

        if medicine_type == 'Painkiller':
            med = self.painkillers.pop()
        else:
            med = self.salves.pop()
        self.medicine.remove(med)
        med.apply(survivor)
        return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return

        if sustenance_type == 'FoodSupply':
            supp = self.food.pop()
        else:
            supp = self.water.pop()
        self.supplies.remove(supp)
        supp.apply(survivor)
        return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')

#
# bunker = Bunker()
# survivor = Survivor('Name', 100)
#
# food = FoodSupply()
# bunker.add_supply(food)
# bunker.add_survivor(survivor)
# bunker.sustain(survivor, 'FoodSupply')
