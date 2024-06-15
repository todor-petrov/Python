from system_split.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):

        available_capacity = self.capacity - sum(s.capacity_consumption for s in self.software_components)
        available_memory = self.memory - sum(s.memory_consumption for s in self.software_components)

        if available_capacity < software.capacity_consumption or available_memory < software.memory_consumption:
            raise Exception('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):

        self.software_components.remove(software)
