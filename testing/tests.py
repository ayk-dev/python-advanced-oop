import unittest
from testing.worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('Albena', 1000, 100)

    def test_worker_is_initialized(self):
        self.assertEqual(self.worker.name, 'Albena')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)

    def test_worker_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_error_is_raised_if_worker_tries_to_work_with_negative_or_zero_energy(self):
        for energy in (0, -10):
            self.worker.energy = energy
            with self.assertRaises(Exception):
                self.worker.work()

    def test_worker_money_is_increased_after_work(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_energy_is_decreased_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_get_info_method_returns_the_proper_string_with_correct_values(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'Albena has saved 0 money.')


if __name__ == '__main__':
    unittest.main()

