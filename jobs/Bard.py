from jobs.Job import Job


class Bard(Job):
    hit_die = 8
    saving_throw_proficiencies = ('dex', 'cha')

    def __str__(self):
        return 'Bard'
