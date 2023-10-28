from random import randint,random
from math import e,sqrt,pi
from ansi_codes import txt,get_list_of_colours_fg

# Weapons have different stats, such as:
# damage
# modifier (affects damage and damage chance)
# damage chance


class Weapon:



    def __init__(self):
        self.modifiers = [["{}Broken".format(txt.col.fg.strg.grey),-3,-12],
                         ["{}Awful".format(txt.col.fg.nml.black),-2,-8],
                         ["{}Shoddy".format(txt.col.fg.nml.black),-1,-4],
                         ["{}Common".format(txt.col.fg.nml.white),0,0],
                         ["{}Rare".format(txt.col.fg.nml.blue),1,2],
                         ["{}Mighty".format(txt.col.fg.strg.blue),2,4],
                         ["{}Epic".format(txt.col.fg.nml.magenta),3,6],
                         ["{}Godly".format(txt.col.fg.nml.yellow),4,8],
                         ["{}{}Legendary".format(txt.col.fg.strg.yellow,txt.sty.bold),5,10]]
        self.maxStack = 1
        self.value = 1

    def get_tags(self=None):
        return ["weapon","shopExclusive"]


    def get_attacks(self):
        return self.attacks

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
                return True
        print("{}Modifier does not exist...{}".format(txt.col.fg.nml.red,txt.sty.reset))
        return False

    def set_modifier_curve(self,x=0,mu=0): # This is for customisation. the dev can easily define a new modifier_curve function without copy pasting the big function
        return {"value":(1/(0.4 * sqrt(2*pi))) * e**((-1/2) * ((x-mu)/0.4)**2),
                "lowerBound":-1.5,
                "upperBound":1.5}



    def randomise_modifier(self,luck=0):

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


    def use(self,hero,inventory): # Swaps the active weapon out for this one.
        cachedWeapon = inventory.inv[0][0][:]
        inventory.delete_item(self)
        if cachedWeapon[1] != "":
            inventory.add_item(cachedWeapon[1],"weapons",cachedWeapon[2])
        inventory.inv[0][0][1] = self
        inventory.inv[0][0][2] = 1
        inventory.update_numbering()



    def inspect(self):
         return "{}{}{}".format(get_list_of_colours_fg()[0][randint(0,len(get_list_of_colours_fg()[0])-1)],self.inspectMessage,txt.sty.reset)

##########################
##### Actual Weapons #####
##########################

class ClassicSword(Weapon):
    def __init__(self):
        super().__init__()
         
        self.attacks = ["slash","pierce"]
        self.name = "sword"
        self.description = "A standard arming sword."
        self.damage = 6
        self.damageChance = 90
        self.hitMessage = "Your blade strikes the enemy, cutting deep."
        self.missMessage = "The foul being afore you evades the assault."
        self.inspectMessage = "The weight of the sword you wield brings comfort."
        
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class Axe(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["slash"]
        self.name = "axe"
        self.description = "May or may not have previously been used to cut trees."
        self.damage = 8
        self.damageChance = 70
        self.hitMessage = "The axe embeds into the enemy with your strong swing."
        self.missMessage = "You are sent staggering by the momentum of your missed attack."
        self.inspectMessage = "A small inscription lies on the handle, reading \"M.K\". Probably the blacksmith."
        
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class Dagger(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["pierce"]
        self.name = "dagger"
        self.description = "A light, discreet blade. Perfect for an assassin."
        self.damage = 5
        self.damageChance = 100
        self.hitMessage = "You manage to drive your dagger hilt-deep into the enemy."
        self.missMessage = "Your jab misses entirely, only piercing the air."
        self.inspectMessage = "Flipping it over your hand, you can't help but remark on the lightness of this dagger."
         
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class Scimitar(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["slash"]
        self.name = "scimitar"
        self.description = "Freshly imported from a far-away land. Looks really cool."
        self.damage = 6
        self.damageChance = 90
        self.hitMessage = "The curve of the blade allows for a wider slash at the enemy, which you take advantage of."
        self.missMessage = "The unorthodox shape of the scimitar doesn't lend itself to your skill, missing entirely."
        self.inspectMessage = "Running your finger along the curved blade, you recognise what a formidable weapon it truly is."
         
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class Mace(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["slash"]
        self.name = "mace"
        self.description = "Someone got a baton and decided to make it look more like a torture device."
        self.damage = 6
        self.damageChance = 90
        self.hitMessage = "The mace crashes down into the enemy, with audibly broken bones."
        self.missMessage = "The mace crashes into the ground, missing the enemy by inches."
        self.inspectMessage = "The heavy implement almost has a mind of its own with its inertia."
         
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class Hammer(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["smash"]
        self.name = "hammer"
        self.description = "A large warhammer, able to deliver large, smashing blows."
        self.damage = 9
        self.damageChance = 60
        self.hitMessage = "The heavy head of the hammer ploughs into their side."
        self.missMessage = "The weight of the weapon slows it too much to hit the enemy."
        self.inspectMessage = "\"Would you like... another nail?\" - A wise philosopher."
         
    def get_tags(self=None):
        return ["weapon","starterWeapon","shopExclusive","blacksmithSellable"]

class AxeOfFlames(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["slash","smash","pierce"]
        self.name = "Axe of Flames"
        self.description = "\"Prometheus stole fire from the gods and gave it to man. For this, he was chained to a rock and tortured for eternity.\""
        self.damage = 8
        self.damageChance = 80
        self.hitMessage = ("The burning edge sparks fires under the enemy's skin.")
        self.missMessage = ("Even though the axe misses, the flaming blade still sparks fear.")
        self.inspectMessage = ("Hefting the axe, even you are intimidated by the fires it could start.")
         
    def get_tags(self=None):
        return ["weapon","legendaryWeapon","shopExclusive","blacksmithSellable"]

class SwordOfSouls(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["slash","smash","pierce"]
        self.name = "Sword of Souls"
        self.description = "A sword that has caused so much death it has become living. Probably previously used by an evil sorcerer or something."
        self.damage = 10
        self.damageChance = 95
        self.hitMessage = ("The blade strikes with the force of a thousand souls.")
        self.missMessage = ("Singing through the air, you can almost hear the screams of thousands.")
        self.inspectMessage = ("You look at the gemstones, and watch the spirits echoing around inside them.")
         
    def get_tags(self=None):
        return ["weapon","legendaryWeapon","shopExclusive","blacksmithSellable"]

class Fisticuffs(Weapon):
     
    def __init__(self):
        super().__init__()
        self.attacks = ["smash"]
        self.name = "Fisticuffs"
        self.description = "Your bare fists."
        self.damage = 2
        self.damageChance = 40
        self.hitMessage = "You punch the enemy right in the guts."
        self.missMessage = "You swing your fist at the enemy."
        self.inspectMessage = "You look at your bloodied and clothed fists."
        self.maxStack = 1
        self.value = 1
        self.modifiers = [["",0,0]]
    def get_tags(self=None):
        return ["weapon"]





weaponList = [ClassicSword,Axe,Dagger,Scimitar,Mace,Hammer,AxeOfFlames,SwordOfSouls]