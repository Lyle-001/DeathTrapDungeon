from random import randint

class Monster:

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "monster"
        self.hitPoints = 10
        self.maxDamage = 5
        self.attackMessage = "It slashes with its razor sharp claws."
        self.gold = randint(4,6)

    # Getters
    def get_colour(self):
        return self.colour

    def get_species(self):
        return self.species

    def get_hitPoints(self):
        return self.hitPoints

    def getGold(self):
        return self.gold

    # Methods
    def attack(self): # Defines monster attack behaviour and returns the damage inflicted.
        damage = randint(0,self.maxDamage)
        if damage == 0:
            print("You successfully dodge the blow!")
        elif damage == 1:
            print("A glancing blow! You take 1 ♡.")
        else:
            print(self.attackMessage + " You take "
                  + str(damage) + " ♡.")
        return damage

    def receive_damage(self,damage): # Subtracts damage from the monster and prints out related message.
        if damage == 0:
            print("Miss! The " + self.species + " is too fast for you.")
        elif damage == 1:
            print("You strike a glancing blow for 1 point of damage.")
        else:
            print("The " + self.species + " takes " + str(damage)
                  + " ♡.")
        self.hitPoints -= damage

    def talk(self): # Prints monster's battle cry
        print("ROAR!! I'm going to eat you!")

class Goblin(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "goblin"
        self.hitPoints = 12
        self.maxDamage = 6
        self.attackMessage = "It hits you with a club."
        self.gold = randint(4,12)

    # Methods
    def talk(self):
        print("Hee! Hee! I'm going to kill you and steal all your gold!")

class Vampire(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "vampire"
        self.hitPoints = 20
        self.maxDamage = 7
        self.attackMessage = "It sinks its fangs into your neck."
        self.gold = randint(3,10)

    # Methods
    def talk(self):
        print("I vant to drink your blood!")

class Slime(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "slime"
        self.hitPoints = 8
        self.maxDamage = 4
        self.attackMessage = "It tries to engulf you."
        self.gold = randint(0,6)

    # Methods
    def talk(self):
        print("Boooiiinnnggg!")

class RogueWarrior(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour +  "-shielded"
        self.species = "rogue warrior"
        self.hitPoints = 25
        self.maxDamage = 6
        self.attackMessage = "They slash at you."
        self.gold = randint(8,18)

    # Methods
    def talk(self):
        print("I'll kill you!")
