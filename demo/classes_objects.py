# class Vehicle:
#     def __init__(self, mileage, max_speed=150):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets = []


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f'The point has coordinates ({self.x},{self.y})'
    

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#     def get_area(self):
#         return Circle.pi * self.radius ** 2
#     def get_circumference(self):
#         return 2 * Circle.pi * self.radius
    

# class Glass:
#     capacity = 250
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if self.content + ml <= Glass.capacity:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return 'Glass is now empty'
#
#     def info(self):
#         return f'{Glass.capacity - self.content} ml left'
    

# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         if not self.is_on:
#             self.is_on = True
#         else:
#             self.is_on = False
#
#     def install(self, app, app_memory):
#         if self.memory >= app_memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f'Installing {app}'
#         if self.memory >= app_memory and not self.is_on:
#             return f'Turn on your phone to install {app}'
#         if self.memory < app_memory:
#             return f'Not enough memory to install {app}'
#
#     def status(self):
#         return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


# class Vet:
#
#     animals = []
#     space = 5
#
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if len(Vet.animals) < Vet.space:
#             self.animals.append(animal_name)
#             Vet.animals.append(animal_name)
#             return f'{animal_name} registered in the clinic'
#         return 'Not enough space'
#
#     def unregister_animal(self, animal_name):
#         if animal_name in Vet.animals:
#             Vet.animals.remove(animal_name)
#             self.animals.remove(animal_name)
#             return f'{animal_name} unregistered successfully'
#         return f'{animal_name} not in the clinic'
#
#     def info(self):
#         space_left_in_clinic = Vet.space - len(Vet.animals)
#         return f'{self.name} has {len(self.animals)} animals. {space_left_in_clinic} space left in clinic'


# class Time:
#
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
#
#     def next_second(self):
#
#         self.seconds += 1
#         if self.seconds > Time.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes > Time.max_minutes:
#                 self.minutes = 0
#                 self.hours += 1
#                 if self.hours > Time.max_hours:
#                     self.hours = 0
#         return self.get_time()


# class Account:
#     def __init__(self, user_id, name, balance=0):
#         self.id = user_id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         return 'Amount exceeded balance'
#
#     def info(self):
#         return f'User {self.name} with account {self.id} has {self.balance} balance'


# class PizzaDelivery:
#
#     def __init__(self, name: str, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = 0
#         self.ingredients[ingredient] += quantity
#         self.price += quantity * price_per_quantity
#
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
#         if ingredient not in self.ingredients:
#             return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
#         if self.ingredients[ingredient] < quantity:
#             return f'Please check again the desired quantity of {ingredient}!'
#         self.ingredients[ingredient] -= quantity
#         self.price -= quantity * price_per_quantity
#
#     def make_order(self):
#         self.ordered = True
#         ordered_ingredients = []
#         for k, v in self.ingredients.items():
#             ordered_ingredients.append(f'{k}: {v}')
#         return (f"You've ordered pizza {self.name} prepared with {', '.join(ordered_ingredients)} "
#                 f"and the price will be {self.price}lv.")

