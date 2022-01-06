from races.Race import Race


class Tiefling(Race):

    def __init__(self):
        self.racial_bonuses['int'] = 1
        self.racial_bonuses['cha'] = 2
        self.size = 'small'
        self.languages = ['infernal']
        self.traits.append('darkvision')
        self.traits.append('hellish-resistance')
        self.traits.append('infernal-legacy')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Tiefling'
