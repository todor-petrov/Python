from aqua_shop.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):

    COMFORT = 1
    PRICE = 5.0

    def __init__(self):
        super().__init__(comfort=Ornament.COMFORT, price=Ornament.PRICE)
