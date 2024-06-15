from system_split.software.software import Software
from math import floor


class LightSoftware(Software):

    CAPACITY_COEFFICIENT = 1.5
    MEMORY_COEFFICIENT = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int, software_type: str = 'Light'):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.capacity_consumption = floor(capacity_consumption * LightSoftware.CAPACITY_COEFFICIENT)
        self.memory_consumption = floor(memory_consumption * LightSoftware.MEMORY_COEFFICIENT)
