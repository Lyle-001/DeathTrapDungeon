from random import randint
from ansi_codes import txt,icons
import Items as it
import Equipment as eq
from validation import validate_int_input

class Shop:
    def __init__(self):
        self.enterMessage = "you enter the shop"
        self.persistentWareList = [] # always appears, near infinite available
        self.strangeWareList = [] # appears sometimes and only in one quantity per shop
        self.exclusiveWareList = [] # rare to appear and only in one quantity per shop. never appears if you have it in your inventory

    def generate_stock(self,inv):
        stock = []
        for item in self.persistentWareList:
            stock.append([item,randint(20,50)])
        for item in self.strangeWareList:
            if randint(0,100) < 70:
                stock.append([item,1])
        for item in self.exclusiveWareList:
            if randint(0,100) < 30: # NEED TO IMPLEMENT CHECKING THE INVENTORY FOR THE PIECE OF EQUIPMENT
                stock.append([item,1])
        return stock

    def shop(self,hero,inventory):
        print(self.enterMessage)
        wareList = self.generate_stock(inventory)
        while True:

            print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)
            for i in range(0,len(wareList),1):
                item = wareList[i]
                print(str(i+1) + ". " + item[0].name + " - " + item[0].description + "\t\t " + str(item[0].value) + icons.gold)

            choice = input("Does much of anything catch your eye? Y/N ").upper()
            if choice == "N":
                return
            bought = False
            while not bought: #check they've chosen an option that's valid
                try:
                    choice = validate_int_input("After much deliberation, you decide to take item... ") - 1
                    bought = hero.purchase(wareList[choice][0].value)
                    if not bought:
                        print("You check your coin pouch, only to find you cannot afford the luxury of that item!")
                        choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                        if choice == "N":
                            return
                except:
                    print("That's not right, you think, there is no option " + str(choice + 1) + "!")
                    choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                    if choice == "N":
                        return
            item = wareList[choice][0]
            print()
            if inventory.add_general_item([item,1]):
                wareList[choice][1] -= 1
                if wareList[choice][1] <= 0:
                    del wareList[choice]
                print("You successfully bought the item.")
            else:
                hero.set_gold(item.value)
                print("You have been refunded.")

class Apothecary(Shop):
    def __init__(self):
        self.enterMessage = "You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you."
        self.persistentWareList = [it.DilutedHealingElixir(),it.ImpureHealingElixir(),it.DistilledHealingElixir()]
        self.strangeWareList = [it.MysteryElixir()]
        self.exclusiveWareList = []

class Blacksmith(Shop):
    def __init__(self):
        self.enterMessage = "You enter the workshop to find a young man hammering at a piece of glowing iron."
        self.persistentWareList = []
        self.strangeWareList = []
        self.exclusiveWareList = [eq.MailHood(),eq.MailHauberk(),eq.MailGloves(),eq.MailChausse(),eq.MailBoots(),
                    eq.SteelHelm(),eq.SteelBreastplate(),eq.SteelGauntlets(),eq.SteelGreaves(),eq.SteelSabatons()]

class Clothier(Shop):
    def __init__(self):
        self.enterMessage = "You enter the homely building. An old man is sitting behind the counter, sewing together a boy's shirt."
        self.persistentWareList = []
        self.strangeWareList = []
        self.exclusiveWareList = [eq.LeatherGauntlets(),eq.LeatherShoes(),
                    eq.WoolGambeson(),
                    eq.ClothHat(),eq.ClothShirt(),eq.ClothGloves(),eq.ClothTrousers(),eq.ClothCloths()]