from random import randint
from .character import Character
from .enemy import Enemy


class Player(Character):
    def __init__(self, state='normal', *args):
        super().__init__(self, *args)
        self.state = state
    def __str__(self):
        return "{}'s health: {}/{}".format(self.name, self.health, self.health_max)


    def quit(self):
        print("{} can't find the way back home, and dies of starvation.\nR.I.P.".format(self.name))
        self.health = 0
    def help(self):
        print(Commands.keys())
    def status(self):
        print(self)
    def tired(self):
        print("{} feels tired. Need a rest.".format(self.name))
        self.health = max(1, self.health - 1)
    def rest(self):
        if self.state != 'normal':
            print("{} can't rest right now!".format(self.name))
            self.enemy_attacks()
        else:
            print("{} rests.".format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("{} is rudely awakened by {}!".format(self.name, self.enemy.name))
                self.state = 'fight'
                self.enemy_attacks()
            else:
                if self.health < self.health_max:
                    self.health += 1
                else:
                    print("{} sleep too much.".format(self.name))
                    self.health -= 1
    def explore(self):
        if self.state != 'normal':
            print("{} is too busy right now!".format(self.name))
            self.enemy_attacks()
        else:
            print("{} explores a twisty passange.".format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("{} enconters {}".format(self.name, self.enemy.name))
                self.state = 'fight'
            else:
                if randint(0, 1): self.tired()
    def flee(self):
        if self.state != 'fight':
            print("{} runs in circles for a while".format(self.name))
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print("{} flees from {}".format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print("{} couldn't escape from {}".format(self.name, self.enemy.name))
    def attack(self):
        if self.state != 'fight':
            print("{} swats the air, without notable results.".format(self.name, self.tired()))
        else:
            if self.do_damage(self.enemy):
                print("{} executes {}".format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
                if randint(0, self.health) < 10:
                    self.health += 1
                    self.health_max += 1
                    print("{} feels stronger!".format(self.name))
                else:
                    self.enemy_attacks()
    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print("{} was slaughtered by {}!!!\n R.I.P".format(self.name, self.enemy.name))
Commands = {
    'quit': Player.quit,
    'help': Player.help,
    'status': Player.status,
    'rest': Player.rest,
    'explore': Player.explore,
    'flee': Player.flee,
    'attack': Player.attack
}
