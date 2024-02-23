from robots.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    WEIGHT = 9
    INCREASING_WEIGHT = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=MaleRobot.WEIGHT)

    def eating(self):
        self.weight += MaleRobot.INCREASING_WEIGHT