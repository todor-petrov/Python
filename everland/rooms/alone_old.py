from everland.rooms.room import Room


class AloneOld(Room):

    ROOM_COST = 10
    MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(name=family_name, budget=pension, members_count=AloneOld.MEMBERS_COUNT)
        self.room_cost = AloneOld.ROOM_COST
