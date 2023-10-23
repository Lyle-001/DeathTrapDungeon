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

            print("\nWhat would you like to do?")
            print("Buy item (type \"buy\" + the item number)")
            print("Sell item (type \"sell\")")
            print("Exit (type \"exit\")")
            selling = False
            valid = False
            while not valid:
                valid = True
                choice = input()
                if choice.lower() == "exit": # deals with the exit command
                    return
                elif choice.lower() == "sell": # deals with the sell command
                    selling = True
                else:
                    choice = choice.split(" ",1) # splits the command into 2 sections: the command and the target item
                    if len(choice) == 2:
                        command = choice[0].lower()
                        target = choice[1]
                        if command != "buy": # deals with the buy command
                            valid = False
                        if target.isdigit():
                            target = int(target)
                            if target < 1 or target > len(self.wareList):
                                valid = False
                        else:
                            valid = False

                    else:
                        valid = False
                if not valid:
                    print("Please enter a valid option.") # now the user input is validated


            if not selling:
                self.buy(target,hero,inventory)
            else:
                self.sell(hero,inventory)

    def buy(self,choice,hero,inventory):
        choice -= 1
        item = self.wareList[choice][0]
        print()
        if "weapon" in item.get_tags() and not inventory.weaponsSectionFull:
            item.randomise_modifier()
            section = "weapons"
        else:
            section = "general"
        if inventory.add_item(item,section):
            self.wareList[choice][1] -= 1
            if self.wareList[choice][1] <= 0:
                del self.wareList[choice]
            print("You successfully bought the item.")
        else:
            hero.set_gold(item.value)
            print("You have been refunded.")

    def sell(self,hero,inventory):
        while True:
            inventory.print_inventory(hero)
            print("What would you like to do?")
            print("Sell item (type \"sell\" + the item number)")
            print("Exit inventory (type \"exit\")")
            valid = False
            while not valid:
                valid = True
                choice = input()
                if choice.lower() == "exit": # deals with the exit command
                    return
                choice = choice.split(" ",1) # splits the command into 2 sections: the command and the target item
                if len(choice) == 2:
                    command = choice[0].lower()
                    target = choice[1]
                    if command != "sell":
                        valid = False
                    if target.isdigit():
                        target = int(target)
                        if target < 1 or target >= inventory.activeSlotCount:
                            valid = False
                    else:
                        valid = False

                else:
                    valid = False
                if not valid:
                    print("Please enter a valid option.") # now the user input is validated

            # find the referenced item
            itemFound = False
            for section in inventory.inv:
                for item in section:
                    if item[0] == target:
                        target = item[1]
                        itemFound = True
                        break
                if itemFound:
                    break

            if self.tag in target.get_tags():
                hero.set_gold(target.value)
                inventory.delete_item(target)
                print("Item sold!")
            else:
                print("The merchant refuses to take this type of item.")


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