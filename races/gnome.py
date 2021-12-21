from races.race import Race


class Gnome(Race):
    speed = 25
    racial_bonuses = {'Con': 1}

    def __str__(self):
        return 'Gnome'
