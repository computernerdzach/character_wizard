import sys
from argparse import ArgumentParser

from Character import Character
from jobs.Job import Job
from races.Race import Race


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--race", choices=Race.AVAILABLE, required=True)
    parser.add_argument("--job", choices=Job.AVAILABLE, required=True)
    parser.add_argument("--player-name", default='Player')
    parser.add_argument("--character-name", default='Character')
    args = parser.parse_args()

    race = str_to_class(args.race)()
    job = str_to_class(args.job)()

    character = Character(race, job, args.character_name, args.player_name, test=True)
    print(f'{character.p_name} made a {str(character.race).title()} {str(character.job).title()} named {character.c_name}.')
    character.display_scores()
    print(f'Armor Class: {character.armor_class}')
    print(f'{character.c_name} knows the following languages: {character.languages}')
