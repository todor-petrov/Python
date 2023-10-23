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
        equipment = [e for e in self.equipment if e.TYPE_ == equipment_type][-1]
        team = [t for t in self.teams if t.name == team_name][0]
        if team.budget < equipment.price:
            return 'Budget is not enough!'
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str):
        ...

    def increase_equipment_price(self, equipment_type: str):
        ...

    def play(self, team_name1: str, team_name2: str):
        ...

    def get_statistics(self):
        ...

