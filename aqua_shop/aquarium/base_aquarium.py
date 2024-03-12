from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        ...

    def calculate_comfort(self):

        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):

        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'

        if not self.fish_type == fish.__class__.__name__:
            return 'Water not suitable.'
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        return (f"{self.name}:\n"
                f"Fish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}\n"
                f"Decorations: {len(self.decorations)}\n"
                f"Comfort: {self.calculate_comfort()}")
