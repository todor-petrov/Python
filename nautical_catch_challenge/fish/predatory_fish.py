from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):

    def fish_details(self):
        return (f'{self.__class__.__name__}: {self.name} '
                f'[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]')
