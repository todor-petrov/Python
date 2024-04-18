from food_orders_app.meals.meal import Meal


class Dessert(Meal):

    QUANTITY = 30

    def __init__(self, name: str, price: float, quantity: int = None):
        super().__init__(name, price, quantity)
        self.quantity = quantity if quantity else Dessert.QUANTITY

    def details(self):
        return f'Dessert {self.name}: {self.price:.2f}lv/piece'
