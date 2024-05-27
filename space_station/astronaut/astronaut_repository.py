from space_station.astronaut.astronaut import Astronaut
from space_station.astronaut.biologist import Biologist
from space_station.astronaut.geodesist import Geodesist
from space_station.astronaut.meteorologist import Meteorologist


class AstronautRepository:

    ASTRONAUTS = {'Biologist': Biologist, 'Geodesist': Geodesist, 'Meteorologist': Meteorologist}

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = [a for a in self.astronauts if a.name == name]
        return astronaut[0] if astronaut else None
