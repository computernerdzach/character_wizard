from races.Elf import Elf


class HighElf(Elf):
    def __init__(self):
        super().__init__()
        self.racial_bonuses['int'] = 1
        self.traits.append('elf-weapon-training')
        self.traits.append('high-elf-cantrip')
        self.traits.append('extra-language')

    def __str__(self):
        return 'high elf'
