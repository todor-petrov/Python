from abc import ABC, abstractmethod

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):

    CLIMBER_STRENGTH_INCREASING = 15

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

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
            raise ValueError('A climber cannot have negative strength or strength equal to 0!')
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        ...

    @abstractmethod
    def climb(self, peak: BasePeak):
        ...

    def rest(self):
        self.strength += BaseClimber.CLIMBER_STRENGTH_INCREASING

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"/// Climber name: {self.name} * "
                f"Left strength: {self.strength} * "
                f"Conquered peaks: {', '.join(self.conquered_peaks)} ///")
