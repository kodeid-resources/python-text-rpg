from characters.player import Player, Commands


def main():
    p = Player()
    p.name = input("What is your character's name? ")
    print("(type help to get a list of actions) \n")
    print("{} enter a dark cave, searching for an adventure.".format(p.name))

    while(p.health > 0):
        print(p.health)
        line = input(">> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](p)
                    commandFound = True
                    break
            if not commandFound:
                print("{} doesn't understand the suggestion.".format(p.name))


main()
