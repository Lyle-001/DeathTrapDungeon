import random

class Monster:

    def __init__(self, adj):
        self.adj = adj
        self.species = "Monster"
        self.hitPoints = 10
        self.maxDamage = 5
        self.attackMessage = "Serrated talons tear at your skin."
        self.gold = random.randint(1,6)

    def getGold(self):
        return self.gold
    
    def getSpecies(self):
        return self.species

    def getAdj(self):
        return self.adj

    def getHitPoints(self):
        return self.hitPoints

    def attack(self):
        damage = random.randint(0, self.maxDamage)
        if damage < 1:
            print("You managed to dodge the blow. No damage!")
        elif damage == 1:
            print("A glancing blow! 1 damage.")
        else:
            print(self.attackMessage + " You receive " + str(damage) + " damage.")
        return damage
    
    def receiveDamage(self, damage):
        if damage == 0:
            print("You barely miss the " + self.species + ".")
        elif damage == 1:
            print("You manage to strike a glancing blow for 1 damage.")
        else:
            print("The " + self.species + " was struck for " + str(damage) + " damage.")
        self.hitPoints -= damage

    def talk(self):
        print("Its bloodcurdling cry shakes you to your core.")

    def death(self):
        print("The fascimile of nature lies broken at your feet. You step over, deeper into the dungeon.")

class Goblin(Monster):

    def __init__(self, adj):
        self.adj = adj
        self.species = "Goblin"
        self.hitPoints = 12
        self.maxDamage = 6
        self.attackMessage = "Its crude hammer crashes into your leg."
        self.gold = random.randint(3,5)

    def talk(self):
        print("The foul creature skitters across bloodstained flagstones towards you.")

    def death(self):
        print("A hoarse wail escapes its lips as the thing passes into the next life. You step around it, deeper into the dungeon.")
        
class Vampire(Monster):

    def __init__(self, adj):
        self.adj = adj
        self.species = "Vampire"
        self.hitPoints = 20
        self.maxDamage = 7
        self.attackMessage = "Its serrated teeth tear at your flesh."
        self.gold = random.randint(4,10)

    def talk(self):
        print("The room turns cold as it glides silently towards you.")

    def death(self):
        print("There was no need for a wooden stake with your prowess. You step over its remains, deeper into the dungeon.")
        
class Thrall(Monster):

    def __init__(self, adj):
        self.adj = adj
        self.species = "Thrall"
        self.hitPoints = 30
        self.maxDamage = 2
        self.attackMessage = "It swings blindly, striking you harshly."
        self.gold = random.randint(1,3)

    def attack(self):
        damage = random.randint(-3, self.maxDamage)
        if damage < 1:
            print("You managed to dodge the blow. No damage!")
        elif damage == 1:
            print("A glancing blow! 1 damage.")
        else:
            print(self.attackMessage + " You receive " + str(damage) + " damage.")
        if damage < 0:
            damage = 0
        return damage

    def talk(self):
        print("Lumbering towards you, the blank eyes reveal the spell it is under.")

    def death(self):
        print("With both spell and body broken, the fading innocent before you wakes for their final moments. You say a prayer and step around, deeper into the dungeon.")

class Chained(Monster):

    def __init__(self):
        self.adj = "Chained"
        self.species = "Demon"
        self.hitPoints = 30
        self.maxDamage = 2
        self.unchained = False
        self.attackMessage = "Its heavy chains bruise your arm."
        self.gold = random.randint(7,13)

    def attack(self):
        if self.hitPoints > 20: #if above threshold
            damage = random.randint(-3, self.maxDamage)
        elif not self.unchained: #only plays once, doesn't attack when played
            print("With your last blow intercepted by the cuffs, they shatter onto the ground.")
            print("Now free of its chains, the demon lets out a baleful cry!")
            self.unchained = True
            self.adj = "Freed"
            self.attackMessage = "Its talons burn as they tear across your flesh!"
            return 0
        else: #much more damage when low on health
            damage = random.randint(-5, 20)
        if damage < 1 and self.unchained:
            print("You feel the air cleaved apart as you dodge away!")
        elif damage < 1:
            print("It stumbles towards you, missing entirely.")
        elif damage == 1 and self.unchained:
            print("Even without them striking you, you feel the burning claws! 1 damage.")
        elif damage == 1:
            print("The chains barely catch on your arm, dealing 1 damage.")
        else:
            print(self.attackMessage + " You receive " + str(damage) + " damage.")
        if damage < 0:
            damage = 0
        return damage

    def death(self):
        print("You feel uneasy, as if sending it back to the hell it came from was a boon for it. You regain your calm and move on, deeper into the dungeon.")
