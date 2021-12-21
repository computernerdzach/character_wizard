from random import randint


class Abilities:
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0

    @staticmethod
    def roll_stats() -> list():
        all_rolls = list()
        for stat in range(6):
            rolls = list()
            for die in range(4):
                roll = randint(0, 6)
                rolls.append(roll)
            rolls.remove(min(rolls))
            stat = sum(rolls)
            all_rolls.append(stat)
        return all_rolls

    def assign_stats(self, rolls: list()):
        unused_stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        unused_scores = rolls
        stat_mappings = {
            'STR': self.STR,
            'DEX': self.DEX,
            'CON': self.CON,
            'INT': self.INT,
            'WIS': self.WIS,
            'CHA': self.CON
        }
        while len(unused_scores) > 0:
            print('Unassigned stats:')
            for i, stat in enumerate(unused_stats):
                print(i, stat)
            print('Unassigned scores:')
            for j, score in enumerate(unused_scores):
                print(j, score)
            stat_answer = input('Stat >')
            score_answer = input('Score >')

            stat_selection = unused_stats[int(stat_answer)]
            score_selection = unused_scores[int(score_answer)]

            stat_mappings[stat_selection] = int(score_selection)

            # print(stat_selection)
            # print(score_selection)

            unused_stats.remove(unused_stats[int(stat_answer)])
            unused_scores.remove(unused_scores[int(score_answer)])

    def roll_assign_abilities(self):
        rolls = self.abilities.roll_stats()
        self.abilities.assign_stats(rolls)

    # my_stats = roll_stats()
    # assign_stats(my_stats)

    modifiers = {
        'str': STR / 2,
        'dex': DEX / 2,
        'con': CON / 2,
        'int': INT / 2,
        'wis': WIS / 2,
        'cha': CHA / 2
    }
