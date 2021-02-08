import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_trap_card_is_instantiated_with_name_damage_and_health_points(self):
        trap_card = TrapCard('test magic card')
        self.assertEqual(trap_card.name, 'test magic card')
        self.assertEqual(trap_card.damage_points, 120)
        self.assertEqual(trap_card.health_points, 5)

    def test_empty_string_as_name_raises_error(self):
        with self.assertRaises(ValueError) as error:
            trap_card = TrapCard('')
        self.assertEqual(str(error.exception), "Card's name cannot be an empty string.")

    def test_negative_health_points_raises_error(self):
        trap_card = TrapCard('test')
        with self.assertRaises(ValueError) as error:
            trap_card.health_points = -1
        self.assertEqual(str(error.exception), "Card's HP cannot be less than zero.")

    def test_negative_damage_points_raises_error(self):
        trap_card = TrapCard('test')
        with self.assertRaises(ValueError) as error:
            trap_card.damage_points = -1
        self.assertEqual(str(error.exception), "Card's damage points cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()