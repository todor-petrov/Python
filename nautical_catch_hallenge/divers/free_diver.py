from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    OXYGEN = 120.0

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=FreeDiver.OXYGEN)

    def miss(self, time_to_catch: int):
        self.oxygen_level -= round(0.60 * time_to_catch)
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.OXYGEN
