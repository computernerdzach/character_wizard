from races.gnome import Gnome
from races.sub_races.rock_gnome import RockGnome
from jobs.barbarian import Barbarian
from character.character import Character

race_mapping = {
    'Gnome': Gnome,
    'Rock-Gnome': RockGnome
}
job_mapping = {
    'Barbarian': Barbarian
}


def make_character(race: str, job: str, character: str, player: str) -> Character:
    race = race_mapping[race]()
    job = job_mapping[job]()
    # abilities = Abilities()
    character = Character(race, job, str(character), str(player))
    return character


def check_for_sub_race(race) -> str:
    if race.sub_races:
        for sub_race in race.sub_races:
            print(sub_race)
        sub_race_choice = input('> ')
        if sub_race_choice == 'vanilla':
            return race.to_string
        else:
            return sub_race_choice

def get_selections():
    race_choice = input('Please enter race. >')
    job_choice = input('Please enter job. >')
    race_choice = check_for_sub_race(race_mapping[race_choice])
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
