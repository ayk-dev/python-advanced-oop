import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.pl_rep = PlayerRepository()
        self.player1 = Beginner('Test 1')

    def test_player_repository_is_instantiated(self):
        self.assertEqual(self.pl_rep.count, 0)
        self.assertEqual(len(self.pl_rep.players), 0)

    def test_adding_existing_player_raises_error(self):
        self.pl_rep.add(self.player1)

        with self.assertRaises(ValueError) as error:
            self.pl_rep.add(self.player1)
        self.assertEqual(str(error.exception), 'Player Test 1 already exists!')

    def test_player_is_added(self):
        self.pl_rep.add(self.player1)
        self.assertEqual(self.pl_rep.count, 1)
        self.assertEqual(len(self.pl_rep.players), 1)

    def test_remove_empty_string_name_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.pl_rep.remove('')
        self.assertEqual(str(error.exception), 'Player cannot be an empty string!')

    def test_player_is_removed(self):
        self.pl_rep.add(self.player1)
        self.assertEqual(self.pl_rep.count, 1)

        self.pl_rep.remove('Test 1')
        self.assertEqual(self.pl_rep.count, 0)

    def test_find_returns_player_correctly(self):
        self.player2 = Beginner('Test 2')

        self.pl_rep.add(self.player1)
        self.pl_rep.add(self.player2)

        searched_player = self.pl_rep.find('Test 1')
        self.assertEqual('Test 1', searched_player.username)
        self.assertNotEqual('Test 2', searched_player.username)


if __name__ == '__main__':
    unittest.main()
