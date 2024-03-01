from christmas_pastry_shop.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):

    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.PORTION, price)

    def details(self):
        return f'Gingerbread {self.name}: {Gingerbread.PORTION}g - {self.price:.2f}lv.'
