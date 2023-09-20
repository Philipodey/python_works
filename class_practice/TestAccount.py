from unittest import TestCase

from class_practice.Account import Account


class TestAccount (TestCase):
    def test_That_Account_Can_Deposit_Money(self):
        savings_Account = Account()