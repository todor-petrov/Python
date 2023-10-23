from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad


class Tournament:
    EQUIPMENT_TYPES = {'ElbowPad': ElbowPad, 'KneePad': KneePad}

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
        ...

    def sell_equipment(self, equipment_type: str, team_name: str):
        ...

    def remove_team(self, team_name: str):
        ...

    def increase_equipment_price(self, equipment_type: str):
        ...

    def play(self, team_name1: str, team_name2: str):
        ...

    def get_statistics(self):
        ...

