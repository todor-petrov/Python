from everland.rooms.room import Room
from everland.appliances.tv import TV
from everland.appliances.fridge import Fridge
from everland.appliances.stove import Stove


class OldCouple(Room):

    ROOM_COST = 15
    MEMBERS_COUNT = 2
    APPLIANCES = [TV(), Fridge(), Stove()] * MEMBERS_COUNT

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(name=family_name, budget=pension_one + pension_two, members_count=OldCouple.MEMBERS_COUNT)
        self.room_cost = OldCouple.ROOM_COST
        self.appliances = OldCouple.APPLIANCES
        self.calculate_expenses(self.appliances)
