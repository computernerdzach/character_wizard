from races.Dwarf import Dwarf


class HillDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.racial_bonuses['wis'] = 1
        self.traits.append('dwarven-toughness')

    def __str__(self):
        return 'hill dwarf'
