from argparse import ArgumentParser

from races.gnome import Gnome
from races.sub_races.rock_gnome import RockGnome
from jobs.barbarian import Barbarian
from character.character import Character

available_races = ['gnome', 'rock-gnome']
available_classes = ['barbarian']

race_mapping = {
    'gnome': Gnome,
    'rock-gnome': RockGnome
}
job_mapping = {
    'barbarian': Barbarian
}

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--race", choices=available_races, required=True)
    parser.add_argument("--job", choices=available_classes, required=True)
    parser.add_argument("--player-name", default='Player')
    parser.add_argument("--character-name", default='Character')
    args = parser.parse_args()

    race = race_mapping[args.race]()
    job = job_mapping[args.job]()

    character = Character(race, job, args.player_name, args.character_name, test=True)

    abilities_dict = {
        'str': character.str,
        'dex': character.dex,
        'int': character.int,
        'wis': character.wis,
        'con': character.con,
        'cha': character.cha
    }

    print(f'{character.p_name} made a {character.race} {character.job}.')
    print(f'{character.str.score}: {character.str.modifier}')
    character.display_scores()





"""
race_mapping = {
    'Gnome': Gnome,
    'Rock-Gnome': RockGnome
}
job_mapping = {
    'Barbarian': Barbarian
}
races_with_subraces = {
    'Gnome': ['Rock-Gnome', 'Deep-Gnome']
}


def make_character(race: str, job: str, character: str, player: str) -> Character:
    race = race_mapping[race]()
    job = job_mapping[job]()
    # abilities = Abilities()
    character = Character(race, job, str(character), str(player))
    return character


def check_for_sub_race(race) -> str:
    if race.sub_races:
        print('Please select your sub-race:')
        for sub_race in race.sub_races:
            print(sub_race)
        sub_race_choice = input('> ')
        if sub_race_choice == 'Vanilla':
            x = race.to_string()
            return x
        else:
            return sub_race_choice


def get_selections():
    race_choice = input('Please enter race. >')
    race_choice = check_for_sub_race(race_mapping[race_choice])
    job_choice = input('Please enter job. >')
    character_name = input('Please enter your character\'s name. >')
    player_name = input('Please enter your real name. >')
    return {'race': race_choice, 'job': job_choice, 'character': character_name, 'player': player_name}


choices = get_selections()
zach = make_character(race=choices['race'], job=choices['job'],
                      character=choices['character'], player=choices['player'])

print(f"{zach.p_name} created a {zach.race} {zach.job} named {zach.c_name}. {zach.c_name} has a speed of {zach.speed} "
      f"and a d{zach.hit_die} hit die.")

print(f"{zach.c_name}'s strength score is {zach.STR}, giving them a {zach.modifiers['STR']} modifier.")

print(f"{zach.c_name} speaks the following languages:")
for tongue in zach.languages:
    print(tongue)
"""