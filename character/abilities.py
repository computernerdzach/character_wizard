from random import randint


class Abilities:
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0
    modifiers = {
        'str': 0,
        'dex': 0,
        'con': 0,
        'int': 0,
        'wis': 0,
        'cha': 0
    }

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

    @staticmethod
    def assigned_stats(self, rolls: list()) -> dict:
        unused_stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        unused_scores = rolls
        stat_dict = {
            'STR': 0,
            'DEX': 0,
            'CON': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0
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
            stat_dict[stat_selection] = int(score_selection)
            unused_stats.remove(unused_stats[int(stat_answer)])
            unused_scores.remove(unused_scores[int(score_answer)])
        return stat_dict

    def calculate_modifiers(self):
        self.modifiers['STR'] = (self.STR - 10) // 2
        self.modifiers['DEX'] = (self.DEX - 10) // 2
        self.modifiers['CON'] = (self.CON - 10) // 2
        self.modifiers['WIS'] = (self.WIS - 10) // 2
        self.modifiers['INT'] = (self.INT - 10) // 2
        self.modifiers['CHA'] = (self.CHA - 10) // 2

    def roll_assign_abilities(self):
        rolls = self.abilities.roll_stats()
        assigned_stats = self.abilities.assigned_stats(self, rolls)
        self.STR = assigned_stats['STR']
        self.DEX = assigned_stats['DEX']
        self.CON = assigned_stats['CON']
        self.WIS = assigned_stats['WIS']
        self.INT = assigned_stats['INT']
        self.CHA = assigned_stats['CHA']
        self.calculate_modifiers()


