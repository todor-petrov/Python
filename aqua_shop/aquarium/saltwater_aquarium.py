from aqua_shop.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):

    CAPACITY = 25
    FISH_TYPE = 'SaltwaterFish'

    def __init__(self, name: str):
        super().__init__(name, capacity=SaltwaterAquarium.CAPACITY)

    @property
    def fish_type(self):
        return SaltwaterAquarium.FISH_TYPE
