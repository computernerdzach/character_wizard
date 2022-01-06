from races.Race import Race


class Dragonborn(Race):

    def __init__(self):
        self.racial_bonuses['str'] = 2
        self.racial_bonuses['cha'] = 1
        self.languages = ['draconic']
        self.traits.append('draconic-ancestry')
        self.traits.append('breath-weapon')
        self.traits.append('damage-resistance')

        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Dragonborn'
