from random import randint
from inventoryfile import get_items_with_tags
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
    
    def __str__(self):
        print(self.name)

    def get_tags(self=None):
        return ["potion","healthPotion","unidentifiedElixirUsable","shopPersistent","apothecarySellable"]

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
            inventory.delete_item(self,1)
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
    def get_tags(self=None):
        return ["potion","healthPotion","unidentifiedElixirUsable","shopPersistent","apothecarySellable"]

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
    def get_tags(self=None):
        return ["potion","healthPotion","unidentifiedElixirUsable","shopPersistent","apothecarySellable"]

class MysteryElixir:
    def __init__(self):
        self.name = "{}{}Mystery Elixir{}".format(txt.col.fg.nml.magenta,txt.sty.bold,txt.sty.reset)
        self.description = "An unknown elixir. Who knows what it does?"
        self.inspectMessage = "This flask contains a greyish fluid. You cannot see anything through it."
        self.destroyOnUse = True
        self.value = randint(3,20)
        self.maxStack = 1
    def get_tags(self=None):
        return ["potion","unidentifiedElixirUsable","shopStrange","apothecarySellable"]

    def get_name(self):
        return self.name

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
        if self.destroyOnUse:
            inventory.delete_item(self,1)

class UnidentifiedElixir:
    def __init__(self):
        self.name = "Unidentified Elixir"
        self.potions = get_items_with_tags(["unidentifiedElixirUsable"])
        self.identity = self.potions[randint(0,len(self.potions)-1)]
        self.description = "You can't seem to decypher what kind of potion this is..."
        self.destroyOnUse = True
        self.value = randint(3,20)
        self.maxStack = 1
    def get_tags(self=None):
        return ["potion","apothecarySellable","shopStrange"]

    def get_name(self):
        return self.name

    def get_type(self):
        return "potion"

    def use(self,player,inv):
        potion = self.identity() # virtualises the potion that it is 
        potion.destroyOnUse = False # makes it so it doesnt destroy an item it doesnt actually have (its virtualised, not in the inventory)
        potion.use(player,inv) # use the virtualised potion
        if self.destroyOnUse:
            inv.delete_item(self,1) # destroy the unidentified potion, not the virtualised one

    def generate_inspect_message(self):
        if randint(1,100) < 30:
            # 30% chance of not being able to see anything
            inspectMessage = "You can't make out much through the murky glass of the flask."
        else:
            # 70% chance of being able to see something

            # define the different messages for the different potions
            if self.identity == DilutedHealingElixir:
                messages = ["doesn't smell of much","has a slight tinge of red to it"]

            elif self.identity == ImpureHealingElixir:
                messages = ["smells somewhat sweet","looks red"]

            elif self.identity == DistilledHealingElixir:
                messages = ["smells very sweet","is dark crimson"]

            elif self.identity == MysteryElixir:
                messages = ["smells bad","looks almost grey"]

            # invent the english language
            inspectMessage = "The potion "
            conjoiners = [". It ",", it "]
            enders = [".", "..."]
            thoughEnders = [" though.", " though..."]
            usedStatements = []

            # create the inspect message
            length = randint(1,2)
            for i in range(0,length,1):

                # find a message to use that hasnt been used already
                candidateFound = False
                while not candidateFound:
                    if len(usedStatements) >= len(messages):
                        break
                    candidate = randint(0,len(messages)-1)
                    if not candidate in usedStatements:
                        candidateFound = True

                # if we successfully found one:
                if candidateFound:
                    if i != length and i != 0:
                        # if its not the end of the message, add a conjunction (conjoiner)
                        inspectMessage += conjoiners[randint(0,len(conjoiners)-1)]
                    inspectMessage += messages[candidate]
                    usedStatements.append(candidate)

            # add the ending of the sentence (the ender)
            if length > 1 and randint(1,100) < 50:
                # if the message has two points in it, 50% chance of adding "though" to the end
                inspectMessage += thoughEnders[randint(0,len(thoughEnders)-1)]
            else:
                inspectMessage += enders[randint(0,len(enders)-1)]
        return inspectMessage

    def inspect(self,inventory):
        
        # STILL NEED TO ADD THE CODE FOR CHECKING IF THE POTION'S TRUE IDENTITY IS ALREADY IN THE PLAYER'S INVENTORY!
        #if inventory.is_in_inv(self.identity):
            #if self.destroyOnUse:
                #inventory.destroy_general_item
        
        return self.generate_inspect_message()



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
    def get_tags(self=None):
        return ["clothierSellable","shopStrange"]

    def get_name(self):
        return self.name

    def use(self,hero,inv):
        print("You put on the potion pouch, now you can store 5 more types of potion.")
        inv.hasPotionPouch = True
        inv.delete_item(self,1)
        inv.update_potion_pouch()
        return True

    def inspect(self):
        return self.inspectMessage

    def get_name(self):
        return self.name





itemList = [DilutedHealingElixir,ImpureHealingElixir,DistilledHealingElixir,MysteryElixir,UnidentifiedElixir,PotionPouch]