from typing import List


class SummitQuestManagerApp:

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        ...

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        ...

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        ...

    def perform_climbing(self, climber_name: str, peak_name: str):
        ...

    def get_statistics(self):
        ...
