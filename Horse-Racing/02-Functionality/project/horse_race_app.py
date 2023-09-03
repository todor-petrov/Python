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
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.horse_breeds:
            self.horses.append(self.horse_breeds[horse_type](horse_name, horse_speed))

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} has been already added!')
        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_match = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey_match:
            raise Exception(f'Jockey {jockey_name} could not be found!')
        jockey = jockey_match[0]
        horse_match = [h for h in self.horses if h.__class__.__name__ == horse_type]
        if not horse_match:
            raise Exception(f'Horse breed {horse_type} could not be found!')
        horse = horse_match[-1]
        if jockey.horse is not None:
            return f'Jockey {jockey_name} already has a horse.'
        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_match = [r for r in self.horse_races if r.race_type == race_type]
        if not race_match:
            raise Exception(f'Race {race_type} could not be found!')
        race = race_match[0]
        jockey_match = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey_match:
            raise Exception(f'Jockey {jockey_name} could not be found!')
        jockey = jockey_match[0]
        if jockey.horse is None:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')
        for j in race.jockeys:
            if j.name == jockey_name:
                return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):
        if race_type not in [r.race_type for r in self.horse_races]:
            raise Exception(f'Race {race_type} could not be found!')
        if len(self.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        winner, highest_speed = '', 0
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                winner = jockey
                horse = winner.horse
                highest_speed = horse.speed
        return f"The winner of the {race_type} race, " \
               f"with a speed of {highest_speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."

