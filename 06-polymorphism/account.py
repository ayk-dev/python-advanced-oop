class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_owner = f'{self.owner}&{other.owner}'
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.balance}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, key):
        return self._transactions[key]


def test_account_can_be_instantiated():
    acc1 = Account('Bob', 10)
    acc1_dict = acc1.__dict__
    assert acc1_dict == {'owner': 'Bob', 'amount': 10, '_transactions': []}
    print('test passed')


def test_add_transaction_method():
    acc1 = Account('Bob', 10)
    acc1.add_transaction(0.5)
    print('test passed')


# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.__dict__)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3.__dict__)
# print(acc3._transactions)







