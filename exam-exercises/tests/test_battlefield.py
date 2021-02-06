import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.test_battle_field = BattleField()

    def test_fight_if_attacker_is_dead_raises_error(self):
        test_attacker = Beginner('test attacker')
        test_enemy = Beginner('test enemy')
        test_attacker.health = 0
        with self.assertRaises(ValueError) as error:
            self.test_battle_field.fight(test_attacker, test_enemy)
        self.assertEqual(str(error.exception), 'Player is dead!')

    def test_fight_if_enemy_is_dead_raises_error(self):
        test_attacker = Beginner('test attacker')
        test_enemy = Beginner('test enemy')
        test_enemy.health = 0
        with self.assertRaises(ValueError) as error:
            self.test_battle_field.fight(test_attacker, test_enemy)
        self.assertEqual(str(error.exception), 'Player is dead!')

    def test_bonus_points_for_beginners(self):
        test_attacker = Beginner('test attacker')
        test_enemy = Advanced('test enemy')
        self.test_battle_field.fight(test_attacker, test_enemy)
        self.assertEqual(test_attacker.health, 90)
        self.assertEqual(test_enemy.health, 250)

    def test_health_changes_in_fight(self):
        test_attacker = Advanced('test enemy')
        test_enemy = Beginner('test attacker')
        mc = MagicCard('testmagic')
        test_attacker.card_repository.add(mc)
        tc = TrapCard('testtrap')
        test_enemy.card_repository.add(tc)
        self.test_battle_field.fight(test_attacker, test_enemy)
        self.assertEqual(test_attacker.health, 180)
        self.assertEqual(test_enemy.health, 90)



if __name__ == '__main__':
    unittest.main()
