from player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str):
        player = [a for a in self.__players if a.name == player_name]
        if not player:
            return f'Player {player_name} not found'
        self.__players.remove(player[0])
        return player[0]
