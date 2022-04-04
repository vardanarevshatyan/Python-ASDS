"""
## Problem 2
Imagine that you have a customer who wants to order some food, a waiter and a chef. Use command design pattern and classes of
your choice to implement this logic. The main operation will be ordering the food, the waiter will decide (depending on the order)
if the order should be cooked by the chef or is it something they already have pre-made and should just be served to the client.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class OrderCommand(Command):
    def __init__(self, food: str, waiter: Waiter):
        self.food = food
        self.waiter = waiter

    def execute(self):
        print(f"Ordering {self.food}")
        self.waiter.process_order(self.food)


class Waiter:
    def __init__(self, cook: Cook, available_meals: Meal) -> None:
        self.cook = cook
        self.available_meals = available_meals

    def process_order(self, order) -> None:
        if self.available_meals.is_available(order):
            print(f"{order} is available, serving it to the client")
        else:
            print(f"{order} is not available, cooking it")
            self.cook.prepare_meal(order)


class Cook:
    def prepare_meal(self, order: str) -> None:
        print(f"Cook is preparing {order}")


class Meal:
    def __init__(self, available_meal: list) -> None:
        self.available_meal = available_meal

    def is_available(self, order: str) -> bool:
        return order in self.available_meal


class Customer:
    def order_food(self, food: str, waiter: Waiter) -> None:
        command = OrderCommand(food, waiter)
        command.execute()


if __name__ == "__main__":
    cook = Cook()
    meal = Meal(["pizza", "burger", "chicken"])
    waiter = Waiter(cook, meal)
    john = Customer()
    john.order_food("pizza", waiter)
    john.order_food("lemonade", waiter)
