class Player:
    added_names = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
    
    @property
    def need_sustenance(self):
        return True if self.stamina < 100 else None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name not valid!')
        if value in self.added_names:
            raise Exception(f'Name {value} is already used!')
        self.__name = value
        self.added_names.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError('The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 > value or value > 100:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'
