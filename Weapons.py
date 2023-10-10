from random import randint,random
from math import e,sqrt,pi

# Weapons have different stats, such as:
# damage
# modifier (affects damage and damage chance)
# damage chance



#####   MODIFIER STUFF   #####


modifiersDict = {"broken":[-3,-12],
                 "awful":[-2,-8],
                 "shoddy":[-1,-4],
                 "common":[0,0],
                 "rare":[1,2],
                 "mighty":[2,4],
                 "epic":[3,6],
                 "godly":[4,8],
                 "legendary":[5,10]}
modifiersList = ["broken","awful","shoddy","common","rare","mighty","epic","godly","legendary"]


#####   END OF MODIFIER STUFF   #####


class Weapon:
    def __init__(self):
        self.name = "unknown weapon"
        self.modifier = 0
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
            return "modifier out of range"

    def randomise_modifier_old(self,luck):
        # luck of 1 is normal luck
        luck = int(luck * 50) # fudge factor, having the luck at this value seems to provide pretty good standard odds

        # algorithm to provide a bell curve
        modifier = len(modifiersDict) - 1
        luckLeft = luck
        for loop in range(0,luck,1):
            choice = randint(0,luckLeft)
            if choice == 0:
                if modifier > 0: # stops the modifier getting bigger than the list of modifiers
                    modifier -= 1
            luckLeft -= 1
        self.modifier = modifiersList[modifier]

    def randomise_modifier(self,luck):

        def set_modifier_curve(sigma,mu,x): # function-ception. i bet you didnt know you could do this
            return (1/(sigma * sqrt(2*pi))) * e**((-1/2) * ((x-mu)/sigma)**2)
        modifierCurveLower = -1.5
        modifierCurveHigher = 1.5

        # estimate the integral by splitting it up into trapeziums gcse-style
        modifierCount = len(modifiersList)
        segmentWidth = (modifierCurveHigher-modifierCurveLower)/modifierCount
        integralList = [0]
        for i in range(1,modifierCount,1):
            areaLowerHeight = set_modifier_curve(0.4,luck,modifierCurveLower + segmentWidth * (i-1))
            areaUpperHeight = set_modifier_curve(0.4,luck,modifierCurveLower + segmentWidth * i)
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
    
    def attack(self):
        if randint(1,100) <= self.damageChance + self.modifiers[self.modifier][2]:
            print(self.hitMessage)
            return self.damage + self.modifiers[self.modifier][1]
        else:
            print(self.missMessage)
            return 0

    def inspect(self):
        print(self.inspectMessage)

class ClassicSword(Weapon):
    def __init__(self):
        self.name = "sword"
        self.modifier = 4
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

class AxeOfFlames(Weapon):
    def __init__(self):
        self.name = "Axe of Flames"
        self.modifier = 4
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
        self.modifier = 4
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