from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 10000.0
    INCREMENT_ADVANTAGE = 115
    TYPE_ = 'OutdoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.wins += 1
        self.advantage += OutdoorTeam.INCREMENT_ADVANTAGE