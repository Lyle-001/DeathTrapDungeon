from random import randint
from ansi_codes import txt,icons
import Items as it
import Equipment as eq
from validation import validate_int_input
from inventoryfile import get_items_with_tags

class Shop:
    def __init__(self,inv):
        self.enterMessage = "you enter the shop"
        self.name = "shop"
        self.tag = "shopSellable"
        self.wareList = self.generate_stock(inv)

    def generate_stock(self,inv):
        stock = []

        persistentItems = get_items_with_tags(["shopPersistent"])
        strangeItems = get_items_with_tags(["shopStrange"])
        exclusiveItems = get_items_with_tags(["shopExclusive"])
        sellableItems = get_items_with_tags([self.tag])
        persistentItems = list( set(sellableItems) & set(persistentItems) )
        strangeItems = list( set(sellableItems) & set(strangeItems) )
        exclusiveItems = list( set(sellableItems) & set(exclusiveItems) )

        alreadyOwned = inv.get_inv_items_with_tags([self.tag])
        for item in persistentItems:
            stock.append([item(),randint(20,50)])
        for item in strangeItems:
            if randint(1,100) < 70:
                stock.append([item(),1])
        for item in exclusiveItems:
            if randint(1,100) < 30:
                inInv = False
                for ownedItem in alreadyOwned:
                    if isinstance(ownedItem,item):
                        inInv = True
                        break
                if not inInv:
                    stock.append([item(),1])
        return stock

    def shop(self,hero,inventory):
        print(self.enterMessage)
        while True:

            print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)
            for i in range(0,len(self.wareList),1):
                item = self.wareList[i]
                print(str(i+1) + ". " + item[0].name + " - " + item[0].description + "\t\t " + str(item[0].value) + icons.gold)

            choice = input("Does much of anything catch your eye? Y/N ").upper()
            if choice == "N":
                return
            bought = False
            while not bought: #check they've chosen an option that's valid
                try:
                    choice = validate_int_input("After much deliberation, you decide to take item... ") - 1
                    bought = hero.purchase(self.wareList[choice][0].value)
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
            item = self.wareList[choice][0]
            print()
            if inventory.add_item(item,count = 1):
                self.wareList[choice][1] -= 1
                if self.wareList[choice][1] <= 0:
                    del self.wareList[choice]
                print("You successfully bought the item.")
            else:
                hero.set_gold(item.value)
                print("You have been refunded.")

class Apothecary(Shop):
    def __init__(self,inv):
        self.enterMessage = "You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you."
        self.name = "Apothecarial Tent"
        self.tag = "apothecarySellable"
        self.wareList = self.generate_stock(inv)

class Blacksmith(Shop):
    def __init__(self,inv):
        self.enterMessage = "You enter the workshop to find a young man hammering at a piece of glowing iron."
        self.name = "Blacksmith"
        self.tag = "blacksmithSellable"
        self.wareList = self.generate_stock(inv)

class Clothier(Shop):
    def __init__(self,inv):
        self.enterMessage = "You enter the homely building. An old man is sitting behind the counter, sewing together a boy's shirt."
        self.name = "Clothier's"
        self.tag = "clothierSellable"
        self.wareList = self.generate_stock(inv)