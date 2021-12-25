import json
from Ability import Ability
from races.Race import Race
from jobs.Job import Job


class Character:
    def __init__(self, race: Race, job: Job, c_name: str, p_name: str, test: bool = False):
        self.race = race
        self.job = job
        self.str = Ability()
        self.dex = Ability()
        self.con = Ability()
        self.int = Ability()
        self.wis = Ability()
        self.cha = Ability()

        if test:
            self.load_test_data()
        self.c_name = c_name
        self.p_name = p_name
        self.languages = race.languages
        self.add_bonuses()

    def __str__(self):
        return self.c_name

    def load_test_data(self):
        with open("test_data/ability_scores.json", "r") as f:
            data = json.load(f)
            for key, value in data.items():
                attr = getattr(self, key)
                attr.update(value)

    def display_scores(self):
        print('Ability / Score / Modifier')
        for ability in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            score = getattr(self, ability).score
            modifier = getattr(self, ability).modifier
            print("{: >7} / {:>5} / {:>8}".format(ability.upper(), score, modifier))

    def add_bonuses(self):
        for key, value in self.race.racial_bonuses.items():
            ability = getattr(self, key)
            ability.score += value

    @property
    def speed(self):
        return self.race.speed

    @property
    def hit_die(self):
        return self.job.hit_die
