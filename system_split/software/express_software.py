from system_split.software.software import Software


class ExpressSoftware(Software):

    MEMORY_COEFFICIENT = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int, software_type: str = 'Express'):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.memory_consumption = memory_consumption * ExpressSoftware.MEMORY_COEFFICIENT
