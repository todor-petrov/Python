from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @abstractmethod
    def miss(self, time_to_catch: int):
        ...

    @abstractmethod
    def renew_oxy(self):
        ...

    def hit(self, fish: BaseFish):
        if (self.oxygen_level - fish.time_to_catch) < 0:
            self.oxygen_level = 0
        self.oxygen_level -= fish.time_to_catch
        self.catch.append(fish)
        self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f'{self.__class__.__name__}: '
                f'[Name: {self.name}, '
                f'Oxygen level left: {self.oxygen_level}, '
                f'Fish caught: {len(self.catch)}, '
                f'Points earned: {self.competition_points}]')
