from races.Race import Race


class Dwarf(Race):
    sub_races = ['Vanilla', 'HillDwarf']

    def __init__(self):
        self.speed = 25
        self.racial_bonuses['con'] = 2
        self.languages = ['dwarvish']
        self.traits.append('darkvision')
        self.traits.append('dwarven-resilience')
        self.traits.append('stonecunning')
        self.traits.append('dwarven-combat-training')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Dwarf'
