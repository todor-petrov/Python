from space_station.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    INITIAL_OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, oxygen=Geodesist.INITIAL_OXYGEN)
