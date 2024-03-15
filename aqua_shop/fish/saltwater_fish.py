from aqua_shop.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    SIZE = 5
    SIZE_INCREASING = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, SaltwaterFish.SIZE, price)
