import random

def initiative_roll(character, modifier):

    roll = random.randint(1,20)

    total = roll + modifier 

    return "{} rolled {} with a modifier of {} for an initiative roll of {}.".format(character, roll, modifier, total)

print initiative_roll("Arthur", 2)
print initiative_roll("Liana", -1)
print initiative_roll("Sybil", 0)