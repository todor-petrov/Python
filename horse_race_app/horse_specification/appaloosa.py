from movie_app.horse_specification.horse import Horse


class Appaloosa(Horse):

    MAX_SPEED = 120
    SPEED_INCREASING_STEP = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + Appaloosa.SPEED_INCREASING_STEP, Appaloosa.MAX_SPEED)
