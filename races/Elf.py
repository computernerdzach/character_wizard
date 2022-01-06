from races.Race import Race


class Elf(Race):
    sub_races = ['Vanilla', 'HighElf']

    def __init__(self):
        self.speed = 30
        self.racial_bonuses['dex'] = 2
        self.languages = ['elvish']
        self.traits.append('darkvision')
        self.traits.append('trance')
        self.traits.append('fey-ancestry')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Elf'
