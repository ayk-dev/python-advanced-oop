from .groups import Group, Person

import unittest


class GroupsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Person('Ali', 'Baba')
        self.p2 = Person('Johnny', 'Smith')


class TestPerson(GroupsTestCase):

    def test_person_is_initiated_with_name_and_last_name(self):
        self.assertEqual(self.p1.name, 'Ali')
        self.assertEqual(self.p1.surname, 'Baba')
        self.assertEqual(self.p2.name, 'Johnny')
        self.assertEqual(self.p2.surname, 'Smith')

    def test_person_add_combines_their_names(self):
        p3 = self.p1 + self.p2
        self.assertEqual(p3.name, 'Ali')
        self.assertEqual(p3.surname, 'Smith')


class TestGroup(GroupsTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.group = Group('groupname', [self.p1, self.p2])

    def test_groups_should_contain_a_sequence_of_people(self):
        self.assertEqual(self.group.name, 'groupname')
        self.assertEqual(self.group.people, [self.p1, self.p2])

    def test_groups_should_return_detail_for_a_person_when_indexed(self):
        self.assertEqual(self.group[0], 'Person 0: Ali Baba')
        self.assertEqual(self.group[1], 'Person 1: Johnny Smith')

    def test_groups_should_return_how_mane_people_they_contain(self):
        self.assertEqual(len(self.group), 2)

    def test_str(self):
        self.assertEqual(str(self.group), 'Group groupname with members Ali Baba, Johnny Smith')

    def test_iteration_should_return_info_for_the_people(self):
        self.assertEqual(list(self.group), [
            'Person 0: Ali Baba',
            'Person 1: Johnny Smith'
        ])

    def test_adding_groups_should_combine_people(self):
        new_group = self.group + self.group
        self.assertEqual(len(new_group), 4)


if __name__ == '__main__':
    unittest.main()

