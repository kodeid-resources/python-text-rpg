from random import randint


class Character:
    def __init__(self):
        self.name = ""
        self.health = 1
        self.health_max = 1
    def attack(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health
        )
        enemy.health = enemy.health - damage
        if damage == 0: print("{} evades {}'s attack.", (enemy.name, self.name))
        else: print("{} hurts {}!".format(self.name, enemy.name))
        return enemy.health <= 0
