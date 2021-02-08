import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.card_rep = CardRepository()
        self.test_card1 = MagicCard('test card one')

    def test_card_rep_is_instantiated_with_zero_count(self):
        self.assertEqual(self.card_rep.count, 0)
        self.assertEqual(len(self.card_rep.cards), 0)

    def test_adding_existing_card_raises_error(self):
        self.card_rep.add(self.test_card1)
        with self.assertRaises(ValueError) as error:
            self.card_rep.add(self.test_card1)
        self.assertEqual(str(error.exception), 'Card test card one already exists!')

    def test_card_is_added(self):
        self.assertEqual(self.card_rep.count, 0)
        self.card_rep.add(self.test_card1)
        self.assertEqual(self.card_rep.count, 1)
        self.assertEqual(self.card_rep.cards, [self.test_card1])

    def test_card_is_removed(self):
        self.card_rep.add(self.test_card1)

        self.card_rep.remove('test card one')
        self.assertEqual(self.card_rep.count, 0)
        self.assertEqual(self.card_rep.cards, [])

    def test_remove_empty_string_raises_error(self):
        self.card_rep.add(self.test_card1)
        with self.assertRaises(ValueError) as error:
            self.card_rep.remove('')

        self.assertEqual(str(error.exception), 'Card cannot be an empty string!')
        # TODO should I test the message itself?

    def test_find_returns_correct_card(self):
        self.test_card2 = MagicCard('Test 2')
        self.card_rep.add(self.test_card1)
        self.card_rep.add(self.test_card2)

        searched_card = self.card_rep.find('Test 2')
        self.assertEqual(self.test_card2, searched_card)
        self.assertNotEqual(self.test_card1, searched_card)


if __name__ == '__main__':
    unittest.main()

