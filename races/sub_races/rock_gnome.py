from races.gnome import Gnome


class RockGnome(Gnome):
    def __init__(self):
        self.racial_bonuses['CON'] = 1

    def __str__(self):
        return 'Rock-Gnome'
