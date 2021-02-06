import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_advanced_player_instantiated_with_username_and_health(self):
        advanced = Advanced('test username')
        self.assertEqual(advanced.username, 'test username')
        self.assertEqual(advanced.health, 250)
        # self.assertEqual(advanced.card_repository.__class__.__name__, 'CardRepository')
        # self.assertFalse(advanced.is_dead)

    def test_is_dead(self):
        advanced = Advanced('test username')
        advanced.health = 0
        self.assertTrue(advanced.is_dead)

    def test_take_damage(self):
        advanced = Advanced('test username')
        advanced.take_damage(50)
        self.assertEqual(advanced.health, 200)

    def test_take_damage_negative_raises_error(self):
        adv = Advanced('test adv username')
        with self.assertRaises(ValueError) as error:
            adv.take_damage(-25)
        self.assertEqual(str(error.exception), 'Damage points cannot be less than zero.')


if __name__ == '__main__':
    unittest.main()

