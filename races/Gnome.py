from races.Race import Race


class Gnome(Race):
    sub_races = ['Vanilla', 'Rock-Gnome']

    def __init__(self):
        self.speed = 25
        self.racial_bonuses['int'] = 2
        self.size = 'small'
        self.languages = ['gnomish']
        self.traits.append('darkvision')
        self.traits.append('gnome-cunning')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Gnome'
