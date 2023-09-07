from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        self.players.extend([p for p in players if p not in self.players])
        players_names = [p.name for p in self.players]
        return f"Successfully added: {', '.join(players_names)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend([s for s in supplies])

    def sustain(self, player_name: str, sustenance_type: str):
        ...

    def duel(self, first_player_name: str, second_player_name: str):
        ...

    def next_day(self):
        ...

    def __str__(self):
        players = '\n'.join(str(p) for p in self.players)
        supplies = '\n'.join(s.details() for s in self.supplies)
        return f'{players}\n{supplies}'

