import unittest

from project.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.test_controller = Controller()

    def test_controller_has_repositories(self):
        self.assertEqual(self.test_controller.card_repository.__class__.__name__, 'CardRepository')
        self.assertEqual(self.test_controller.player_repository.__class__.__name__, 'PlayerRepository')

    def test_adding_player_to_repository(self):
        self.assertEqual(self.test_controller.card_repository.count, 0)
        self.assertEqual(self.test_controller.player_repository.count, 0)
        result = self.test_controller.add_player('Beginner', 'test')
        self.assertEqual(self.test_controller.card_repository.count, 0)
        self.assertEqual(self.test_controller.player_repository.count, 1)
        self.assertEqual(result, 'Successfully added player of type Beginner with username: test')

    def test_adding_card_to_repository(self):
        self.assertEqual(self.test_controller.card_repository.count, 0)
        self.assertEqual(self.test_controller.player_repository.count, 0)
        result = self.test_controller.add_card('Magic', 'test')
        self.assertEqual(self.test_controller.card_repository.count, 1)
        self.assertEqual(self.test_controller.player_repository.count, 0)
        self.assertEqual(result, 'Successfully added card of type MagicCard with name: test')

    def test_adding_card_to_player(self):
        self.assertEqual(self.test_controller.card_repository.count, 0)
        self.assertEqual(self.test_controller.player_repository.count, 0)
        self.test_controller.add_player('Beginner', 'test_player')
        self.test_controller.add_card('Magic', 'test_card')
        result = self.test_controller.add_player_card('test_player', 'test_card')
        self.assertEqual(self.test_controller.card_repository.count, 1)
        self.assertEqual(self.test_controller.player_repository.count, 1)
        self.assertEqual(result, 'Successfully added card: test_card to user: test_player')

    def test_players_fight(self):
        self.test_controller.add_player('Beginner', 'player1')
        self.test_controller.add_player('Advanced', 'player2')
        result = self.test_controller.fight('player2', 'player1')
        self.assertEqual(result, 'Attack user health 250 - Enemy user health 90')

    def test_report(self):
        self.test_controller.add_player('Beginner', 'player1')
        self.test_controller.add_player('Advanced', 'player2')
        self.test_controller.add_card('Magic', 'test_card')
        self.test_controller.add_player_card('player1', 'test_card')
        result = self.test_controller.report()
        self.assertEqual(result, "Username: player1 - Health: 50 - Cards 1\n" +
                         "### Card: test_card - Damage: 5\n" +
                         "Username: player2 - Health: 250 - Cards 0\n")


if __name__ == '__main__':
    unittest.main()

