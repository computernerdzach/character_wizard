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
        self.armor_class = 10

        if test:
            self.load_test_data()
        self.c_name = c_name
        self.p_name = p_name
        self.languages = race.languages
        self.add_bonuses()
        self.calculate_raw_armor_class()

    def __str__(self):
        return self.c_name

    def calculate_raw_armor_class(self):
        self.armor_class += self.dex.modifier
        if self.job.__str__() == 'barbarian':
            self.armor_class += self.con.modifier

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

    def details(self):
        print(f'{self.p_name} made a {str(self.race).title()} {str(self.job).title()} named {self.c_name}.')
        self.display_scores()
        print(f'Armor Class: {self.armor_class}')
        print(f'{self.c_name} knows the following languages: {self.languages}')
        print(f'{self.c_name} has the following traits:')
        for trait in self.race.traits:
            print(trait)
        print()
        print('And they are proficient at the following saving throws:')
        for ability in self.job.saving_throw_proficiencies:
            print(f'- {ability}')

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
