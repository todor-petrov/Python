from everland.rooms.room import Room
from everland.appliances.tv import TV


class AloneYoung(Room):

    ROOM_COST = 10
    MEMBERS_COUNT = 1
    APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(name=family_name, budget=salary, members_count=AloneYoung.MEMBERS_COUNT)
        self.room_cost = AloneYoung.ROOM_COST
        self.appliances = AloneYoung.APPLIANCES
        self.calculate_expenses(self.appliances)
