from jobs.Job import Job


class Barbarian(Job):
    hit_die = 12
    saving_throw_proficiencies = ('Str', 'Con')

    def __str__(self):
        return 'barbarian'
