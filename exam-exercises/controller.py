from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        pass

    def add_card(self, type: str, name: str):
        pass

    def add_player_card(self, username: str, card_name: str):
        pass

    def fight(self, attack_name: str, enemy_name: str):
        pass

    def report(self):
        pass

