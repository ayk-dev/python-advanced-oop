from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Heavy', int(capacity * 2), int(0.75 * memory))
