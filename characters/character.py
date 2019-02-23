from random import randint


class Character:
    def __init__(self, *args, **kwargs):
        self.name = ""
        self.health = 10
        self.health_max = 10

        for key, value in kwargs:
            setattr(self, key, value)
    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health
        )
        enemy.health = enemy.health - damage
        if damage == 0: print("{} evades {}'s attack.".format(enemy.name, self.name))
        else: print("{} hurts {}!".format(self.name, enemy.name))
        return enemy.health <= 0
