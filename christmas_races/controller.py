from christmas_races.car.muscle_car import MuscleCar
from christmas_races.car.sports_car import SportsCar
from christmas_races.driver import Driver
from christmas_races.race import Race


class Controller:

    CARS = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}
    MIN_PARTICIPANTS = 3

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if car_type not in Controller.CARS:
            return

        if model in [c.model for c in self.cars]:
            raise Exception(f'Car {model} is already created!')

        self.cars.append(Controller.CARS[car_type](model, speed_limit))
        return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):

        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f'Driver {driver_name} is already created!')

        self.drivers.append(Driver(driver_name))
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):

        if race_name in [r.name for r in self.races]:
            raise Exception(f'Race {race_name} is already created!')

        self.races.append(Race(race_name))
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):

        driver = self._find_driver_by_driver_name(driver_name)
        cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        car = cars[-1] if cars else None

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not car:
            raise Exception(f'Car {car_type} could not be found!')

        if car and driver.car:
            old_model = driver.car
            old_model.is_taken, car.is_taken = False, True
            driver.car = car
            return f'Driver {driver.name} changed his car from {old_model.model} to {car.model}.'

        if car and not driver.car:
            driver.car, car.is_taken = car, True
            return f'Driver {driver.name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):

        race = self._find_race_by_race_name(race_name)
        driver = self._find_driver_by_driver_name(driver_name)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not driver.car:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):

        race = self._find_race_by_race_name(race_name)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < Controller.MIN_PARTICIPANTS:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted(race.drivers, key=lambda d: -d.car.speed_limit)[:3]
        winners_info = []

        for winner in winners:
            winner.number_of_wins += 1
            winners_info.append(f'Driver {winner.name} wins the {race_name} '
                                f'race with a speed of {winner.car.speed_limit}.')

        return '\n'.join(winners_info)

    def _find_driver_by_driver_name(self, driver_name):
        driver = [d for d in self.drivers if d.name == driver_name]
        return driver[0] if driver else None

    def _find_car_by_car_type(self, car_type):
        car = [c for c in self.cars if c.__class__.__name__ == car_type]
        return car[0] if car else None

    def _find_race_by_race_name(self, race_name):
        race = [r for r in self.races if r.name == race_name]
        return race[0] if race else None
