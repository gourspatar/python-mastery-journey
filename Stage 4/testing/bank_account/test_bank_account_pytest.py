import pytest
from bank_account import BankAccount


def test_initial_balance():
    account = BankAccount(1000)
    assert account.balance == 1000


def test_deposit():
    account = BankAccount(1000)
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw():
    account = BankAccount(1000)
    account.withdraw(200)
    assert account.balance == 800


def test_withdraw_more_than_balance():
    account = BankAccount(1000)

    with pytest.raises(ValueError):
        account.withdraw(1500)


def test_deposit_negative_money():
    account = BankAccount(1000)

    with pytest.raises(ValueError):
        account.deposit(-100)