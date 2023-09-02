from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    horse_breeds = {'Appaloosa': Appaloosa,  'Thoroughbred': Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.horse_breeds:
            return
        if self.__horse_already_added(horse_name):
            raise Exception(f'Horse {horse_name} has been already added!')
        horse = self.horse_breeds[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f'"{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        if self.__jockey_already_added(jockey_name):
            raise Exception(f'Jockey {jockey_name} has been already added!')
        jockey = Jockey(jockey_name, age)
        self.horses.append(jockey)
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if any(r for r in self.horse_races if r.race_type == race_type):
            raise Exception(f'Race {race_type} has been already created!')
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        ...

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        ...

    def start_horse_race(self, race_type: str):
        ...

    def __horse_already_added(self, name):
        horse = next(filter(lambda h: h.name == name, self.horses), None)
        return True if horse else False

    def __jockey_already_added(self, name):
        jockey = next(filter(lambda j: j.name == name, self.jockeys), None)
        return True if jockey else False
