#formatted

from random import randint
from ansi_codes import txt,icons,clearscreen
import Items as it
import Equipment as eq
from validation_and_functions import validate_int_input,RandomColour
from inventoryfile import get_items_with_tags

class Shop:
    def __init__(self,inv): 
        pass

    def find(self): 
        print(self.findMessage)

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
        clearscreen()
        print(self.enterMessage)
        while True:

            print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)
            for i in range(0,len(self.wareList),1):
                item = self.wareList[i]
                print(str(i+1) + ". " + item[0].name + " - " + item[0].description + "\t\t " + str(item[0].value) + icons.gold)

            print("\n{}What would you like to do?{}".format(txt.col.fg.nml.yellow,txt.sty.reset))
            print("{}\"Help\" for help{}".format(txt.col.fg.strg.grey,txt.sty.reset))
            selling = False
            valid = False
            leave = False
            while not leave:
                valid = True
                leave = True
                choice = input()
                if choice.lower() == "exit" or choice.lower() == "e": # deals with the exit command
                    return
                elif choice.lower() == "sell" or choice.lower() == "s": # deals with the sell command
                    selling = True
                elif choice.lower() == "help" or choice.lower() == "h": #do they need help with commands
                    leave = False
                    print("\n{}Buy item (type \"buy\" + the item number)".format(txt.col.fg.nml.green))
                    print("Sell item (type \"sell\")")
                    print("Exit (type \"exit\")")
                    print("Abbreviations are: \"b\", \"s\", \"e\" and \"h\" if you need anymore help.{}\n".format(txt.sty.reset))
                else:
                    choice = choice.split(" ",1) # splits the command into 2 sections: the command and the target item
                    if len(choice) == 2:
                        command = choice[0].lower()
                        target = choice[1]
                        if command != "buy" and command != "b": # deals with the buy command
                            valid = False
                            leave = False
                        if target.isdigit():
                            target = int(target)
                            if target < 1 or target > len(self.wareList):
                                valid = False
                                leave = False
                        else:
                            valid = False
                            leave = False

                    else:
                        valid = False
                        leave = False
                if not valid:
                    print("{}Please enter a valid option.{}".format(txt.warning,txt.sty.reset)) # now the user input is validated


            if not selling:
                self.buy(target,hero,inventory)
                input()
                clearscreen()
            else:
                self.sell(hero,inventory)
                clearscreen()

    def buy(self,choice,hero,inventory):
        choice -= 1
        item = self.wareList[choice][0]
        print()
        if "weapon" in item.get_tags():
            item.randomise_modifier()
            section = "weapons"
        else:
            section = "general"
        if inventory.add_item(item,section):
            self.wareList[choice][1] -= 1
            if self.wareList[choice][1] <= 0:
                del self.wareList[choice]
            print("{}You successfully bought {}{}".format(txt.col.fg.nml.yellow,item.get_name(),txt.sty.reset))
            hero.set_gold(item.value*-1)
        else:
            hero.set_gold(item.value) 
            print("{}You have been refunded.{}".format(txt.col.fg.nml.yellow,txt.sty.reset))

    def sell(self,hero,inventory):
        while True:
            inventory.print_inventory(hero)
            print("\n{}What would you like to do?{}".format(txt.col.fg.nml.yellow,txt.sty.reset))
            print("{}\"Help\" for help{}".format(txt.col.fg.strg.grey,txt.sty.reset))
            valid = False
            leave = False
            while not leave:
                valid = True
                leave = True
                choice = input()
                if choice.lower() == "exit" or choice.lower() == "e": # deals with the exit command
                    return
                elif choice.lower() == "help" or choice.lower() == "h":
                    print("{}Sell item (type \"sell\" + the item number)".format(txt.col.fg.nml.green))
                    print("Exit inventory (type \"exit\")")
                    print("Abbreviations are \"s\", \"e\" and \"h\" for more help.{}".format(txt.sty.reset))
                    leave = False
                else:
                    choice = choice.split(" ",1) # splits the command into 2 sections: the command and the target item
                    if len(choice) == 2:
                        command = choice[0].lower()
                        target = choice[1]
                        if command != "sell":
                            valid = False
                            leave = False
                        if target.isdigit():
                            target = int(target)
                            if target < 1 or target >= inventory.activeSlotCount:
                                valid = False
                                leave = False
                        else:
                            valid = False
                            leave = False

                    else:
                        valid = False
                        leave = False
                if not valid:
                    print("{}Please enter a valid option.{}".format(txt.warning,txt.sty.reset)) # now the user input is validated

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
                print("{}Item sold!{}".format(txt.col.fg.nml.yellow,txt.sty.reset))
                input()
            else:
                print("{}The merchant refuses to take this type of item.{}".format(txt.warning,txt.sty.reset))
                input()


class Apothecary(Shop):
    def __init__(self,inv):
        self.colour = RandomColour()
        self.findMessage = self.colour + "Up ahead lies a hastily-constructed shelter. Alchemy equipment is strewn across the nearby floor." + txt.sty.reset
        self.enterMessage = self.colour + "You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you." + txt.sty.reset
        self.name = "Apothecarial Tent"
        self.tag = "apothecarySellable"
        self.wareList = self.generate_stock(inv)

class Blacksmith(Shop):
    def __init__(self,inv):
        self.colour = RandomColour()
        self.findMessage = self.colour + "You see a blacksmith in the distance." + txt.sty.reset
        self.enterMessage = self.colour + "You enter the workshop to find a young man hammering at a piece of glowing iron." + txt.sty.reset
        self.name = "Blacksmith"
        self.tag = "blacksmithSellable"
        self.wareList = self.generate_stock(inv)

class Clothier(Shop):
    def __init__(self,inv):
        self.colour = RandomColour()
        self.findMessage = self.colour +"You see a small house with a sign in front. In its windowsill are spools of sewing thread." + txt.sty.reset
        self.enterMessage = self.colour +"You enter the homely building. An old man is sitting behind the counter, sewing together a boy's shirt." + txt.sty.reset
        self.name = "Clothier's"
        self.tag = "clothierSellable"
        self.wareList = self.generate_stock(inv)