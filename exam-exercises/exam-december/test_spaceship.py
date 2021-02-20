from project.spaceship.spaceship import Spaceship
import unittest


class TestSpaceship(unittest.TestCase):
    def setUp(self) -> None:
        self.spaceship = Spaceship('test', 1)

    def test_spaceship_is_instantiated(self):
        self.assertEqual(self.spaceship.name, 'test')
        self.assertEqual(self.spaceship.capacity, 1)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_astronaut_is_added(self):
        result = self.spaceship.add('Name')
        self.assertEqual(len(self.spaceship.astronauts), 1)
        self.assertEqual(result, 'Added astronaut Name')

    def test_no_space_to_add_raises_error(self):
        self.spaceship.add('Name')
        self.assertEqual(len(self.spaceship.astronauts), self.spaceship.capacity)
        with self.assertRaises(ValueError) as error:
            self.spaceship.add('Name2')
        self.assertEqual(str(error.exception), 'Spaceship is full')

    def test_astronaut_already_in_spaceship_raises_error(self):
        self.spaceship.capacity = 2
        self.spaceship.add('Name')
        self.assertEqual(len(self.spaceship.astronauts), 1)
        with self.assertRaises(ValueError) as error:
            self.spaceship.add('Name')
        self.assertEqual(str(error.exception), 'Astronaut Name Exists')

    def test_remove_astronaut_raises_error_if_not_found(self):
        with self.assertRaises(ValueError) as error:
            self.spaceship.remove('Name')
        self.assertEqual(str(error.exception), 'Astronaut Not Found')

    def test_astronaut_is_removed(self):
        self.spaceship.add('Name')
        self.assertEqual(len(self.spaceship.astronauts), 1)

        result = self.spaceship.remove('Name')
        self.assertEqual(len(self.spaceship.astronauts), 0)
        self.assertEqual(result, 'Removed Name')
        

if __name__ == '__main__':
    unittest.main()
