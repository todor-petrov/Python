from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @abstractmethod
    def win(self):
        ...

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == ' ':
            raise ValueError('Team name cannot be empty!')
        self._name = value

    def get_statistics(self):
        total_equipment_price = sum([el.price for el in self.equipment])
        protections = [el.protection for el in self.equipment]
        avg_protection = floor(sum(protections) / len(protections))
        return (f'Name: {self.name}\n'
                f'Country: {self.country}\n'
                f'Advantage: {self.advantage} points\n'
                f'Budget: {self.budget:.2f}EUR\n'
                f'Wins: {self.wins}\n'
                f'Total Equipment Price: {total_equipment_price:.2f}\n'
                f'Average Protection: {floor(avg_protection)}')
