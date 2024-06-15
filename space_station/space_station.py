from space_station.astronaut.astronaut_repository import AstronautRepository
from space_station.planet.planet import Planet
from space_station.planet.planet_repository import PlanetRepository


class SpaceStation:

    OXYGEN_INCREASING = 10
    OXYGEN_FOR_MISSION = 30
    ASTRONAUTS_FOR_MISSION = 5

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        if astronaut_type not in self.astronaut_repository.ASTRONAUTS:
            raise Exception('Astronaut type is not valid!')

        self.astronaut_repository.add(self.astronaut_repository.ASTRONAUTS[astronaut_type](name))
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):

        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):

        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):

        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(SpaceStation.OXYGEN_INCREASING)

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception('Invalid planet name!')

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts
                               if SpaceStation.OXYGEN_FOR_MISSION < a.oxygen]

        if not suitable_astronauts:
            raise Exception('You need at least one astronaut to explore the planet!')

        sorted_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)

        if len(sorted_astronauts) <= SpaceStation.ASTRONAUTS_FOR_MISSION:
            astronauts_on_mission = sorted_astronauts
        else:
            astronauts_on_mission = sorted_astronauts[:SpaceStation.ASTRONAUTS_FOR_MISSION]

        participated_astronauts = 0

        for astronaut in astronauts_on_mission:

            if len(planet.items) == 0:
                break

            participated_astronauts += 1

            while planet.items and 0 < astronaut.oxygen:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if not planet.items:
            self.successful_missions += 1
            return (f'Planet: {planet_name} was explored. '
                    f'{participated_astronauts} space_station participated in collecting items.')

        else:
            self.not_completed_missions += 1
            return f'Mission is not completed.'

    def report(self):

        report_info = [f'{self.successful_missions} successful missions!',
                       f'{self.not_completed_missions} missions were not completed!',
                       'Astronauts\' info:']
        for astronaut in self.astronaut_repository.astronauts:
            report_info.append(astronaut.details())

        return '\n'.join(report_info)
