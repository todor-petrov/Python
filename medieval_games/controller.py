class Controller:

    SUPPLIES = ['Food', 'Drink']

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):

        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):

        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):

        player = self._find_player_by_player_name(player_name)
        supplies = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]

        if sustenance_type not in Controller.SUPPLIES or player not in self.players:
            return

        if not player.need_sustenance:
            return f'{player.name} have enough stamina.'

        if not supplies:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

        supply = supplies.pop()
        player.stamina = min(player.stamina + supply.energy, player.MAX_STAMINA)

        del self.supplies[len(self.supplies) - self.supplies[::-1].index(supply) - 1]

        return f'{player.name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self._find_player_by_player_name(first_player_name)
        second_player = self._find_player_by_player_name(second_player_name)

        zero_stamina, players = [], [first_player, second_player]

        for player in players:
            if player.stamina == 0:
                zero_stamina.append(f'Player {player.name} does not have enough stamina.')
        if zero_stamina:
            return '\n'.join(zero_stamina)

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina = max(second_player.stamina - first_player.stamina / 2,
                                    second_player.MIN_STAMINA)
        if second_player.stamina == 0:
            return f'Winner: {first_player.name}'

        first_player.stamina = max(first_player.stamina - second_player.stamina / 2,
                                   first_player.MIN_STAMINA)

        if first_player.stamina == 0:
            return f'Winner: {second_player.name}'

        winner = first_player if second_player.stamina < first_player.stamina else second_player
        return f'Winner: {winner.name}'

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, player.MIN_STAMINA)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        controller_data = [str(p) for p in self.players]
        controller_data.extend(s.details() for s in self.supplies)
        return '\n'.join(controller_data)

    def _find_player_by_player_name(self, player_name):
        player = [p for p in self.players if p.name == player_name]
        return player[0] if player else None
