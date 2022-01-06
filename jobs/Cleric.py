from jobs.Job import Job


class Cleric(Job):
    hit_die = 8
    saving_throw_proficiencies = ('wis', 'cha')

    def __str__(self):
        return 'Cleric'
