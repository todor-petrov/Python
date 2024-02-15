from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber


class SummitQuestManagerApp:

    VALID_CLIMBERS_TYPES = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):

        if climber_type not in SummitQuestManagerApp.VALID_CLIMBERS_TYPES:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [x.name for x in self.climbers]:
            return f'{climber_name} has been already registered.'

        climber = SummitQuestManagerApp.VALID_CLIMBERS_TYPES[climber_type](climber_name)
        self.climbers.append(climber)
        return f'{climber_name} is successfully registered as a {climber_type}.'

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        ...

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        ...

    def perform_climbing(self, climber_name: str, peak_name: str):
        ...

    def get_statistics(self):
        ...
