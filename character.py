################################################################
#####            VENTURE VOID - CHARACTER MAKER            #####
################################################################
import os, time, random, time, funcs

## Character class to standardize basic fields -- to be extended with child subclasses
class Character(object):
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100 ## Starting Health - To be changed/rolled
        self.max_health = 100 ## Maximum Health - To be changed/rolled
        self.strength = 10
        self.defense = 10
        self.luck = random.randint(1,100)
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.is_alive = True ## Flag to check if character is alive :(
        print(f"\n\n----- Out of the misty mountains of your mind steps {self.name}! -----\n")
        print(f"\n\n----- After gazing upon their figure, you are in awe of their abilities! -----\n")
        print(f"  Name: {self.name}\n  Health: {self.health}\n  Strength: {self.strength}\n  Defense: {self.defense}\n  Luck: {self.luck}\n")
    
    # Announces your character to the world
    def announce_yaself(self):
        print(f"{self.name} is HERE to FIGHT!\n")

    # Results of taking damage mitigated by defense (if any)
    def take_damage(self, damage):
        net_damage = (damage - self.defense)
        result_damage = max(0, net_damage)
        print(f'{self.name} has level {self.defense} armor, so the {damage} point attack resulted in {result_damage} damage!\n')
        # Update health & possibly life
        self.health -= result_damage
        self.health = max(0,self.health)
        if self.health <= 0:
            self.is_alive = False
            print(f'Alas, it seems {self.name} bit the dust - oh well, they were just a phantom!')

    # How to level up a character
    def level_up(self):
        self.level += 1
        self.max_health += funcs.diceRoll(self.luck)
        self.health = self.max_health
        self.strength += funcs.diceRoll(self.luck)
        print(f'-----> {self.name} leveled up to level {self.level}!\n')
        print(f'New Max Health: {self.max_health}; New Strength: {self.strength}')

    # How to gain experience
    def gain_experience(self, xp):
        self.experience += xp
        print(f'-----> {self.name} gained {xp} experience, up to {self.experience}!!\n')
        if self.experience >= 100:
            self.level_up()
            self.experience = 0


## SUBCLASS of Character
class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.arcana = funcs.diceRoll(self.luck)
    
    def cast_spell(self):
        ying = funcs.diceRoll(100)
        yang = funcs.diceRoll(100)
        spell_damage = self.arcana*(ying/yang)

def take_damage(player: Character):
    while True:
        action = input("\nDo you want to take damage? (Y/N) --> ")
        time.sleep(1)
        if action.lower() == 'y':
            player.announce_yaself()
            dmg = random.randint(1,100)
            player.take_damage(dmg)
            if player.health > 0:
                continue
            elif player.health <= 0:
                print(f"Suddenly silence.... Somewhere a faint whisper... 'Ah crap {player.name} ded.'")
                break
            else:
                print("Some kind of player health comparison error!!!!")
                break
        elif action.lower() == 'n':
            print("\nAight goodbye!")
            break
        else:
            print("\nSorry dawg I don't know what you want.")