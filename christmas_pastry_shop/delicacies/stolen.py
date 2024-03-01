from christmas_pastry_shop.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    PORTION = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.PORTION, price)

    def details(self):
        return f'Stolen {self.name}: {Stolen.PORTION}g - {self.price:.2f}lv.'
