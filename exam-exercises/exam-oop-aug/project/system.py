from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                hardware.install(express_software)
                System._software.append(express_software)
            except Exception as error:
                return str(error)

        except IndexError:
            return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                hardware.install(light_software)
                System._software.append(light_software)
            except Exception as error:
                return str(error)

        except IndexError:
            return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name: str, software_name:str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        count_hardware_components = len(System._hardware)
        count_software_components = len(System._software)

        total_memory = int(sum([h.memory for h in System._hardware]))
        total_used_memory = int(sum([s.memory_consumption for s in System._software]))

        total_capacity = int(sum([h.capacity for h in System._hardware]))
        total_used_space = int(sum([s.capacity_consumption for s in System._software]))

        result = "System Analysis" + '\n' + f"Hardware Components: {count_hardware_components}" + '\n' + f"Software Components: {count_software_components}" + '\n' + f"Total Operational Memory: {total_used_memory} / {total_memory}" + '\n' + f"Total Capacity Taken: {total_used_space} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ''

        for h in System._hardware:
            result += f'Hardware Component - {h.name}\n'

            n_installed_express_sc = len([s for s in h.software_components if s.__class__.__name__ == 'ExpressSoftware'])
            result += f'Express Software Components: {n_installed_express_sc}\n'

            n_installed_light_sc = len([s for s in h.software_components if s.__class__.__name__ == 'LightSoftware'])
            result += f'Light Software Components: {n_installed_light_sc}\n'

            total_memory_used = sum([s.memory_consumption for s in h.software_components])
            result += f'Memory Usage: {total_memory_used} / {h.memory}\n'

            total_capacity_used = sum([s.capacity_consumption for s in h.software_components])
            result += f'Capacity Usage: {total_capacity_used} / {h.capacity}\n'

            result += f'Type: {h.type}\n'

            if h.software_components:
                names_of_software_components = ', '.join([s.name for s in h.software_components])
            else:
                names_of_software_components = 'None'
            result += f'Software Components: {names_of_software_components}'

        return result

