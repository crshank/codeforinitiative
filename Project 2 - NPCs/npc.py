import random

hair_color = ["blonde", "black", "brown", "gray", "red"]

occupation = ["teacher", "blacksmith", "alchemist", "shopkeeper", "guard", "rat catcher"]

personality_traits = ["abrasive", "cautious", "detached", "easygoing", "jolly", "inattentive", "suspicious"]

def npc_generator(hair_color, occupation, personality_traits):
    master_list = [hair_color, occupation, personality_traits]

    selected = []

    for trait_list in master_list:
        selected.append(random.choice(trait_list))

    if selected[1] == "rat catcher":
        selected[1] = "exterminator"
    elif selected[2] == "easygoing":
        selected[2] = "easy-going"
    elif selected[0] == "brown":
        selected[0] = "purple"

    if selected[2][0] in "aeiou":
        return "The random NPC is an {} {} with {} hair.".format(selected[2], selected[1], selected[0])
    else:
        return "The random NPC is a {} {} with {} hair.".format(selected[2], selected[1], selected[0])

for i in range(5):
    print npc_generator(hair_color, occupation, personality_traits)

