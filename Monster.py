from random import randint
from ansi_codes import txt,get_list_of_colours_fg,icons
import monster_messages
# Genders of all enemies are male right now, but later it will be randomised for extra detail
# Currently, only the Monster has random pre-attack talking lines depending on mental states. This will be extended to all enemies soon but im lazy rn whoops!
# Fort and Ego checks because later there will be additional dialogue for scenarios like high ego and low fortitude and etc. 

class Monster:
    # Construction
    def __init__(self,colour,adj):
        monsterMessageBank = monster_messages.get_monster_bank()
        self.resists = [["smash",0],["pierce",0],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "monster"
        self.maxHitPoints = 10
        self.hitPoints = self.maxHitPoints
        self.maxDamage = 5
        self.attackMessage = monsterMessageBank[randint(0, len(monsterMessageBank) - 1)]
        self.gold = randint(6,9)
        self.mentalFortitude = randint(0,100)
 
    # Getters
    def get_adj(self):
        return self.adj

    def get_species(self):
        return self.species
    
    def get_max_hp(self):
        return self.maxHitPoints

    def get_hitPoints(self):
        return self.hitPoints

    def getGold(self):
        return self.gold

    def getFortitude(self):
        return self.mentalFortitude

    def getEgo(self):
        return self.ego

    def getCode(self):
        return self.colourcode

    def getResists(self):
        return self.resists

    # Methods
    def attack(self): # Defines monster attack behaviour and returns the damage inflicted.
        damage = randint(0,self.maxDamage)
        if damage == 0:
            print("You successfully dodge the blow!")
        elif damage == 1:
            print("A glancing blow! You take 1 {}.".format(icons.heart))
        else:
            print(self.attackMessage + " You take "
                  + str(damage) + " {}.".format(icons.heart))
        return damage

    def receive_damage(self,damage,damagetype): # Subtracts damage from the monster and prints out related message.
        for loop in self.resists:
            if loop[0] == damagetype:
                damage -= loop[1]
        if damage <= 0:
            damage = 0
            print("Miss! The " + self.colourcode + self.species + "{} is too fast for you.".format(txt.sty.reset))
        elif damage == 1:
            print("You strike a glancing blow for 1 {}".format(icons.heart))
        else:
            print("The " + self.colourcode + self.species + "{} takes ".format(txt.sty.reset) + str(damage)
                  + " {}.".format(icons.heart))
        self.hitPoints -= damage

    def talk(self): # Prints monster's battle cry
        highIntelligence = monster_messages.get_monster_intel_talk()
        normalMonster = monster_messages.get_monster_norm_talk()

        fortitude = self.mentalFortitude

        if fortitude >= 70:
            print('The Monster announces: {}"{}"{}'.format(self.colourcode,highIntelligence[randint(0, len(highIntelligence) - 1)],txt.sty.reset)) 
        else:
            print('The Monster squeals: {}"{}"{}'.format(self.colourcode,normalMonster[randint(0, len(normalMonster) - 1)],txt.sty.reset))  

class Goblin(Monster):
    # Construction
    def __init__(self,colour,adj):
        super().__init__(colour,adj)
        goblinMessageBank = monster_messages.get_goblin_bank()
        self.resists = [["smash",0],["pierce",0],["slash",2]]
        self.species = "goblin"
        self.maxHitPoints = 12
        self.hitPoints = self.maxHitPoints
        self.maxDamage = 6
        self.attackMessage = goblinMessageBank[randint(0, len(goblinMessageBank) - 1)]
        self.gold = randint(6,18)
     # Methods
    def talk(self):
        highIntelligence = monster_messages.get_goblin_intel_talk()
        normalGob = monster_messages.get_goblin_norm_talk()

        fortitude = self.getFortitude()

        if fortitude >= 70:
            print('The Goblin says: {}"{}"{}'.format(self.colourcode,highIntelligence[randint(0, len(highIntelligence) - 1)],txt.sty.reset)) 
        else:
            print('The Goblin chimes: {}"{}"{}'.format(self.colourcode,normalGob[randint(0, len(normalGob) - 1)],txt.sty.reset))  

class Vampire(Monster):

    # Construction
    def __init__(self,colour,adj):
        vampireMessageBank = monster_messages.get_vampire_bank()
        self.resists = [["smash",0],["pierce",4],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "vampire"
        self.maxHitPoints = 20
        self.hitPoints = self.maxHitPoints
        self.maxDamage = 7
        self.attackMessage = vampireMessageBank[randint(0, len(vampireMessageBank) - 1)]
        self.gold = randint(5,15)
        self.mentalFortitude = randint(0,100)
 
    # Methods
    def talk(self):

        highIntelligence = monster_messages.get_vampire_intel_talk()

        normalVamp = monster_messages.get_vampire_norm_talk()

        fortitude = self.getFortitude()

        if fortitude >= 70:
            print('The Vampire says: {}"{}"{}'.format(self.colourcode,highIntelligence[randint(0, len(highIntelligence) - 1)],txt.sty.reset)) 
        else:
            print('The Vampire shrieks: {}"{}"{}'.format(self.colourcode,normalVamp[randint(0, len(normalVamp) - 1)],txt.sty.reset))  


class Slime(Monster):

    # Construction
    def __init__(self,colour,adj):
        slimeMessageBank = monster_messages.get_slime_bank()
        self.resists = [["smash",4],["pierce",0],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "slime"
        self.maxHitPoints = 8
        self.hitPoints = self.maxHitPoints
        self.maxDamage = 4
        self.attackMessage = slimeMessageBank[randint(0, len(slimeMessageBank) - 1)]
        self.gold = randint(2,9)
        self.mentalFortitude = randint(0,100)
 
    # Methods

    def talk(self):

        highIntelligence = monster_messages.get_slime_intel_talk()

        normalSlime = monster_messages.get_slime_norm_talk()

        fortitude = self.getFortitude()

        if fortitude >= 70:
            print('The Slime gurgles: {}"{}"{}'.format(self.colourcode,highIntelligence[randint(0, len(highIntelligence) - 1)],txt.sty.reset)) 
        else:
            print('The Slime gurgles: {}"{}"{}'.format(self.colourcode,normalSlime[randint(0, len(normalSlime) - 1)],txt.sty.reset))  


class RogueWarrior(Monster):

    # Construction
    def __init__(self,colour,adj):
        rogueMessageBank = monster_messages.get_rogue_bank()
        self.resists = [["smash",4],["pierce",2],["slash",3]]
        self.adj = adj
        self.colourcode = colour
        self.species = "rogue warrior"
        self.maxHitPoints = 25
        self.hitPoints = self.maxHitPoints
        self.maxDamage = 6
        self.attackMessage = rogueMessageBank[randint(0, len(rogueMessageBank) - 1)]
        self.gold = randint(12,27)
        self.mentalFortitude = randint(0,100)
 
    # Methods
    def talk(self):

        highFortandEgoRogue = monster_messages.get_rogue_intel_talk()

        normalRogue = monster_messages.get_goblin_norm_talk()

        fortitude = self.getFortitude()

        if fortitude >= 70:
            print('The Rogue Warrior spits: {}"{}"{}'.format(self.colourcode,highFortandEgoRogue[randint(0, len(highFortandEgoRogue) - 1)],txt.sty.reset)) 
        else:
            print('The Rogue Warrior ululates: {}"{}"{}'.format(self.colourcode,normalRogue[randint(0, len(normalRogue) - 1)],txt.sty.reset))  

