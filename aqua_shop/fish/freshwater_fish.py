from aqua_shop.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    SIZE = 3
    SIZE_INCREASING = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, FreshwaterFish.SIZE, price)
