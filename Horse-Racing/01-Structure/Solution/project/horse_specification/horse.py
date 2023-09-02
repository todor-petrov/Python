from abc import ABC, abstractmethod


class Horse(ABC):

    MAX_SPEED = None
    INCREMENT_BY_TRAINING = 2

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED:
            raise ValueError('Horse speed is too high!')
        self.__speed = value

    def train(self):
        self.speed += self.INCREMENT_BY_TRAINING
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
