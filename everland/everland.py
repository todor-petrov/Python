from everland.people.child import Child
from everland.rooms.room import Room
from everland.rooms.young_couple import YoungCouple
from everland.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:

    def __init__(self):
        self.rooms = []
        self.monthly_consumptions = 0

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):

        total_consumption = sum(room.expenses for room in self.rooms)
        total_consumption += sum(room.room_cost for room in self.rooms)
        return f'Monthly consumption: {total_consumption:.2f}$.'

    def pay(self):

        payment_info = []

        for room in self.rooms:
            expenses = room.expenses + room.room_cost

            if expenses <= room.budget:
                room.budget -= expenses
                payment_info.append(f'{room.family_name} paid {expenses:.2f}$ '
                                    f'and have {room.budget:.2f}$ left.')

            else:
                self.rooms.remove(room)
                payment_info.append(f'{room.family_name} does not have enough '
                                    f'budget and must leave the hotel.')

        return '\n'.join(payment_info)

    def status(self):

        status_info = [f'Total population: {sum(r.members_count for r in self.rooms)}']

        for room in self.rooms:

            status_info.append(f'{room.family_name} with {room.members_count} members. '
                               f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$')
            if room.children:
                for c in range(len(room.children)):
                    status_info.append(f'--- Child {c+1} monthly cost: {room.children[c].get_monthly_expense():.2f}$')

            appliances_cost = sum(a.get_monthly_expense() for a in room.appliances)
            status_info.append(f'--- Appliances monthly cost: {appliances_cost:.2f}$')

        return '\n'.join(status_info)


everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
