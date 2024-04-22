from food_orders_app.meals.meal import Meal


class Starter(Meal):

    QUANTITY = 60

    def __init__(self, name: str, price: float, quantity: int = None):
        super().__init__(name, price, quantity)
        self.quantity = quantity if quantity else Starter.QUANTITY

    def details(self):
        return f'Starter {self.name}: {self.price:.2f}lv/piece'
