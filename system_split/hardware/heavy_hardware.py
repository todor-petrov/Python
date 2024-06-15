from system_split.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):

    CAPACITY_COEFFICIENT = 2
    MEMORY_COEFFICIENT = 0.75

    def __init__(self, name: str, capacity: int, memory: int, hardware_type: str = 'Heavy'):
        super().__init__(name, hardware_type, capacity, memory)
        self.capacity = capacity * HeavyHardware.CAPACITY_COEFFICIENT
        self.memory = floor(memory * HeavyHardware.MEMORY_COEFFICIENT)
