from races.race import Race


class Gnome(Race):
    def __init__(self):
        self.speed = 25
        self.racial_bonuses = {'INT': 2}
        self.size = 'small'
        self.languages = ['gnomish']
        self.sub_races.append('rock-gnome', 'deep-gnome')
        self.traits.append('darkvision', 'gnome-cunning')
        for tongue in Race.languages:
            self.languages.append(tongue)

    sub_races = ('Rock-Gnome', 'Deep-Gnome')

    def __str__(self):
        return 'Gnome'
