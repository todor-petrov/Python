# 01. Calculator
"""
from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)
"""

# 02. Shop
"""
class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        return Shop(name, shop_type, capacity=10)

    def add_item(self, item_name: str):
        if sum(self.items.values()) < self.capacity:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f'{item_name} added to the shop'
        return f'Not enough capacity in the shop'

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'
"""

# 03. Integer
"""
class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        float_value = int(float_value)
        return Integer(float_value)

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        for i in range(len(value) - 1, -1, -1):
            num = roman[value[i]]
            if 3 * num < summ:
                summ = summ - num
            else:
                summ = summ + num
        return Integer(summ)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        return Integer(int(value))
"""


# 01. Photo Album
"""
class PhotoAlbum:

    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        album_pages = photos_count // PhotoAlbum.MAX_PHOTOS_ON_PAGE
        if photos_count % PhotoAlbum.MAX_PHOTOS_ON_PAGE != 0:
            album_pages += 1
        return cls(album_pages)

    def add_photo(self, label: str):
        if sum([len(x) for x in self.photos]) == PhotoAlbum.MAX_PHOTOS_ON_PAGE * self.pages:
            return 'No more free slots'
        for page in self.photos:
            if len(page) < PhotoAlbum.MAX_PHOTOS_ON_PAGE:
                page.append(label)
                page_number = self.photos.index(page) + 1
                slot_number = self.photos[page_number - 1].index(label) + 1
                return f'{label} photo added successfully on page {page_number} slot {slot_number}'

    def display(self):
        my_album = ['-----------']
        for page in range(self.pages):
            if len(self.photos[page]) > 0:
                my_album.append(' '.join('[]' for x in self.photos[page]))
                my_album.append('-----------')
            else:
                my_album.append('\n' + '-----------')
        return '\n'.join(my_album)
"""
