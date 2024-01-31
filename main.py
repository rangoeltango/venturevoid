###########################################
#####            VENTURE VOID         #####
###########################################
import os, time, random, funcs, character as char

## WELCOME TITLE DISPLAY
funcs.titlecard()
funcs.title()

## Welcome, create a character!
name = input("  Welcome to the void!\n  What shall we call your phantasmal champion?? --> ")
time.sleep(0.5)
player = char.Character(name)
funcs.q_continue()

print("Sorry just for now I'm creating a wizard tutor named Gargamel!")
narrator = char.Wizard('Gargamel')
narrator.cast_spell()
funcs.q_continue()


print("Time to level up...")
funcs.q_continue()
player.level_up()

print("Ready to leave?...")
funcs.q_continue()
funcs.goodbye()

## Two different ways of taking damage
#player.take_damage(random.randint(1,100))
#char.take_damage(player)





"""
name1 = input("Name your Legend: ")
type1 = input("Character Type (Human, Elf, Wizard, Orc): ")

time.sleep(1)

print("Legend: ", name1)

hp1 = character_health()
print("Health: ", hp1)

strength1 = character_strength()
print("Strength: ", strength1)

time.sleep(1)

print("Who are they battling?")

name2 = input("Name your Legend: ")
type2 = input("Character Type (Human, Elf, Wizard, Orc): ")
time.sleep(1)
print("Legend: ", name2)

hp2 = character_health()
print("Health: ", hp2)

strength2 = character_strength()
print("Strength: ", strength2)

print("BATTLE TIME!")
time.sleep(3)

round = 0

while True:
    print("rolling...")
    time.sleep(3)
    os.system("clear")
    char1roll = diceRoll(6)
    char2roll = diceRoll(6)
    damage = abs(strength1 - strength2) + 1
    if char1roll > char2roll:
        print(name1, "wins the round")
        hp2 = hp2 - damage
        print(name2, "takes a hit, with", damage, "damage")
        scoreBoard()
        if hp2 <= 0:
            print("Oh no", name2, "has died!")
            print(name1, "destroyed", name2, "in", round, "rounds!")
            break
        else:
            round += 1
            time.sleep(1)
            os.system("clear")
            continue
    elif char2roll > char1roll:
        print(name2, "wins the round")
        hp1 = hp1 - damage
        print(name1, "takes a hit, with", damage, "damage")
        scoreBoard()
        if hp1 <= 0:
            print("Oh no, ", name1, "has died!")
            print(name2, "destroyed", name1, "in", round, "rounds!")
            break
        else:
            round += 1
            time.sleep(1)
            os.system("clear")
            continue
    if char1roll == char2roll:
        print("Its a draw!")
        scoreBoard()
        round += 1
        time.sleep(1)
        os.system("clear")
        continue
"""