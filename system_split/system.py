from system_split.hardware.heavy_hardware import HeavyHardware
from system_split.hardware.power_hardware import PowerHardware
from system_split.software.express_software import ExpressSoftware
from system_split.software.light_software import LightSoftware


class System:

    def __init__(self):
        self._hardware = []
        self._software = []

    def register_power_hardware(self, name: str, capacity: int, memory: int):

        self._hardware.append(PowerHardware(name, capacity, memory))

    def register_heavy_hardware(self, name: str, capacity: int, memory: int):

        self._hardware.append(HeavyHardware(name, capacity, memory))

    def register_express_software(self, hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):

        hardware = self._find_hardware_by_hardware_name(hardware_name)

        if not hardware:
            return 'Hardware does not exist'

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        self._software.append(software)

    def register_light_software(self, hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):

        hardware = self._find_hardware_by_hardware_name(hardware_name)

        if not hardware:
            return 'Hardware does not exist'

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        self._software.append(software)

    def release_software_component(self, hardware_name: str, software_name: str):

        hardware = self._find_hardware_by_hardware_name(hardware_name)
        software = self._find_software_by_software_name(software_name)

        if not hardware or not software:
            return 'Some of the components do not exist'

        hardware.uninstall(software)
        self._software.remove(software)

    def analyze(self):

        software_memory_consumption = sum(s.memory_consumption for s in self._software)
        hardware_memory = sum(h.memory for h in self._hardware)
        software_capacity_consumption = sum(s.capacity_consumption for s in self._software)
        hardware_capacity = sum(h.capacity for h in self._hardware)

        system = ['System Analysis',
                  f'Hardware Components: {len(self._hardware)}',
                  f'Software Components: {len(self._software)}',
                  f'Total Operational Memory: {software_memory_consumption} / {hardware_memory}',
                  f'Total Capacity Taken: {software_capacity_consumption} / {hardware_capacity}']

        return '\n'.join(system)

    def system_split(self):

        data = []

        for component in self._hardware:
            express_software = [es for es in component.software_components if
                                es.__class__.__name__ == 'ExpressSoftware']
            light_software = [ls for ls in component.software_components if ls.__class__.__name__ == 'LightSoftware']
            software_memory = sum(sm.memory_consumption for sm in component.software_components)
            software_capacity = sum(sc.capacity_consumption for sc in component.software_components)
            software_components = ', '.join(s.name for s in component.software_components) \
                if component.software_components else 'None'

            data.extend([f'Hardware Component - {component.name}',
                         f'Express Software Components: {len(express_software)}',
                         f'Light Software Components: {len(light_software)}',
                         f'Memory Usage: {software_memory} / {component.memory}',
                         f'Capacity Usage: {software_capacity} / {component.capacity}',
                         f'Type: {component.hardware_type}',
                         f'Software Components: {software_components}'])

        return '\n'.join(data)

    def _find_hardware_by_hardware_name(self, hardware_name):
        hardware = [h for h in self._hardware if h.name == hardware_name]
        return hardware[0] if hardware else None

    def _find_software_by_software_name(self, software_name):
        software = [s for s in self._software if s.name == software_name]
        return software[0] if software else None
