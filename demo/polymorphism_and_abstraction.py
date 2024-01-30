# 02. ImageArea
"""
class ImageArea:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()
"""

# 03. Playing
"""
def start_playing(instance):
    return instance.play()
"""

# 04. Shapes
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        ...

    @abstractmethod
    def calculate_perimeter(self):
        ...


class Circle(Shape):
    
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)
"""

# 01. Vehicles
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance: int):
        ...

    @abstractmethod
    def refuel(self, fuel: int):
        ...


class Car(Vehicle):

    AIR_CONDITION_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        needed_fuel = (self.fuel_consumption + Car.AIR_CONDITION_CONSUMPTION) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    AIR_CONDITION_CONSUMPTION = 1.6
    FUEL_LOSES_COEFFICIENT = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        needed_fuel = (self.fuel_consumption + Truck.AIR_CONDITION_CONSUMPTION) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * Truck.FUEL_LOSES_COEFFICIENT
"""

# 02. Groups
"""
class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group_name = f'{self.name} {other.name}'
        new_group_people = self.people + other.people
        return Group(new_group_name, new_group_people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(p.__repr__() for p in self.people)}"

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item].__repr__()}'
"""


# 03. Account
"""
class Account:

    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount if amount != 0 else 0
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')
        self._transactions.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        return self.handle_transaction(amount)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        account = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        account._transactions = self._transactions + other._transactions
        return account
"""


