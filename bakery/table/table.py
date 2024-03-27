from bakery.baked_food.baked_food import BakedFood
from bakery.drink.drink import Drink


class Table:

    MIN_CAPACITY = 0

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f'Capacity has to be greater than {Table.MIN_CAPACITY}!')
        self.__capacity = value

    def reserve(self, number_of_people: int):

        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):

        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):

        self.drink_orders.append(drink)

    def get_bill(self):

        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):

        self.food_orders, self.drink_orders = [], []
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        free_table_info = [f'Table: {self.table_number}',
                           f'Type: {self.__class__.__name__}',
                           f'Capacity: {self.capacity}']
        return '\n'.join(free_table_info) if not self.is_reserved else None
