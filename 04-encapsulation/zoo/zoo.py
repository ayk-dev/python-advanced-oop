from collections import defaultdict


class Zoo:
    __animal_capacity: int
    __workers_capacity: int
    __budget: int
    name: str
    animals: list
    workers: list

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.workers_names = {}

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'
        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        self.workers_names[worker.name] = worker
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        if worker_name in self.workers_names.keys():
            worker = self.workers_names.get(worker_name)
            self.workers.remove(worker)
            self.workers_names.pop(worker_name)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_of_salaries = sum([w.salary for w in self.workers])
        if sum_of_salaries <= self.__budget:
            self.__budget -= sum_of_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_needs = sum([a.get_needs() for a in self.animals])
        if total_animal_needs <= self.__budget:
            self.__budget -= total_animal_needs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_string = f'You have {len(self.animals)} animals\n'

        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        l_info = f'----- {len(lions)} Lions:\n' + "\n".join([l.__repr__() for l in lions])

        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        t_info = f'----- {len(tigers)} Tigers:\n' + "\n".join([t.__repr__() for t in tigers])

        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        ch_info = f'----- {len(cheetahs)} Cheetahs:\n' + "\n".join([ch.__repr__() for ch in cheetahs])

        return animal_string + l_info + '\n'+ t_info + '\n' + ch_info

    def workers_status(self):
        workers_string = f'You have {len(self.workers)} workers\n'

        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        k_info = f'----- {len(keepers)} Keepers:\n' + '\n'.join([k.__repr__() for k in keepers])

        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        ct_info = f'----- {len(caretakers)} Caretakers:\n' + '\n'.join([ct.__repr__() for ct in caretakers])

        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        v_info = f'----- {len(vets)} Vets:\n' + '\n'.join([v.__repr__() for v in vets])

        return workers_string + k_info + '\n' + ct_info + '\n' + v_info
