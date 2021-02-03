class CardRepository:
    def __init__(self):
        self.count: int = 0
        self.cards: list = []

    def add(self, card: 'Card object'):
        try:
            c = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f'Card {card.name} already exists!')
        except IndexError:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError('Card cannot be an empty string!')
        c = [c for c in self.cards if c.name == card][0]
        self.cards.remove(c)
        self.count -= 1

    def find(self, name: str):
        card = [c for c in self.cards if c.name == name][0]
        return card



