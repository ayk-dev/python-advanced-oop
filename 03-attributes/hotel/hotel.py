class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f'{stars_count} stars Hotel'
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        search_room = [r for r in self.rooms if r.number == room_number]
        res = search_room[0].take_room(people)
        if res is None:
            self.guests += people
        else:
            return res

    def free_room(self, room_number):
        search_room = [r for r in self.rooms if r.number == room_number]
        res = search_room[0].free_room()
        if res is None:
            self.guests -= search_room[0].guests
        else:
            return res

    def print_status(self):
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {", ".join([str(r.number) for r in self.rooms if not r.is_taken])}')
        print(f'Taken rooms: {", ".join([str(r.number) for r in self.rooms if r.is_taken])}')




