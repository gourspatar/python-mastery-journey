import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount(1000)
        self.assertEqual(account.balance, 1000)

    def test_deposit(self):
        account = BankAccount(1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_withdraw(self):
        account = BankAccount(1000)
        account.withdraw(200)
        self.assertEqual(account.balance, 800)

    def test_withdraw_more_than_balance(self):
        account = BankAccount(1000)

        with self.assertRaises(ValueError):
            account.withdraw(1500)

    def test_deposit_negative_money(self):
        account = BankAccount(1000)

        with self.assertRaises(ValueError):
            account.deposit(-100)


if __name__ == "__main__":
    unittest.main()