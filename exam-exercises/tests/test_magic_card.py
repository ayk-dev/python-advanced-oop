import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_magic_card_is_instantiated_with_name_damage_and_health_points(self):
        magic_card = MagicCard('test magic card')
        self.assertEqual(magic_card.name, 'test magic card')
        self.assertEqual(magic_card.damage_points, 5)
        self.assertEqual(magic_card.health_points, 80)

    def test_empty_string_as_name_raises_error(self):
        with self.assertRaises(ValueError) as error:
            magic_card = MagicCard('')
        self.assertEqual(str(error.exception), "Card's name cannot be an empty string.")

    def test_negative_health_points_raises_error(self):
        magic_card = MagicCard('test')
        with self.assertRaises(ValueError) as error:
            magic_card.health_points = -1
        self.assertEqual(str(error.exception), "Card's HP cannot be less than zero.")

    def test_negative_damage_points_raises_error(self):
        magic_card = MagicCard('test')
        with self.assertRaises(ValueError) as error:
            magic_card.damage_points = -1
        self.assertEqual(str(error.exception), "Card's damage points cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()

