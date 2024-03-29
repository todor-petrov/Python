from typing import List

from climbers.arctic_climber import ArcticClimber
from climbers.summit_climber import SummitClimber
from peaks.arctic_peak import ArcticPeak
from peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    CLIMBERS = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}
    PEAKS = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):

        if climber_type not in SummitQuestManagerApp.CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [x.name for x in self.climbers]:
            return f'{climber_name} has been already registered.'

        climber = SummitQuestManagerApp.CLIMBERS[climber_type](climber_name)
        self.climbers.append(climber)
        return f'{climber_name} is successfully registered as a {climber_type}.'

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in SummitQuestManagerApp.PEAKS:
            return f'{peak_type} is an unknown type of peak.'
        peak = SummitQuestManagerApp.PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f'{peak_name} is successfully added to the wish list as a {peak_type}.'

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        climber = [c for c in self.climbers if c.name == climber_name][0]
        peak = [p for p in self.peaks if p.name == peak_name][0]
        peak_gear = set(peak.get_recommended_gear())
        missing_gear = peak_gear - set(gear)

        if not missing_gear:
            return f'{climber_name} is prepared to climb {peak_name}.'
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):

        if climber_name not in [c.name for c in self.climbers]:
            return f'Climber {climber_name} is not registered yet.'

        if peak_name not in [p.name for p in self.peaks]:
            return f'Peak {peak_name} is not part of the wish list.'

        climber = [c for c in self.climbers if c.name == climber_name][0]
        peak = [p for p in self.peaks if p.name == peak_name][0]

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f'{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}.'

        if not climber.is_prepared:
            return f'{climber_name} will need to be better prepared next time.'

        if not climber.can_climb():
            climber.rest()
            return f'{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest.'

    def get_statistics(self):
        climbers = sorted([c for c in self.climbers if c.conquered_peaks],
                          key=lambda c: (-len(c.conquered_peaks), c.name))
        data = [f"Total climbed peaks: {len(self.peaks)}", "**Climber's statistics:**"]
        data.extend([str(c) for c in climbers])
        return '\n'.join(data)
