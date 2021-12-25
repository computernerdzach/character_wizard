from Character import Character
from util import str_to_class

if __name__ == '__main__':
    race = input("Race >")
    job = input("Class >")
    character_name = input("Character name >")
    player_name = input("Player name >")

    race = str_to_class('races', race)()
    job = str_to_class('jobs', job)()

    character = Character(race, job, character_name, player_name, test=True)
    print(character.details)
