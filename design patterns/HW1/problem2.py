"""
## Problem 2
Use Factory Method pattern to create 2 different classes PersonalAccount and
BusinessAccount of type BankAccount having a method CreateAccount with some
implementation of your choice. Have a BankAccountFactory class and a Client class and allow
the Client to ask the factory to create an account. The type of the account should be determined
based on the client’s input. You can decide what should be the client input and how the factory
class should determine what type of an account to create.
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_account(self, *args, **kwargs):
        pass


class PersonalAccount(BankAccount):
    def __init__(self, name: str, limit: int, region: str, premium: bool):
        self.name = name
        self.limit = limit
        self.region = region
        self.premium = premium

    'class instantiation'
    @classmethod
    def create_account(cls, name: str, limit: int, region: str, premium: bool):
        return cls(name, limit, region, premium)


class BusinessAccount(BankAccount):
    def __init__(self, organization: str, limit: int, region: str, premium: bool, staff_size: int):
        self.org = organization
        self.limit = limit
        self.region = region
        self.premium = premium
        self.staff_size = staff_size

    @classmethod
    def create_account(cls, organization: str, limit: int, region: str, premium: bool, staff_size: int):
        cls(organization, limit, region, premium, staff_size)


class BankAccountFactory:
    ACCOUNTS = {
        'personal': PersonalAccount,
        'business': BusinessAccount,
    }

    @classmethod
    def open_account(cls, acc_type: str, **kwargs):
        return cls.ACCOUNTS[acc_type](**kwargs)


class Client:

    @staticmethod
    def create_account(acc_type: str, **kwargs) -> BankAccount:
        account = BankAccountFactory.open_account(acc_type, **kwargs)
        return account


if __name__ == '__main__':
    client = Client()
    personal_acc = {'name': 'John Smith', 'limit': 1000000, 'region': 'Canada', 'premium': True}
    personal_account = client.create_account('personal', **personal_acc)
    print(type(personal_account))
