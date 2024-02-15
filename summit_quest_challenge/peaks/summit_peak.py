from peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    def get_recommended_gear(self):
        return ['Climbing helmet', 'Harness', 'Climbing shoes', 'Ropes']

    def calculate_difficulty_level(self):
        if 2500 < self.elevation:
            return 'Extreme'
        if 1500 <= self.elevation <= 2500:
            return 'Advanced'
