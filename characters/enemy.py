from .character import Character
from random import randint


class Enemy(Character):
    def __init__(self, player, *args):
        super().__init__(self, *args)
        self.name = 'a goblin'
        self.health = randint(1, player.health)
