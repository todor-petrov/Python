from food_orders_app.client import Client
from food_orders_app.meals.dessert import Dessert
from food_orders_app.meals.main_dish import MainDish
from food_orders_app.meals.meal import Meal
from food_orders_app.meals.starter import Starter


class FoodOrdersApp:

    MEALS = {'Starter': Starter, 'MainDish': MainDish, 'Dessert': Dessert}
    MENU_MINIMUM = 5

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):

        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception('The client has already been registered!')

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f'Client {client.phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        self.menu.extend([m for m in meals if m.__class__.__name__ in FoodOrdersApp.MEALS])

    def show_menu(self):

        if len(self.menu) < FoodOrdersApp.MENU_MINIMUM:
            raise Exception('The menu is not ready!')

        return '\n'.join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, ** meal_names_and_quantities):

        if len(self.menu) < FoodOrdersApp.MENU_MINIMUM:
            raise Exception('The menu is not ready!')

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))
        client = self._find_client_by_phone_number(client_phone_number)

        for meal in meal_names_and_quantities:
            if meal not in [m.name for m in self.menu]:
                raise Exception(f'{meal} is not on the menu!')

        for meal, quantity in meal_names_and_quantities.items():
            menu_meal = [m for m in self.menu if meal == m.name][0]
            if menu_meal.quantity < quantity:
                raise Exception(f'Not enough quantity of {menu_meal.__class__.__name__}: {meal}!')

        for meal, quantity in meal_names_and_quantities.items():
            menu_meal = [m for m in self.menu if m.name == meal][0]
            client_meal = FoodOrdersApp.MEALS[menu_meal.__class__.__name__](menu_meal.name, menu_meal.price, quantity)
            menu_meal.quantity -= quantity
            client.shopping_cart.append(client_meal)

        client.bill = sum([m.price * m.quantity for m in client.shopping_cart])
        client_meals = [m.name for m in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(client_meals)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client = self._find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        for meal in client.shopping_cart:
            menu_meal = [m for m in self.menu if m.name == meal.name][0]
            menu_meal.quantity += meal.quantity

        client.bill = 0.0
        client.shopping_cart = []
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        total_paid_money = client.bill
        client.bill = 0.0
        client.shopping_cart = []
        receipt_id = self.get_receipt_id()

        return (f'Receipt #{receipt_id} with total amount of {total_paid_money:.2f} '
                f'was successfully paid for {client_phone_number}.')

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'

    def _find_client_by_phone_number(self, client_phone_number):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        return client[0] if client else None

    def get_receipt_id(self):
        self.receipt_id += 1
        return self.receipt_id
