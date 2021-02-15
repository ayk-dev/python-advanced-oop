from project.rooms.room import Room


class Everland:
    rooms: list

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.get_monthly_expense() + room.room_cost for room in self.rooms])

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        pass

    def status(self):
        pass

