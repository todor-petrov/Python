from abc import ABC, abstractmethod


class Musician(ABC):

    AGE_RESTRICTION = 16

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Musician name cannot be empty!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < Musician.AGE_RESTRICTION:
            raise ValueError('Musicians should be at least 16 years old!')
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill):
        ...
