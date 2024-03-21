from bakery.drink.drink import Drink


class Tea(Drink):

    PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str, price: float = PRICE):
        super().__init__(name, portion, price, brand)
