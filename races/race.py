from abc import abstractmethod


class Race:
    speed = 30
    size = 'medium'
    languages = ['common']
    racial_bonuses = dict()
    traits = list()

    @abstractmethod
    def __str__(self):
        return NotImplemented

    @property
    def to_string(self):
        return self.__str__()
