from abc import ABC, abstractmethod


class Car(ABC):

    MODEL_MIN_LENGTH = 4

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if len(value) < Car.MODEL_MIN_LENGTH:
            raise ValueError(f'Model {value} is less than 4 symbols!')
        self.__model = value
