from hotel_rooms.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        return [r for r in self.rooms if r.number == room_number][0].take_room(people)

    def free_room(self, room_number):
        return [r for r in self.rooms if r.number == room_number][0].free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if r.is_taken is False]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken is True]
        hotel_data = [f"Hotel {self.name} has {self.guests} total guests",
                      f"Free rooms: {', '.join(free_rooms)}",
                      f"Taken rooms: {', '.join(taken_rooms)}"]
        return '\n'.join(hotel_data)
