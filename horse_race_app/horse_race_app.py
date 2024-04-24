from movie_app.horse_race import HorseRace
from movie_app.horse_specification.appaloosa import Appaloosa
from movie_app.horse_specification.thoroughbred import Thoroughbred
from movie_app.jockey import Jockey


class HorseRaceApp:

    HORSE_TYPES = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in HorseRaceApp.HORSE_TYPES:
            self.horses.append(HorseRaceApp.HORSE_TYPES[horse_type](horse_name, horse_speed))
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):

        if self._find_jockey_by_name(jockey_name):
            raise Exception(f'Jockey {jockey_name} has been already added!')

        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):

        if self._find_horse_race_by_race_type(race_type):
            raise Exception(f'Race {race_type} has been already created!')

        self.horse_races.append(HorseRace(race_type))
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        jockey = self._find_jockey_by_name(jockey_name)
        available_horses = [h for h in self.horses if h.__class__.__name__ == horse_type]

        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not available_horses:
            raise Exception(f'Horse breed {horse_type} could not be found!')

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        horse = available_horses[-1]
        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey.name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        horse_race = self._find_horse_race_by_race_type(race_type)
        jockey = self._find_jockey_by_name(jockey_name)

        if not horse_race:
            raise Exception(f'Race {race_type} could not be found!')

        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in horse_race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        horse_race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):

        race = self._find_horse_race_by_race_type(race_type)
        if not race:
            raise Exception(f'Race {race_type} could not be found!')

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner, max_speed = None, 0
        for jockey in race.jockeys:
            if max_speed < jockey.horse.speed:
                max_speed = jockey.horse.speed
                winner = jockey

        return (f"The winner of the {race.race_type} race, "
                f"with a speed of {winner.horse.speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")

    def _find_jockey_by_name(self, jockey_name):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        return jockey[0] if jockey else None

    def _find_horse_race_by_race_type(self, race_type):
        horse_race = [r for r in self.horse_races if r.race_type == race_type]
        return horse_race[0] if horse_race else None


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))
