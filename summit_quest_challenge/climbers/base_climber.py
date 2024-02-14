from abc import ABC, abstractmethod


class BaseClimber(ABC):

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Climber name cannot be null or empty!')
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError('')