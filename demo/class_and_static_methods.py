# 01. Calculator
"""
from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)
"""


# 02. Shop
"""
class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        return Shop(name, shop_type, capacity=10)

    def add_item(self, item_name: str):
        if sum(self.items.values()) < self.capacity:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f'{item_name} added to the shop'
        return f'Not enough capacity in the shop'

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'
"""



