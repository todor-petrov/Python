from christmas_races.car.car import Car


class MuscleCar(Car):

    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not MuscleCar.MIN_SPEED_LIMIT <= value <= MuscleCar.MAX_SPEED_LIMIT:
            raise ValueError(f'Invalid speed limit! Must be between '
                             f'{MuscleCar.MIN_SPEED_LIMIT} and {MuscleCar.MAX_SPEED_LIMIT}!')
        self.__speed_limit = value
