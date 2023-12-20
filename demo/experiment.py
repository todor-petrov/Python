# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages


# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model
#         self.engine = engine

#     def get_info(self):
#         return f'This is {self.name} {self.model} with engine {self.engine}'


# class Music:
#     def __init__(self, title, artist, lyrics):
#         self.title = title
#         self.artist = artist
#         self.lyrics = lyrics

#     def print_info(self):
#         return f'This is "{self.title}" from "{self.artist}"'
    
#     def play(self):
#         return self.lyrics


# class Shop:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items

#     def get_items_count(self):
#         return len(self.items)
    

# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def defend(self, damage):
#         if self.health - damage <= 0:
#            self.health = 0
#            return f'{self.name} was defeated'
#         self.health -= damage

#     def heal(self, amount):
#         self.health += amount


# class Employee:
#     def __init__(self, id, first_name, last_name, salary):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
#     def get_annual_salary(self):
#         return self.salary * 12
    
#     def raise_salary(self, amount):
#         self.salary += amount
#         return self.salary


