from random import randint
from ansi_codes import txt
from inventoryfile import inventory



#############################
########## Potions ##########
#############################

class DilutedHealingElixir:
    def __init__(self):
        self.name = "{}Diluted Healing Elixir{}".format(txt.col.fg.nml.red,txt.sty.reset)
        self.description = "Heals small wounds."
        self.inspect = "This vial contains a semi-red liquid. There are a few glittery particles inside."
        self.useMessage = "The weak elixir eases you slightly, but isn't the most pleasant..."
        self.value = 4
        self.maxStack = 5
        self.healingPower = [3,7]

    def get_value(self):
        return self.value

    def inspect(self):
        return self.inspect

    def use(self,hero):
        healAmount = randint(self.healingPower[0],self.healingPower[1])
        hero.heal(healAmount)
        print(self.useMessage)
        return healAmount

class ImpureHealingElixir(DilutedHealingElixir):
    def __init__(self):
        self.name = "{}Impure Healing Elixir{}".format(txt.col.fg.strg.red,txt.sty.reset)
        self.description = "Heals wounds."
        self.inspect = "This conical flask contains a red liquid. There are a few glittery particles inside."
        self.useMessage = "Your wounds feel somewhat better, and you feel full of a new vigour."
        self.value = 10
        self.maxStack = 5
        self.healingPower = [5,10]

class DistilledHealingElixir(DilutedHealingElixir):
    def __init__(self):
        self.name = "{}{}Distilled Healing Elixir{}".format(txt.col.fg.nml.red,txt.sty.bold,txt.sty.reset)
        self.description = "Heals major wounds."
        self.inspect = "This boiling flask contains a deep crimson liquid. There is a whirlpool of glistening particles inside."
        self.useMessage = "As the formulation pours down your throat, you feel better in body and soul, ready to take on the next fight!"
        self.value = 20
        self.maxStack = 5
        self.healingPower = [15,20]

class MysteryElixir:
    def __init__(self):
        self.name = "{}{}Mystery Elixir{}".format(txt.col.fg.nml.magenta,txt.sty.bold,txt.sty.reset)
        self.description = "An unknown elixir. Who knows what it does?"
        self.inspect = "This flask contains a greyish fluid. You cannot see anything through it."
        self.value = randint(3,20)
        self.maxStack = 1

    def use(self,hero):
        effect = randint(1,6)
        if effect <= 3: #weighted towards nothing
            print("As you drink it, you realise it is a phony elixir, with no effects other than an unpleasant taste.")
        elif effect == 4:
            print("The potion tastes vile, but turns out to be medicinal.")
            hero.heal(randint(5,10))
        elif effect == 5:
            print("You feel the flask's contents burning down your throat, causing you some discomfort.")
            hero.receiveDamage(randint(3,5))
        elif effect == 6:
            print("Too late you realise the recklessness of your drinking as poison spills down your throat, taking its effect in seconds.")
            hero.receiveDamage(1000) #there's more elegant ways to kill you, yes. there's also more elegant ways to make a game and i don't see them used here
            return



####################################
########## Clothier Items ##########
####################################

class PotionPouch:
    def __init__(self):
        self.name = "Potion Pouch"
        self.description = "Use this item to put on the pouch, giving you 5 potion slots."
        self.inspect = "A leather satchel in which you can store your vials and flasks."
        self.value = 5
        self.maxStack = 1

    def use(self,inv):
        inv.potionPouchCurrentSlots = inv.potionPouchSlots
        inv.hasPotionPouch = True
        return True