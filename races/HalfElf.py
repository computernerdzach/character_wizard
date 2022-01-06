from races.Race import Race


class HalfElf(Race):
    def __init__(self):
        self.racial_bonuses['cha'] = 2
        self.languages = ['elvish']
        self.traits.append('darkvision')
        self.traits.append('fey-ancestry')
        self.traits.append('skill-versatility')
        for tongue in Race.languages:
            self.languages.append(tongue)

    def __str__(self):
        return 'Half Elf'
