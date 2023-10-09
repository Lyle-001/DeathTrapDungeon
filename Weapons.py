from numbers import Integral
from random import randint,random

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
    def __init__(self,modifier):
        self.name = "unknown weapon"
        self.modifier = "common"
        self.damage = randint(1,100)
        self.damageChance = randint(1,100)
        self.hitMessage = ("You did something and it worked!?")
        self.missMessage = ("I don't even know what weapon this is, of course you wouldn't be able to swing it!")
        self.inspectMessage = ("It looks unexplainable. How did you get this?")

    def get_name(self):
        return self.modifier + " " + self.name

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
        luck = random() # doing this until i figure out a good way to actually have it randomise, if it breaks the balance of the game tell me and ill speed up the production of a real solution.

        def set_modifier_curve(x): # function-ception. i bet you didnt know you could do this
            return (-1*x**2 + 1)**3
        self.modifierCurveLower = -1
        self.modifierCurveHigher = 1

        modifierCount = len(modifiersList)
        segmentWidth = (self.modifierCurveHigher-self.modifierCurveLower)/modifierCount
        integralList = [0]
        for i in range(1,modifierCount,1):
            areaLowerHeight = set_modifier_curve(self.modifierCurveLower + segmentWidth * (i-1))
            areaUpperHeight = set_modifier_curve(self.modifierCurveLower + segmentWidth * i)
            area = areaLowerHeight * segmentWidth
            area += (areaUpperHeight - areaLowerHeight) * segmentWidth / 2
            integralList.append(area + integralList[i-1])

        integral = integralList[1] + integralList[len(integralList) - 1]
        luck *= integral
        
        for i in range(0,len(integralList),1):
            if luck < integralList[i]:
                self.modifier = modifiersList[i-1]
                return
        self.modifier = modifiersList[len(modifiersList)-1]
    
    def attack(self):
        if randint(1,100) <= self.damageChance + modifiersDict[self.modifier][1]:
            print(self.hitMessage)
            return self.damage + modifiersDict[self.modifier][0]
        else:
            print(self.missMessage)
            return 0

    def inspect(self):
        print(self.inspectMessage)

class ClassicSword(Weapon):
    def __init__(self,modifier):
        self.name = "sword"
        self.modifier = "common"
        self.damage = 6
        self.damageChance = 90
        self.hitMessage = ("You slash the monster with your sword-like sword.")
        self.missMessage = ("You slash the air with your sword-like sword")
        self.inspectMessage = ("Your sword feels solid in your hands.")

class AxeOfFlames(Weapon):
    def __init__(self,modifier):
        self.name = "Axe of Flames"
        self.modifier = "common"
        self.damage = 8
        self.damageChance = 80
        self.hitMessage = ("The cold metal hacks the enemy, while the fire burns their wound.")
        self.missMessage = ("Your enemy is intimated by a wall of flames.")
        self.inspectMessage = ("You examine the flaming axe. Your enemies will surely know fear.")

class SwordOfSouls(Weapon):
    def __init__(self,modifier):
        self.name = "Sword of Souls"
        self.modifier = "common"
        self.damage = 10
        self.damageChance = 95
        self.hitMessage = ("Your enemy is struck with the blood of thousands.")
        self.missMessage = ("Your enemy hears the souls trapped within the blade.")
        self.inspectMessage = ("You unsheathe the sword. A threatening aura surrounds it.")