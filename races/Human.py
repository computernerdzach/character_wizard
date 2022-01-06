from races.Race import Race


class Human(Race):

    def __init__(self):
        self.racial_bonuses['str'] = 1
        self.racial_bonuses['dex'] = 1
        self.racial_bonuses['con'] = 1
        self.racial_bonuses['int'] = 1
        self.racial_bonuses['wis'] = 1
        self.racial_bonuses['cha'] = 1
        self.languages = list()
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Human'
