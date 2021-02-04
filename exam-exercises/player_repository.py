class PlayerRepository:
    def __init__(self):
        self.count: int = 0
        self.players: list = []

    def add(self, player: 'Player object'):
        name = player.username
        try:
            player = [p for p in self.players if p.username == name][0]
            raise ValueError(f'Player {name} already exists!')
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError('Player cannot be an empty string!')
        p = [p for p in self.players if p.username == player][0]
        self.players.remove(p)
        self.count -= 1

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player

