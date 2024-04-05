from everland.appliances.appliance import Appliance


class TV(Appliance):

    COST = 1.5

    def __init__(self):
        super().__init__(cost=TV.COST)