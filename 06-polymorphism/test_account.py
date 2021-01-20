from .account import Account

import unittest


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.acc = Account('Billy')

    def test_account_has_correct_owner_and_amount(self):
        self.assertEqual(self.acc.owner, 'Billy')
        self.assertEqual(self.acc.amount, 0)

    def test_account_len_should_be_zero_by_default(self):
        self.assertEqual(len(self.acc), 0)

    def test_add_transaction_changes_balance(self):
        self.acc.add_transaction(100)
        self.assertEqual(self.acc.balance, 100)

    # def test_add_transaction_with_non_int_amount_raises_error(self):
    #     with self.assertRaises(ValueError) as error:
    #         self.acc.add_transaction(10.5)
    #     self.assertEqual(str(error.exception), str(ValueError('please use int for amount')))

    def test_validate_transaction(self):
        with self.assertRaises(ValueError) as error:
            self.acc.validate_transaction(self.acc, -101)
        self.assertEqual(str(error.exception), str(ValueError('sorry cannot go in debt!')))

        result = self.acc.validate_transaction(self.acc, 100)
        self.assertEqual(result, f"New balance: {self.acc.balance}")

    def test_if_balances_are_equal(self):
        other_acc = Account('Bob')
        self.assertTrue(self.acc.__eq__(other_acc))

        second_other_acc = Account('Toto', 200)
        self.assertFalse(self.acc.__eq__(second_other_acc))

    def test_adding_transactions_should_increase_balance(self):
        self.acc.add_transaction(10)
        self.acc.add_transaction(20)
        self.assertEqual(30, self.acc.balance)

    def test_add_accounts(self):
        other_acc = Account('Bob', 100)
        new_account = self.acc + other_acc
        self.assertEqual(new_account.owner, f'{self.acc.owner}&{other_acc.owner}')
        self.assertEqual(new_account.amount, self.acc.amount + other_acc.amount)

    def test_account_string_method(self):
        result = self.acc.__str__()
        self.assertEqual(result, f'Account of {self.acc.owner} with starting amount: {self.acc.balance}')

    def test_account_repr_method(self):
        result = self.acc.__repr__()
        self.assertEqual(result, f'Account({self.acc.owner}, {self.acc.amount})')

    def test_correct_number_of_transactions_is_returned(self):
        self.acc.add_transaction(10)
        self.assertEqual(len(self.acc), 1)

    def test_return_transaction_by_key(self):
        self.acc.add_transaction(10)
        self.assertEqual(self.acc.__getitem__(0), 10)

    def test_compare_account_balances(self):
        other_acc = Account('Bob', 50)
        greater_or_equal_result = self.acc.balance >= other_acc.balance
        result = other_acc >= self.acc
        self.assertEqual(greater_or_equal_result, False)
        self.assertEqual(result, True)

        self.assertFalse(self.acc >= other_acc)
        self.assertTrue(other_acc >= self.acc)

        less_than_or_equal_result = self.acc <= other_acc
        self.assertEqual(less_than_or_equal_result, True)

    def test_reversing_account(self):
        self.acc.add_transaction(10)
        self.acc.add_transaction(20)
        self.assertEqual([20, 10], list(reversed(self.acc)))


if __name__ == '__main__':
    unittest.main()