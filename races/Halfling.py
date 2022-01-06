from races.Race import Race


class Halfling(Race):
    sub_races = ['Vanilla', 'LightfootHalfling']

    def __init__(self):
        self.speed = 25
        self.racial_bonuses['dex'] = 2
        self.size = 'small'
        self.languages = ['halfling']
        self.traits.append('brave')
        self.traits.append('halfling-nimbleness')
        self.traits.append('lucky')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Halfling'
