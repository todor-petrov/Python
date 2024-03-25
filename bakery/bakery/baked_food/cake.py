from bakery.baked_food.baked_food import BakedFood


class Cake(BakedFood):

    PORTION = 245.0

    def __init__(self, name: str, price: float, portion: float = PORTION):
        super().__init__(name, portion, price)
