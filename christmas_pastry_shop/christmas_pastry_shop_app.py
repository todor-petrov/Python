from christmas_pastry_shop.booths.open_booth import OpenBooth
from christmas_pastry_shop.booths.private_booth import PrivateBooth
from christmas_pastry_shop.delicacies.gingerbread import Gingerbread
from christmas_pastry_shop.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    DELICACIES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    BOOTHS = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):

        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if name in [d.name for d in self.delicacies]:
            raise Exception(f'{name} already exists!')

        if type_delicacy not in ChristmasPastryShopApp.DELICACIES:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        delicacy = ChristmasPastryShopApp.DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth not in ChristmasPastryShopApp.BOOTHS:
            raise Exception(f'{type_booth} is not a valid booth!')

        booth = ChristmasPastryShopApp.BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):

        available_booths = [b for b in self.booths if not b.is_reserved and number_of_people <= b.capacity]
        booth = available_booths[0] if available_booths else None

        if not booth:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = self._find_booth_by_booth_number(booth_number)
        delicacy = self._find_delicacy_by_name(delicacy_name)

        if not booth:
            raise Exception(f'Could not find booth {booth_number}!')

        if not delicacy:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):

        booth = self._find_booth_by_booth_number(booth_number)
        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0

        return f'Booth {booth_number}:\nBill: {bill:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'

    def _find_booth_by_booth_number(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        return booth[0] if booth else None

    def _find_delicacy_by_name(self, delicacy_name):
        delicacy = [d for d in self.delicacies if d.name == delicacy_name]
        return delicacy[0] if delicacy else None
