class Lion:
    name: str
    gender: str
    age: int

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Lion'

    @staticmethod
    def get_needs():
        amount = 50
        return amount

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

