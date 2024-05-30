from space_station.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    INITIAL_OXYGEN = 90
    BREATHED_OXYGEN = 15

    def __init__(self, name: str):
        super().__init__(name, Meteorologist.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= Meteorologist.BREATHED_OXYGEN
