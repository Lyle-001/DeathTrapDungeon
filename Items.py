from random import randint
from ansi_codes import txt



#############################
########## Potions ##########
#############################

class DilutedHealingElixir:
    def __init__(self):
        self.name = "{}Diluted Healing Elixir{}".format(txt.col.fg.nml.red,txt.sty.reset)
        self.description = "Heals small wounds."
        self.inspectMessage = "This vial contains a semi-red liquid. There are a few glittery particles inside."
        self.useMessage = "The weak elixir eases you slightly, but isn't the most pleasant..."
        self.destroyOnUse = True
        self.value = 4
        self.maxStack = 5
        self.healingPower = [3,7]

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def get_type(self):
        return "potion"

    def inspect(self):
        return self.inspectMessage

    def use(self,hero,inventory):
        healAmount = randint(self.healingPower[0],self.healingPower[1])
        hero.heal(healAmount)
        print(self.useMessage)
        if self.destroyOnUse:
            inventory.destroy_general_item([self,1])
        return healAmount

class ImpureHealingElixir(DilutedHealingElixir):
    def __init__(self):
        self.name = "{}Impure Healing Elixir{}".format(txt.col.fg.strg.red,txt.sty.reset)
        self.description = "Heals wounds."
        self.inspectMessage = "This conical flask contains a red liquid. There are a few glittery particles inside."
        self.useMessage = "Your wounds feel somewhat better, and you feel full of a new vigour."
        self.destroyOnUse = True
        self.value = 10
        self.maxStack = 5
        self.healingPower = [5,10]

class DistilledHealingElixir(DilutedHealingElixir):
    def __init__(self):
        self.name = "{}{}Distilled Healing Elixir{}".format(txt.col.fg.nml.red,txt.sty.bold,txt.sty.reset)
        self.description = "Heals major wounds."
        self.inspectMessage = "This boiling flask contains a deep crimson liquid. There is a whirlpool of glistening particles inside."
        self.useMessage = "As the formulation pours down your throat, you feel better in body and soul, ready to take on the next fight!"
        self.destroyOnUse = True
        self.value = 20
        self.maxStack = 5
        self.healingPower = [15,20]

class MysteryElixir:
    def __init__(self):
        self.name = "{}{}Mystery Elixir{}".format(txt.col.fg.nml.magenta,txt.sty.bold,txt.sty.reset)
        self.description = "An unknown elixir. Who knows what it does?"
        self.inspectMessage = "This flask contains a greyish fluid. You cannot see anything through it."
        self.value = randint(3,20)
        self.maxStack = 1

    def get_type(self):
        return "potion"

    def use(self,hero,inventory):
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
            hero.receiveDamage(1000000000) #there's more elegant ways to kill you, yes. there's also more elegant ways to make a game and i don't see them used here
            return
        inventory.destroy_general_item([self,1])

class UnidentifiedElixir:
    def __init__(self):
        self.potions = [DilutedHealingElixir(),ImpureHealingElixir(),DistilledHealingElixir(),MysteryElixir()]
        self.identity = self.potions[randint(0,len(self.potions)-1)]
        self.description = "You can't seem to decypher what kind of potion this is..."
        self.value = randint(3,20)
        self.maxStack = 1

    def get_type(self):
        return "potion"

    def use(self,player,inventory):
        self.identity.use(player,inventory)

    def inspect(self):

        if self.identity == DilutedHealingElixir():
            messages = ["The potion doesn't smell of much. It has a slight tinge of red to it though..."]
            return messages[randint(0,len(messages)-1)]

        elif self.identity == ImpureHealingElixir():
            messages = ["The potion smells somewhat sweet. It looks red..."]
            return messages[randint(0,len(messages)-1)]

        elif self.identity == DistilledHealingElixir():
            messages = ["The potion smells very sweet. It is dark crimson."]
            return messages[randint(0,len(messages)-1)]

        elif self.identity == MysteryElixir():
            messages = ["The potion smells bad. It looks almost grey..."]
            return messages[randint(0,len(messages)-1)]



####################################
########## Clothier Items ##########
####################################

class PotionPouch:
    def __init__(self):
        self.name = "Potion Pouch"
        self.description = "A leather satchel in which you can store your vials and flasks."
        self.inspectMessage = "Use this item to put on the pouch, giving you 5 potion slots."
        self.value = 5
        self.maxStack = 1

    def use(self,hero,inv):
        print("You put on the potion pouch, now you can store 5 more types of potion.")
        inv.potionPouchCurrentSlots = inv.potionPouchSlots
        inv.hasPotionPouch = True
        inv.update_potion_pouch()
        inv.destroy_general_item([self,1])
        return True

    def get_type(self):
        return "potion pouch"

    def inspect(self):
        return self.inspectMessage

    def get_name(self):
        return self.name
