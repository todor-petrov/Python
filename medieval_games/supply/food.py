from medieval_games.supply.supply import Supply


class Food(Supply):

    ENERGY = 25

    def __init__(self, name: str, energy: int = ENERGY):
        super().__init__(name, energy)

    def details(self):
        return f'{self.__class__.__name__}: {self.name}, {self.energy}'
