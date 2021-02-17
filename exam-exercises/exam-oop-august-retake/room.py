class Room:
    family_name: str
    budget: float
    members_count: int
    children: list

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum([el.cost for seq in args for el in seq])

    def get_monthly_expense(self):
        return self.expenses * 30



