from jobs.Job import Job


class Barbarian(Job):
    hit_die = 12
    saving_throw_proficiencies = ('str', 'con')

    def __str__(self):
        return 'Barbarian'
