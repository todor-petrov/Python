from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver


class NauticalCatchChallengeApp:

    DIVERS = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in NauticalCatchChallengeApp.DIVERS:
            return f'{diver_type} is not allowed in our competition.'
        if diver_name in [d.name for d in self.divers]:
            return f'{diver_name} is already a participant.'
        diver = NauticalCatchChallengeApp.DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f'{diver_name} is successfully registered for the competition as a {diver_type}.'

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        ...

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        ...

    def health_recovery(self):
        ...

    def diver_catch_report(self, diver_name: str):
        ...

    def competition_statistics(self):
        ...
