from races.race import Race
from jobs.job import Job
from character.abilities import Abilities


class Character:
    def __init__(self, race: Race, job: Job, c_name: str, p_name: str):
        self.race = race
        self.job = job
        self.abilities = Abilities()
        self.abilities.roll_assign_abilities()
        self.modifiers = self.abilities.calculate_modifiers()
        self.c_name = c_name
        self.p_name = p_name
        self.languages = race.languages

    def __str__(self):
        return self.c_name

    @property
    def speed(self):
        return self.race.speed

    @property
    def hit_die(self):
        return self.job.hit_die
