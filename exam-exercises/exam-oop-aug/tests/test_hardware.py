import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('test name', 'test type', 100, 200)

    def test_hardware_is_instantiated(self):
        self.assertEqual(self.hardware.name, 'test name')
        self.assertEqual(self.hardware.type, 'test type')
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 200)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_software_component(self):
        software = Software('test', 'type', 10, 20)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_not_enough_capacity_to_install_raises_error(self):
        software = Software('test', 'type', 101, 20)
        with self.assertRaises(Exception) as error:
            self.hardware.install(software)
        self.assertEqual(str(error.exception), 'Software cannot be installed')

    def test_uninstall_software(self):
        software = Software('test', 'type', 10, 20)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.software_components, [])


if __name__ == '__main__':
    unittest.main()
