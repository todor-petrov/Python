class Trainer:

    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id

    @staticmethod
    def get_next_id():
        if Trainer.id == 1:
            return Trainer.id
        Trainer.id += 1
        return Trainer.id

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
