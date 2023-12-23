from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        player.guild = self.name
        self.players.append(player)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
            player.guild = 'Unaffiliated'
            self.players.remove(player)
            return f'Player {player_name} has been removed from the guild.'
        except StopIteration:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        guild_data = [f'Guild: {self.name}']
        [guild_data.append(player.player_info()) for player in self.players]
        return '\n'.join(guild_data)
    

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

