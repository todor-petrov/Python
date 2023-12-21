# class Vehicle:
#     def __init__(self, mileage, max_speed=150):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets = []


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def set_x(self, new_x):
#         self.x = new_x

#     def set_y(self, new_y):
#         self.y = new_y

#     def __str__(self):
#         return f'The point has coordinates ({self.x},{self.y})'
    

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

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

#     def fill(self, ml):
#         if self.content + ml <= Glass.capacity:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
    
#     def empty(self):
#         self.content = 0
#         return 'Glass is now empty'
    
#     def info(self):
#         return f'{Glass.capacity - self.content} ml left'
    

# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False

#     def power(self):
#         if not self.is_on:
#             self.is_on = True
#         else:
#             self.is_on = False

#     def install(self, app, app_memory):
#         if self.memory >= app_memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f'Installing {app}'
#         if self.memory >= app_memory and not self.is_on:
#             return f'Turn on your phone to install {app}'
#         if self.memory < app_memory:
#             return f'Not enough memory to install {app}'
        
#     def status(self):
#         return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'
