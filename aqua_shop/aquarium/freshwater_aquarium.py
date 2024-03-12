from aqua_shop.aquarium.base_aquarium import BaseAquarium
from aqua_shop.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):

    CAPACITY = 50
    FISH_TYPE = 'FreshwaterFish'

    def __init__(self, name: str):
        super().__init__(name, capacity=FreshwaterAquarium.CAPACITY)

    @property
    def fish_type(self):
        return FreshwaterFish.__name__
