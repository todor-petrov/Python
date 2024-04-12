from everland.rooms.room import Room
from everland.appliances.tv import TV
from everland.appliances.fridge import Fridge
from everland.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):

    ROOM_COST = 30
    PARENTS = 2
    APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one + salary_two,
                         members_count=YoungCoupleWithChildren.PARENTS + len(children))
        self.room_cost = YoungCoupleWithChildren.ROOM_COST
        self.appliances = (YoungCoupleWithChildren.APPLIANCES *
                           (YoungCoupleWithChildren.PARENTS + len(children)))
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)
