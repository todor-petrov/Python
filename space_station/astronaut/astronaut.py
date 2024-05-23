class Astronaut:

    BREATHED_OXYGEN = 10

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Astronaut name cannot be empty string or whitespace!')
        self.__name = value

    def breathe(self):
        self.oxygen -= Astronaut.BREATHED_OXYGEN

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def details(self):

        return (f"Name: {self.name}\n"
                f"Oxygen: {self.oxygen}\n"
                f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}")
