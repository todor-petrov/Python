from wild_farm.animals.animal import Mammal
from wild_farm.food import Food


class Mouse(Mammal):

    WEIGHT_INCREASING = 0.10

    def make_sound(self):
        return 'Squeak'

    def feed(self, food: Food):
        if food.__class__.__name__ not in ['Vegetable', 'Fruit']:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * Mouse.WEIGHT_INCREASING
        self.food_eaten += food.quantity


class Dog(Mammal):

    WEIGHT_INCREASING = 0.40

    def make_sound(self):
        return 'Woof!'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * Dog.WEIGHT_INCREASING
        self.food_eaten += food.quantity


class Cat(Mammal):

    WEIGHT_INCREASING = 0.30

    def make_sound(self):
        return 'Meow'

    def feed(self, food: Food):
        if food.__class__.__name__ not in ['Vegetable', 'Meat']:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * Cat.WEIGHT_INCREASING
        self.food_eaten += food.quantity


class Tiger(Mammal):

    WEIGHT_INCREASING = 1.00

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * Tiger.WEIGHT_INCREASING
        self.food_eaten += food.quantity
