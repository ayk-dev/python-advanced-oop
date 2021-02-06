import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_beginner_player_instantiated_with_username_and_health(self):
        beginner = Beginner('test beg username')
        self.assertEqual(beginner.username, 'test beg username')
        self.assertEqual(beginner.health, 50)

    def test_take_damage(self):
        beginner = Beginner('test beg username')
        beginner.take_damage(25)
        self.assertEqual(beginner.health, 25)

    def test_take_damage_negative_raises_error(self):
        beginner = Beginner('test beg username')
        with self.assertRaises(ValueError) as error:
            beginner.take_damage(-25)
        self.assertEqual(str(error.exception), 'Damage points cannot be less than zero.')

    def test_is_dead(self):
        beginner = Beginner('test beg username')
        beginner.health = 0
        self.assertTrue(beginner.is_dead)

    # TODO do I need to test any more methods here?

if __name__ == '__main__':
    unittest.main()

