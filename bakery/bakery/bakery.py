from bakery.baked_food.bread import Bread
from bakery.baked_food.cake import Cake
from bakery.drink.tea import Tea
from bakery.drink.water import Water
from bakery.table.inside_table import InsideTable
from bakery.table.outside_table import OutsideTable


class Bakery:

    FOODS = {'Bread': Bread, 'Cake': Cake}
    DRINKS = {'Tea': Tea, 'Water': Water}
    TABLES = {'InsideTable': InsideTable, 'OutsideTable': OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0.0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        if food_type not in Bakery.FOODS:
            return

        food = Bakery.FOODS[food_type](name, price)

        if food.name in [f.name for f in self.food_menu]:
            raise Exception(f'{food_type} {name} is already in the menu!')

        self.food_menu.append(food)
        return f'Added {food.name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):

        if drink_type not in Bakery.DRINKS:
            return

        drink = Bakery.DRINKS[drink_type](name, portion, brand)

        if drink.name in [d.name for d in self.drinks_menu]:
            raise Exception(f'{drink_type} {name} is already in the menu!')

        self.drinks_menu.append(drink)
        return f'Added {drink.name} ({drink.brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):

        if table_type not in Bakery.TABLES:
            return

        table = Bakery.TABLES[table_type](table_number, capacity)

        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f'Table {table_number} is already in the bakery!')

        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):

        tables = [t for t in self.tables_repository if number_of_people <= t.capacity and not t.is_reserved]

        if not tables:
            return f'No available table for {number_of_people} people'

        table = tables[0]
        table.reserve(number_of_people)
        return f'Table {table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number: int, *food_names):

        table = self._find_table_by_table_number(table_number)
        unavailable_foods = []

        if not table:
            return f'Could not find table {table_number}'

        for food_name in food_names:
            food = self._find_food_by_food_name(food_name)
            if not food:
                unavailable_foods.append(food_name)
            else:
                table.order_food(food)

        food_order_info = [f'Table {table_number} ordered:']
        food_order_info.extend([f.__repr__() for f in table.food_orders])
        food_order_info.append(f'{self.name} does not have in the menu:')
        food_order_info.extend(unavailable_foods)

        return '\n'.join(food_order_info)

    def order_drink(self, table_number: int, *drinks_names):

        table = self._find_table_by_table_number(table_number)
        unavailable_drinks = []

        if not table:
            return f'Could not find table {table_number}'

        for drink_name in drinks_names:
            drink = self._find_drink_by_drink_name(drink_name)
            if not drink:
                unavailable_drinks.append(drink_name)
            else:
                table.order_drink(drink)

        drink_order_info = [f'Table {table_number} ordered:']
        drink_order_info.extend([d.__repr__() for d in table.drink_orders])
        drink_order_info.append(f'{self.name} does not have in the menu:')
        drink_order_info.extend(unavailable_drinks)

        return '\n'.join(drink_order_info)

    def leave_table(self, table_number: int):

        table = self._find_table_by_table_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()

        return f'Table: {table_number}' + '\n' + f'Bill: {table_bill:.2f}'

    def get_free_tables_info(self):

        return '\n'.join(t.free_table_info() for t in self.tables_repository)

    def get_total_income(self):

        return f'Total income: {self.total_income:.2f}lv'

    def _find_table_by_table_number(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        return table[0] if table else None

    def _find_food_by_food_name(self, food_name):
        food = [f for f in self.food_menu if f.name == food_name]
        return food[0] if food else None

    def _find_drink_by_drink_name(self, drink_name):
        drink = [d for d in self.drinks_menu if d.name == drink_name]
        return drink[0] if drink else None
