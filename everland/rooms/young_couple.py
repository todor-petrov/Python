from everland.rooms.room import Room
from everland.appliances.tv import TV
from everland.appliances.fridge import Fridge
from everland.appliances.laptop import Laptop


class YoungCouple(Room):

    ROOM_COST = 20
    MEMBERS_COUNT = 2
    APPLIANCES = [TV(), Fridge(), Laptop()] * MEMBERS_COUNT

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=YoungCouple.MEMBERS_COUNT)
        self.room_cost = YoungCouple.ROOM_COST
        self.appliances = YoungCouple.APPLIANCES
        self.calculate_expenses(self.appliances)
