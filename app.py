from races.gnome import Gnome
from jobs.barbarian import Barbarian
from character.character import Character

race_mapping = {
    'Gnome': Gnome
}
job_mapping = {
    'Barbarian': Barbarian
}


def make_character(race=str, job=str, character=str, player=str) -> Character:
    race = race_mapping[race]()
    job = job_mapping[job]()
    # abilities = Abilities()
    character = Character(race, job, str(character), str(player))
    return character


def get_selections():
    race_choice = input('Please enter race. >')
    job_choice = input('Please enter job. >')
    character_name = input('Please enter your character\'s name. >')
    player_name = input('Please enter your real name. >')
    return {'race': race_choice, 'job': job_choice, 'character': character_name, 'player': player_name}


choices = get_selections()
zach = make_character(choices['race'], choices['job'], choices['character'], choices['player'])

print(f"{zach.p_name} created a {zach.race} {zach.job} named {zach.c_name}. {zach.c_name} has a speed of {zach.speed} "
      f"and a d{zach.hit_die} hit die.")

print(f"{zach.c_name}'s strength score is {zach.STR}, giving them a {zach.modifiers['STR']} modifier.")
