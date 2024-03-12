from aqua_shop.aquarium.freshwater_aquarium import FreshwaterAquarium
from aqua_shop.aquarium.saltwater_aquarium import SaltwaterAquarium
from aqua_shop.decoration.decoration_repository import DecorationRepository
from aqua_shop.decoration.ornament import Ornament
from aqua_shop.decoration.plant import Plant
from aqua_shop.fish.freshwater_fish import FreshwaterFish
from aqua_shop.fish.saltwater_fish import SaltwaterFish


class Controller:

    AQUARIUMS = {'FreshwaterAquarium': FreshwaterAquarium, 'SaltwaterAquarium': SaltwaterAquarium}
    DECORATIONS = {'Ornament': Ornament, 'Plant': Plant}
    FISH = {'FreshwaterFish': FreshwaterFish, 'SaltwaterFish': SaltwaterFish}

    def __init__(self):

        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):

        if aquarium_type not in Controller.AQUARIUMS:
            return 'Invalid aquarium type.'

        self.aquariums.append(Controller.AQUARIUMS[aquarium_type](aquarium_name))
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):

        if decoration_type not in Controller.DECORATIONS:
            return 'Invalid decoration type.'

        decoration = Controller.DECORATIONS[decoration_type]()
        self.decorations_repository.decorations.append(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        aquarium = self._find_aquarium_by_name(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        if fish_type not in Controller.FISH:
            return f'There isn\'t a fish of type {fish_type}.'

        fish = Controller.FISH[fish_type](fish_name, fish_species, price)
        aquarium = self._find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):

        aquarium = self._find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):

        aquarium = self._find_aquarium_by_name(aquarium_name)
        value = (sum(f.price for f in aquarium.fish) +
                 sum(d.price for d in aquarium.decorations))
        return f'The value of Aquarium {aquarium_name} is {value:.2f}.'

    def report(self):

        return '\n'.join(str(a) for a in self.aquariums)

    def _find_aquarium_by_name(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        return aquarium[0] if aquarium else None
