from races.race import Race


class Gnome(Race):
    def __init__(self):
        self.speed = 25
        self.racial_bonuses = {'INT': 2}
        self.size = 'small'
        self.languages = ['gnomish']
        self.traits.append('darkvision', 'gnome-cunning')
        for tongue in Race.languages:
            self.languages.append(tongue)

    sub_races = ('vanilla', 'rock-gnome')

    def __str__(self):
        return 'Gnome'
