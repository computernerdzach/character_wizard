class Ability:
    score = 0

    def update(self, value: int):
        self.score = value

    @property
    def modifier(self):
        return (self.score - 10) // 2
