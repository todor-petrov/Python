from climbers.base_climber import BaseClimber
from peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    INITIAL_STRENGTH = 150
    MIN_STRENGTH = 75
    STRENGTH_REDUCING = 30
    ADVANCED = 1.3
    NON_ADVANCED = 2.5

    def __init__(self, name: str):
        super().__init__(name, strength=SummitClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return SummitClimber.MIN_STRENGTH <= self.strength

    def climb(self, peak: BasePeak):

        self.conquered_peaks.append(peak.name)
        if peak.difficulty_level == 'Advanced':
            self.strength -= SummitClimber.STRENGTH_REDUCING * SummitClimber.ADVANCED
        else:
            self.strength -= SummitClimber.STRENGTH_REDUCING * SummitClimber.NON_ADVANCED
