from everland.appliances.appliance import Appliance


class Laptop(Appliance):

    COST = 1.0

    def __init__(self):
        super().__init__(cost=Laptop.COST)
