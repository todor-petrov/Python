from space_station.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    INITIAL_OXYGEN = 70
    BREATHED_OXYGEN = 5

    def __init__(self, name: str):
        super().__init__(name, oxygen=Biologist.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= Biologist.BREATHED_OXYGEN
