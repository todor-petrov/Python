from abc import ABC, abstractmethod


class Horse(ABC):

    MAX_SPEED = 0
    HORSE_NAME_MIN_LENGTH = 4

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value.strip()) < self.HORSE_NAME_MIN_LENGTH:
            raise ValueError(f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if self.MAX_SPEED < value:
            raise ValueError('Horse speed is too high!')
        self.__speed = value

    @abstractmethod
    def train(self):
        ...
