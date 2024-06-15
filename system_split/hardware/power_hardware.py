from system_split.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):

    CAPACITY_COEFFICIENT = 0.25
    MEMORY_COEFFICIENT = 1.75

    def __init__(self, name: str, capacity: int, memory: int, hardware_type: str = 'Power'):
        super().__init__(name, hardware_type, capacity, memory)
        self.capacity = floor(capacity * PowerHardware.CAPACITY_COEFFICIENT)
        self.memory = floor(memory * PowerHardware.MEMORY_COEFFICIENT)
