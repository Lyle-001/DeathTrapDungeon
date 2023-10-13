from random import randint,random
from math import e,sqrt,pi
from ansi_codes import txt

# Weapons have different stats, such as:
# damage
# modifier (affects damage and damage chance)
# damage chance


class Weapon:



    def __init__(self):
        self.name = "unknown weapon"
        self.damage = randint(1,100)
        self.damageChance = randint(1,100)
        self.hitMessage = ("You did something and it worked!?")
        self.missMessage = ("I don't even know what weapon this is, of course you wouldn't be able to swing it!")
        self.inspectMessage = ("It looks unexplainable. How did you get this?")
        self.modifiers = [["unobtainable",0,0]]




    def get_name(self):
        try:
            return self.modifiers[self.modifier][0] + " " + self.name
        except:
            return self.name

    ####################################
    ##### Modifier-Related Methods #####
    ####################################

    def set_modifier(self,name):
        for i in range(0,len(self.modifiers),1):
            if self.modifiers[i][0] == name:
                self.modifier = i
                return
        print("{}Modifier does not exist...{}",format(txt.col.fg.nml.red,txt.sty.reset))

    def set_modifier_curve(self,x=0,mu=0): # This is for customisation. the dev can easily define a new modifier_curve function without copy pasting the big function
        return {"value":(1/(0.4 * sqrt(2*pi))) * e**((-1/2) * ((x-mu)/0.4)**2),
                "lowerBound":-1.5,
                "upperBound":1.5}



    def randomise_modifier(self,luck):

        bounds = self.set_modifier_curve() # get the bounds from the set_modifier_curve function. allows the dev to create new weapon modifier curves without copy pasting the complicated function
        modifierCurveHigher = bounds["upperBound"]
        modifierCurveLower = bounds["lowerBound"]

        # estimate the integral by splitting it up into trapeziums gcse-style
        modifierCount = len(self.modifiers)
        segmentWidth = (modifierCurveHigher-modifierCurveLower)/modifierCount
        integralList = [0]
        for i in range(1,modifierCount,1):
            areaLowerHeight = self.set_modifier_curve(modifierCurveLower + segmentWidth * (i-1),luck)["value"]
            areaUpperHeight = self.set_modifier_curve(modifierCurveLower + segmentWidth * i,luck)["value"]
            area = areaLowerHeight * segmentWidth
            area += (areaUpperHeight - areaLowerHeight) * segmentWidth / 2
            integralList.append(area + integralList[i-1])

        choice = random()
        
        for i in range(1,len(integralList),1):
            if choice <= integralList[i]:
                self.modifier = i-1
                return
        if luck >= 0:
            self.modifier = len(self.modifiers)-1
        else:
            self.modifier = 0

    #########################
    ##### Other Methods #####
    #########################
    
    def attack(self):
        if randint(1,100) <= self.damageChance + self.modifiers[self.modifier][2]:
            print(self.hitMessage)
            return self.damage + self.modifiers[self.modifier][1]
        else:
            print(self.missMessage)
            return 0




    def inspect(self):
        print(self.inspectMessage)

##########################
##### Actual Weapons #####
##########################

class ClassicSword(Weapon):
    def __init__(self):
        self.name = "sword"
        self.damage = 6
        self.damageChance = 90
        self.hitMessage = ("You slash the monster with your sword-like sword.")
        self.missMessage = ("You slash the air with your sword-like sword")
        self.inspectMessage = ("Your sword feels solid in your hands.")
        self.modifiers = [["broken",-3,-12],
                         ["awful",-2,-8],
                         ["shoddy",-1,-4],
                         ["common",0,0],
                         ["rare",1,2],
                         ["mighty",2,4],
                         ["epic",3,6],
                         ["godly",4,8],
                         ["legendary",5,10]]

class Axe(Weapon):
    def __init__(self):
        self.name = "axe"
        self.damage = 8
        self.damageChance = 70
        self.hitMessage = ("You slice your enemy with your wieldly axe.")
        self.missMessage = ("You waste energy swinging your axe about.")
        self.inspectMessage = ("Looking at your axe, you notice a small inscribing on the handle. Probably the craftsman's.")
        self.modifiers = [["broken",-3,-12],
                         ["awful",-2,-8],
                         ["shoddy",-1,-4],
                         ["common",0,0],
                         ["rare",1,2],
                         ["mighty",2,4],
                         ["epic",3,6],
                         ["godly",4,8],
                         ["legendary",5,10]]

class Dagger(Weapon):
    def __init__(self):
        self.name = "dagger"
        self.damage = 5
        self.damageChance = 100
        self.hitMessage = ("You stab your enemy right in their guts.")
        self.missMessage = ("You try to stab them but you can't get close enough.")
        self.inspectMessage = ("You marvel at how lightweight this blade is.")
        self.modifiers = [["broken",-3,-12],
                         ["awful",-2,-8],
                         ["shoddy",-1,-4],
                         ["common",0,0],
                         ["rare",1,2],
                         ["mighty",2,4],
                         ["epic",3,6],
                         ["godly",4,8],
                         ["legendary",5,10]]

class AxeOfFlames(Weapon):
    def __init__(self):
        self.name = "Axe of Flames"
        self.damage = 8
        self.damageChance = 80
        self.hitMessage = ("The cold metal hacks the enemy, while the fire burns their wound.")
        self.missMessage = ("Your enemy is intimated by a wall of flames.")
        self.inspectMessage = ("You examine the flaming axe. Your enemies will surely know fear.")
        self.modifiers = [["Broken",-3,-12],
                         ["Awful",-2,-8],
                         ["Shoddy",-1,-4],
                         ["Common",0,0],
                         ["Rare",1,2],
                         ["Mighty",2,4],
                         ["Epic",3,6],
                         ["Godly",4,8],
                         ["Legendary",5,10]]

class SwordOfSouls(Weapon):
    def __init__(self):
        self.name = "Sword of Souls"
        self.damage = 10
        self.damageChance = 95
        self.hitMessage = ("Your enemy is struck with the blood of thousands.")
        self.missMessage = ("Your enemy hears the souls trapped within the blade.")
        self.inspectMessage = ("You unsheathe the sword. A threatening aura surrounds it.")
        self.modifiers = [["Broken",[-3,-12]],
                         ["Awful",[-2,-8]],
                         ["Shoddy",[-1,-4]],
                         ["Common",[0,0]],
                         ["Rare",[1,2]],
                         ["Mighty",[2,4]],
                         ["Epic",[3,6]],
                         ["Godly",[4,8]],
                         ["Legendary",[5,10]]]