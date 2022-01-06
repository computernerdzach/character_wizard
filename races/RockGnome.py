from races.Gnome import Gnome


class RockGnome(Gnome):
    def __init__(self):
        super().__init__()
        self.racial_bonuses['con'] = 1

    def __str__(self):
        return 'Rock Gnome'
