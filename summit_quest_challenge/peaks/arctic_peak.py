from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    @staticmethod
    def get_recommended_gear():
        return ['Ice axe', 'Crampons', 'Insulated clothing', 'Helmet']

    def calculate_difficulty_level(self):
        if 3000 < self.elevation:
            self.difficulty_level = 'Extreme'
        if 2000 <= self.elevation <= 3000:
            self.difficulty_level = 'Advanced'
