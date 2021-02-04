from player.player import Player


class Advanced(Player):
    def __init__(self, username):
        Player.__init__(self, username, 250)


adv_pl = Advanced('test name')
print(adv_pl.__doc__)
