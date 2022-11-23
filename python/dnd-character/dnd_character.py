import random, math
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
    def ability(self):
        rolls = []
        for i in range(4):
            rolls.append(random.randint(0, 6))

        rolls.pop(rolls.index(min(rolls)))
        return sum(rolls)
def modifier(score):
    return math.floor((score - 10) / 2)


