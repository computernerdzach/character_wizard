from abc import abstractmethod


class Race:
    AVAILABLE = ['Gnome', 'RockGnome', 'Dragonborn', 'Dwarf', 'HillDwarf',
                 'Elf', 'HighElf', 'HalfElf', 'HalfOrc', 'Halfling',
                 'LightfootHalfling']
    speed = 30
    size = 'medium'
    languages = ['common']
    racial_bonuses = dict()
    traits = list()

    @abstractmethod
    def __str__(self):
        return NotImplemented

    def to_string(self):
        return self.__str__()
