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

    def get_statistics(self):
        self.budget = f'{self.budget:.2f}'
        total_equipment_price = f'{sum([el.price for el in self.equipment]):.2f}'
        protections = [el.protection for el in self.equipment]
        avg_protection = floor(sum(protections) / len(protections))
