from food_orders_app.meals.meal import Meal


class MainDish(Meal):

    QUANTITY = 50

    def __init__(self, name: str, price: float, quantity: int = None):
        super().__init__(name, price, quantity)
        self.quantity = quantity if quantity else MainDish.QUANTITY

    def details(self):
        return f'Main Dish {self.name}: {self.price:.2f}lv/piece'
