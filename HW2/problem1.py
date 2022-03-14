"""
## Problem 1
You know that each BankAccount object has attributes id, balance and rate. Use builder pattern
and any extra classes and methods that you may need to realize the creation of a BankAccount type
object. Create some objects and do some operations to test your classes.
"""
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def account(self) -> None:
        pass

    @abstractmethod
    def add_id(self, *args) -> None:
        pass

    @abstractmethod
    def add_balance(self, *args) -> None:
        pass

    @abstractmethod
    def add_rate(self, *args) -> None:
        pass


class GoodBuilder(Builder):
    def __init__(self) -> None:
        self._account = None
        self.create_default_account()

    def create_default_account(self) -> None:
        self._account = BankAccount()

    @property
    def account(self) -> None:
        account = self._account
        id = self._account.id
        print('Account id: ', id)
        self.create_default_account()
        return account

    def add_id(self, value: str) -> None:
        self._account.id = value

    def add_balance(self, value: float) -> None:
        self._account.balance = value

    def add_rate(self, value: float) -> None:
        self._account.rate = value


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def create_full_account(self, auth_id, balance, rate):
        self.builder.add_id(auth_id)
        self.builder.add_balance(balance)
        self.builder.add_rate(rate)

    def create_faulty_account(self, auth_id, balance, rate):
        """This one fails to create a fully operational account due to directors wrong instructions."""
        self.builder.add_balance(balance)
        self.builder.add_rate(rate)


class BankAccount:
    def __init__(self):
        self._id = None
        self._rate = None
        self._balance = None

    @property
    def id(self):
        if self._id is None:
            print('Error! Identification failed.')
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


if __name__ == '__main__':
    director = Director()
    builder = GoodBuilder()
    director.builder = builder
    director.create_full_account('good_account_1334', 50000.0, .2)
    good_account = builder.account
    director.create_faulty_account('this_will_go_wrong', 10000.0, .1)
    bad_account = builder.account

