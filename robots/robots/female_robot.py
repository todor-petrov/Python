from robots.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    WEIGHT = 7
    INCREASING_WEIGHT = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=FemaleRobot.WEIGHT)

    def eating(self):
        self.weight += FemaleRobot.INCREASING_WEIGHT
