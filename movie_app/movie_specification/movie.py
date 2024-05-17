from abc import ABC, abstractmethod


class Movie(ABC):

    MIN_YEAR = 1888

    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if value < Movie.MIN_YEAR:
            raise ValueError(f"Movies weren't made before {Movie.MIN_YEAR}!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        if not value.__class__.__name__ == 'User':
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value

    @abstractmethod
    def details(self):
        ...
