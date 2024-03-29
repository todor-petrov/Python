from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {'ElbowPad': ElbowPad, 'KneePad': KneePad}
    TEAM_TYPES = {'IndoorTeam': IndoorTeam, 'OutdoorTeam': OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')
        self._name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in Tournament.EQUIPMENT_TYPES:
            raise Exception('Invalid equipment type!')
        equipment = Tournament.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)
        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in Tournament.TEAM_TYPES:
            raise Exception('Invalid team type!')
        if len(self.teams) >= self.capacity:
            return 'Not enough tournament capacity.'
        team = Tournament.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f'{team_type} was successfully added.'

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipments = [e for e in self.equipment if e.TYPE_ == equipment_type]
        equipment = equipments[-1] if equipments else None
        teams = [team for team in self.teams if team.name == team_name]
        team = teams[0] if teams else None
        if team.budget < equipment.price:
            raise Exception('Budget is not enough!')
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str):
        team_search = [team for team in self.teams if team.name == team_name]
        if not team_search:
            raise Exception('No such team!')
        team = team_search[0]
        if team.wins != 0:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')
        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str):
        increased_equipments = len([e.increase_price() for e in self.equipment if e.TYPE_ == equipment_type])
        return f'Successfully changed {increased_equipments}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team_1 = [team for team in self.teams if team.name == team_name1][0]
        team_2 = [team for team in self.teams if team.name == team_name2][0]
        if not team_1.TYPE_ == team_2.TYPE_:
            raise Exception('Game cannot start! Team types mismatch!')
        team_1_points = team_1.advantage + sum([e.protection for e in team_1.equipment])
        team_2_points = team_2.advantage + sum([e.protection for e in team_2.equipment])
        if team_1_points == team_2_points:
            return 'No winner in this game.'
        winner = team_1 if team_1_points > team_2_points else team_2
        winner.win()
        return f'The winner is {winner.name}.'

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        result = [f'Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:']
        result.extend([team.get_statistics() for team in sorted_teams])
        return '\n'.join(result)


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
