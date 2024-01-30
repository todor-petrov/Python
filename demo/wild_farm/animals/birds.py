from wild_farm.animals.animal import Bird
from wild_farm.food import Food


class Owl(Bird):

    WEIGHT_INCREASING = 0.25

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * Owl.WEIGHT_INCREASING
        self.food_eaten += food.quantity


class Hen(Bird):

    WEIGHT_INCREASING = 0.35

    def make_sound(self):
        return 'Cluck'

    def feed(self, food: Food):
        self.weight += food.quantity * Hen.WEIGHT_INCREASING
        self.food_eaten += food.quantity
