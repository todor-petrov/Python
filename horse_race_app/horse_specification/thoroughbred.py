from movie_app.horse_specification.horse import Horse


class Thoroughbred(Horse):

    MAX_SPEED = 140
    SPEED_INCREASING_STEP = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + Thoroughbred.SPEED_INCREASING_STEP, Thoroughbred.MAX_SPEED)
