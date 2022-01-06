from jobs.Job import Job


class Druid(Job):
    hit_die = 8
    saving_throw_proficiencies = ('int', 'wis')

    def __str__(self):
        return 'Druid'
