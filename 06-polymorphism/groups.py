class Person:
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'unsupported operand type(s) for +: {self.__class__.__name__} and {other.__class__.__name__}')
        return Person(self.name, other.surname)

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    name: str
    people: 'list of Person instances'

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        name = self.name + other.name
        people = self.people + other.people
        return Group(name, people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        members = [p.__repr__() for p in self.people]
        return f'Group {self.name} with members {", ".join(members)}'

    def __getitem__(self, item):
        result = f'Person {item}: {self.people[item].name} {self.people[item].surname}'
        return result


def test_people_can_be_added_together():
    p1 = Person('t', 't')
    p2 = Person('T', 'T')

    assert (p1 + p2).full_name == 't T'
    print('test passed')


def add_person_with_something_else_should_raise_type_error():
    try:
        Person('t', 'T') + 3
    except TypeError:
        pass
    except Exception as e:
        assert False, f'expected TypeError, got {e.__class__.__name__}'
    else:
        assert False, f'expected TypeError, got nothing'
    print('test passed')

# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)