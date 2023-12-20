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


# class Cup:
#     def __init__(self, size, quantity):
#          self.size = size
#          self.quantity = quantity

#     def fill(self, quantity):
#         if self.quantity + quantity <= self.size:
#             self.quantity += quantity

#     def status(self):
#         return self.size - self.quantity
    

# class Flower:
#     def __init__(self, name, water_requirements):
#         self.name = name
#         self.water_requirements = water_requirements
#         self.is_happy = False
        
#     def water(self, quantity):
#         if quantity >= self.water_requirements:
#             self.is_happy = True
#             return
#         self.is_happy = False
        
#     def status(self):
#         if self.is_happy:
#             return f'{self.name} is happy'
#         return f'{self.name} is not happy'
    

# class SteamUser:
#     def __init__(self, username, games):
#         self.username = username
#         self.games = games
#         self.played_hours = 0

#     def play(self, game, hours):
#         if game in self.games:
#             self.played_hours += hours
#             return f'{self.username} is playing {game}'
#         return f'{game} is not in library'
#     def buy_game(self, game):
#         if game in self.games:
#             return f'{game} is already in your library'
#         self.games.append(game)
#         return f'{self.username} bought {game}'
    
#     def status(self):
#         return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'
    
    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and self.language != new_language:
            previous_language = self.language
            self.language = new_language
            return f'{self.name} switched from {previous_language} to {self.language}'
        if self.skills >= skills_needed and self.language == new_language:
            return f'{self.name} already knows {self.language}'
        if self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'
        

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

