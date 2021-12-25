from argparse import ArgumentParser

from Character import Character
from jobs.Job import Job
from races.Race import Race
from util import str_to_class

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--race", choices=Race.AVAILABLE, required=True)
    parser.add_argument("--job", choices=Job.AVAILABLE, required=True)
    parser.add_argument("--player-name", default='Player')
    parser.add_argument("--character-name", default='Character')
    args = parser.parse_args()

    race = str_to_class('races', args.race)()
    job = str_to_class('jobs', args.job)()

    character = Character(race, job, args.character_name, args.player_name, test=True)
    print(character.details)
