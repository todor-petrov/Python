from peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def get_recommended_gear(self):
        return ['Ice axe', 'Crampons', 'Insulated clothing', 'Helmet']

    def calculate_difficulty_level(self):
        if 3000 < self.elevation:
            return 'Extreme'
        if 2000 <= self.elevation <= 3000:
            return 'Advanced'
