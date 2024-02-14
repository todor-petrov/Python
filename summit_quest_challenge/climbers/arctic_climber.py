from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    ARCTIC_CLIMBER_INITIAL_STRENGTH = 200
    MIN_ARCTIC_CLIMBER_STRENGTH = 100
    STRENGTH_CLIMB_REDUCING = 20
    EXTREME_LEVEL_COEFFICIENT = 2
    NON_EXTREME_LEVEL_COEFFICIENT = 1.5

    def __init__(self, name: str):
        super().__init__(name, strength=ArcticClimber.ARCTIC_CLIMBER_INITIAL_STRENGTH)

    def can_climb(self):
        return ArcticClimber.MIN_ARCTIC_CLIMBER_STRENGTH <= self.strength

    def climb(self, peak: BasePeak):
        self.conquered_peaks.append(peak.name)
        if peak.difficulty_level == 'Extreme':
            self.strength -= ArcticClimber.STRENGTH_CLIMB_REDUCING * ArcticClimber.EXTREME_LEVEL_COEFFICIENT
        else:
            self.strength -= ArcticClimber.STRENGTH_CLIMB_REDUCING * ArcticClimber.NON_EXTREME_LEVEL_COEFFICIENT
