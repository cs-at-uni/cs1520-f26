from random import randint

class Die(object):
    def __init__(self):
        self.num_sides = 6

    def roll(self):
        return randint(1,self.num_sides)


class CustomSidedDie(Die):
    def __init__(self, sides):
        self.num_sides = sides


class SettableDie(CustomSidedDie):
    def __init__(self, sides):
        self.num_sides = sides

    def setRoll(self, val_to_set):
        self.rolled_value = val_to_set

    def roll(self):
        return self.rolled_value


if __name__=='__main__':
    #my_die = Die()
    my_die = CustomSidedDie(20)
    #print(my_die)
    #print(my_die.roll())

    for _ in range(6):
        print(my_die.roll())

    #big_die = CustomSidedDie(20)
    #print(big_die)
    #print(big_die.roll())

