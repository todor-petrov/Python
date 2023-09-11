from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    car_types = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.car_types:
            return
        if any(c for c in self.cars if c.model == model):
            raise Exception(f'Car {model} is already created!')
        self.cars.append(self.car_types[car_type](model, speed_limit))
        return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        if any(d for d in self.drivers if d.name == driver_name):
            raise Exception(f'Driver {driver_name} is already created!')
        self.drivers.append(Driver(driver_name))
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        if any(r for r in self.races if r.name == race_name):
            raise Exception(f'Race {race_name} is already created!')
        self.races.append(Race(race_name))
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)
        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')
        car_match = [c for c in self.cars if c.__class__.__name__ == car_type and c.is_taken is False]
        if not car_match:
            raise Exception(f'Car {car_type} could not be found!')
        car = car_match[-1]
        car.is_taken = True
        if driver.car is None:
            driver.car = car
            return f'Driver {driver_name} chose the car {car.model}.'
        old_model = driver.car
        driver.car.is_taken = False
        driver.car = car
        return f'Driver {driver_name} changed his car from {old_model.model} to {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        if race is None:
            raise Exception(f'Race {race_name} could not be found!')
        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)
        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')
        if driver.car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')
        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'
        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        if race is None:
            raise Exception(f'Race {race_name} could not be found!')
        if len(self.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')
        sorted_drivers = list(sorted(self.drivers, key=lambda x: -x.car.speed_limit))
        finalists = []
        for d in range(3):
            finalists.append(sorted_drivers[d])
        result = []
        for d in finalists:
            d.number_of_wins += 1
            result.append(f'Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.')
        return '\n'.join(result)
