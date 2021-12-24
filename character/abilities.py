from random import randint


class Abilities:
    abilities = {
        'str': 0,
        'dex': 0,
        'con': 0,
        'int': 0,
        'wis': 0,
        'cha': 0
    }
    # modifiers = {
    #     'str': 0,
    #     'dex': 0,
    #     'con': 0,
    #     'int': 0,
    #     'wis': 0,
    #     'cha': 0
    # }

    def __init__(self, **kwargs):
        # TODO add validation
        self.abilities.update(kwargs)



    # @staticmethod
    # def update_ability():


    @staticmethod
    def roll_stats() -> list:
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
    def assigned_stats(self, rolls: list) -> dict:
        unused_stats = ['str', 'dex', 'con', 'int', 'wis', 'cha']
        unused_scores = rolls
        stat_dict = {
            'str': 0,
            'dex': 0,
            'con': 0,
            'int': 0,
            'wis': 0,
            'cha': 0
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
        self.modifiers['str'] = (self.STR - 10) // 2
        self.modifiers['dex'] = (self.DEX - 10) // 2
        self.modifiers['con'] = (self.CON - 10) // 2
        self.modifiers['wis'] = (self.WIS - 10) // 2
        self.modifiers['int'] = (self.INT - 10) // 2
        self.modifiers['cha'] = (self.CHA - 10) // 2
        return self.modifiers

    def roll_assign_abilities(self):
        rolls = self.roll_stats()
        assigned_stats = self.assigned_stats(self, rolls)
        self.STR = assigned_stats['str']
        self.DEX = assigned_stats['dex']
        self.CON = assigned_stats['con']
        self.WIS = assigned_stats['wis']
        self.INT = assigned_stats['int']
        self.CHA = assigned_stats['cha']
        self.calculate_modifiers()


