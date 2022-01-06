from races.Halfling import Halfling


class LightfootHalfling(Halfling):
    def __init__(self):
        super().__init__()
        self.racial_bonuses['cha'] = 1
        self.traits.append('naturally-stealthy')

    def __str__(self):
        return 'Lightfoot Halfling'
