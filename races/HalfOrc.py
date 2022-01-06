from races.Race import Race


class HalfOrc(Race):

    def __init__(self):
        self.racial_bonuses['str'] = 2
        self.racial_bonuses['con'] = 1
        self.languages = ['orc']
        self.traits.append('darkvision')
        self.traits.append('savage-attacks')
        self.traits.append('relentless-endurance')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Half Orc'
