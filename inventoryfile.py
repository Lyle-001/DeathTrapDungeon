from ansi_codes import txt,icons
from validation import validate_not_empty_input
import Items
import Equipment
import Weapons

def get_items_with_tags(tags: list) -> list:
    """This function returns a list of all the items with a specific tag.

    Args:
        tags (list): A list of all the tags you want to search for

    Returns:
        A list of all the items with any of the provided tags.
    """
    items = []
    for tag in tags:
        for item in Weapons.weaponList:
            if tag in item.get_tags():
                if not item in items:
                    items.append(item)
        for item in Equipment.equipmentList:
            if tag in item.get_tags():
                if not item in items:
                    items.append(item)
        for item in Items.itemList:
            if tag in item.get_tags():
                if not item in items:
                    items.append(item)
    return items


class inventory:
    def __init__(self):
        # config stats. may be used for rebalancing later on
        self.weaponSlotCount = 2
        self.equipmentSlotCount = 5
        self.generalSlotCount = 15
        self.potionPouchSlotCount = 5
        self.quiverSize = 10

        self.hasPotionPouch = False
        self.inv = []
        self.activeSlotCount = 0

        # initialise the weapons part of the inventory
        self.inv.append([[0,"",0] for i in range(self.weaponSlotCount)])
        self.weaponsSectionFull = False
        
        # initialise the equipment part of the inventory
        self.inv.append([[0,"",0] for i in range(self.equipmentSlotCount)])

        # initialise the general part of the inventory
        self.inv.append([[0,"",0] for i in range(self.generalSlotCount)])
        self.generalFull = False

        # initialise the potions part of the inventory
        self.inv.append([[0,"",0] for i in range(self.potionPouchSlotCount)])
        self.potionPouchFull = False




    def get_inv_items_with_tags(self,tags: list) -> list:
        """ 
        Returns all the items in the inventory that have any of the given tags.

        Args:
            tags (list): The list of tags you want to search for

        Returns:
            A list of all the items in the inventory that have any of the tags
        """
        items = []
        for tag in tags:
            for section in self.inv:
                for item in section:
                    if item[1] != "":
                        if tag in item[1].get_tags() and not item[1] in items:
                            items.append(item[1])
        return items





    def print_inventory(self,hero: object): # deals with the printing of the inventory. separate procedure because its so massive
        """
        Prints the contents of the inventory. Contains all the formatting and stuff.

        Args:
            hero (hero object): Used for displaying the gold and health of the player.

        Returns:
            Nothing.
        """

        def print_item(colour,item): # function-ception. i bet you didn't know you could do this
            if item[1].maxStack == 1:
                print("\t{}{}. {}{}".format(colour,str(item[0]),txt.sty.reset,item[1].get_name()))
            else:
                print("\t{}{}. {}{}\t{}".format(colour,str(item[0]),txt.sty.reset,item[1].get_name(),str(item[2])))

        # print the player's health and gold
        print(txt.sty.reset + "\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)

        # print the inventory contents
        itemIncrement = 1

        # NEED TO MAKE THE QUANTITY VALUES ALIGN PROPERLY SOMEHOW

        # print the weapons. main colour for weapons is green
        sectColNorm = txt.col.fg.nml.green
        sectColStrong = txt.col.fg.strg.green
        print(sectColNorm + "Weapons" + txt.sty.reset)
        for item in self.inv[0]:
            if item[1] != "":
                print_item(sectColStrong,item)
            else:
                print("\t   {}Weapon{}".format(txt.col.fg.strg.grey,txt.sty.reset))

        # print the equipment. main colour for equipment is cyan
        sectColNorm = txt.col.fg.nml.cyan
        sectColStrong = txt.col.fg.strg.cyan
        print(sectColNorm + "Equipment" + txt.sty.reset)
        for index in range(len(self.inv[1])):
            item = self.inv[1][index]
            if item[1] != "":
                print_item(sectColStrong,item)
            else:
                if index == 0:
                    print("\t   {}Head{}".format(txt.col.fg.strg.grey,txt.sty.reset))
                elif index == 1:
                    print("\t   {}Torso{}".format(txt.col.fg.strg.grey,txt.sty.reset))
                elif index == 2:
                    print("\t   {}Hands{}".format(txt.col.fg.strg.grey,txt.sty.reset))
                elif index == 3:
                    print("\t   {}Legs{}".format(txt.col.fg.strg.grey,txt.sty.reset))
                else:
                    print("\t   {}Feet{}".format(txt.col.fg.strg.grey,txt.sty.reset))

        # print the general items. main colour for general items is yellow
        sectColNorm = txt.col.fg.nml.yellow
        sectColStrong = txt.col.fg.strg.yellow
        print(sectColNorm + "General Items" + txt.sty.reset)
        blankSlots = 0
        for item in self.inv[2]:
            if item[1] != "":
                print_item(sectColStrong,item)
            else:
                blankSlots += 1
        if blankSlots == 1:
            print("\t   {}With 1 slot remaining.{}".format(txt.col.fg.strg.grey,txt.sty.reset))
        elif blankSlots == self.generalSlotCount:
            print("\t   {}{} slots remaining.{}".format(txt.col.fg.strg.grey,str(blankSlots),txt.sty.reset))
        else:
            print("\t   {}With {} slots remaining.{}".format(txt.col.fg.strg.grey,str(blankSlots),txt.sty.reset))

        # print the potion pouch if the player has it. main colour for potion pouch is magenta
        sectColNorm = txt.col.fg.nml.magenta
        sectColStrong = txt.col.fg.strg.magenta
        if self.hasPotionPouch:
            print(sectColNorm + "Potion Pouch" + txt.sty.reset)
            blankSlots = 0
            for item in self.inv[3]:
                if item[1] != "":
                    print_item(sectColStrong,item)
                else:
                    blankSlots += 1
            if blankSlots == 1:
                print("\t   {}With 1 slot remaining.{}".format(txt.col.fg.strg.grey,txt.sty.reset))
            elif blankSlots == self.potionPouchSlotCount:
                print("\t   {}{} slots remaining.{}".format(txt.col.fg.strg.grey,str(blankSlots),txt.sty.reset))
            else:
                print("\t   {}With {} slots remaining.{}".format(txt.col.fg.strg.grey,str(blankSlots),txt.sty.reset))
        else:
            print(sectColNorm + "\nYou do not have a potion pouch. You might be able to find one at a clothier's.\n" + txt.sty.reset)





    def access_inventory(self,hero: object): # this is called when the user types "inventory". the backbone of the inventory
        """
        Called when the player enters their inventory.

        Args:
            hero (hero object): Used for displaying the player's health and gold, and for the ability to use items.

        Returns:
            Nothing.
        """
        self.print_inventory(hero)
        while True:
            # give options
            print("\nWhat would you like to do?")
            print("Inspect item (\"inspect\" + item number)")
            print("Use item (\"use\" + item number)")
            print("Exit (\"exit\")")
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
                    if command != "inspect" and command != "use":
                        valid = False
                    if target.isdigit():
                        target = int(target)
                        if target < 1 or target >= self.activeSlotCount:
                            valid = False
                    else:
                        valid = False

                else:
                    valid = False
                if not valid:
                    print("Please enter a valid option.") # now the user input is validated

            # find the referenced item
            itemFound = False
            for section in self.inv:
                for item in section:
                    if item[0] == target:
                        target = item[1]
                        itemFound = True
                        break
                if itemFound:
                    break

            # actually run the commands
            if command == "inspect":
                try:
                    print(target.inspect())
                except:
                    print("You cannot inspect this item.")
            elif command == "use":
                try:
                    target.use(hero,self)
                    if hero.get_hp() <= 0:
                        return
                    self.print_inventory(hero)
                except:
                    print("You cannot use this item.")




    def update_numbering(self): # update the numbering of the items in the inventory
        """ 
        Updates the item numbering for when the user picks an item to interact with.

        Args:
            None

        Returns:
            Nothing.
        """
        itemAddress = 0
        for sectionIndex in range(len(self.inv)):
            for itemIndex in range(len(self.inv[sectionIndex])):
                if self.inv[sectionIndex][itemIndex][1] != "":
                    itemAddress += 1
                    self.inv[sectionIndex][itemIndex][0] = itemAddress
                else:
                    self.inv[sectionIndex][itemIndex][0] = 0
        self.activeSlotCount = itemAddress + 1




    def add_item(self,itemID: object,section: str = "general",count: int = 1) -> bool: # add an item to a specified section of the inventory
        """
        Add an item to the inventory.

        Args:
            itemID (object): The actual item you want to add
            section (str, default is "general"): Can be either "weapons", "equipment, "general" or "potions" to specify the section of the inventory
            count (int, default is 1): How many of the object you want to add

        Returns:
            bool: Whether it was added successfully or not
        """
        if section == "weapons":
            section = 0
        elif section == "equipment":

            # Equip equipment. This works differently to the rest of the equipping that's why its here.
            section = 1
            itemTags = itemID.get_tags() # this is me when i save cpu time at the expense of memory usage
            # find what slot to put the item in
            if "head" in itemTags:
                slot = 0
            elif "torso" in itemTags:
                slot = 1
            elif "hands" in itemTags:
                slot = 2
            elif "legs" in itemTags:
                slot = 3
            elif "feet" in itemTags:
                slot = 4
            else:
                # if there is no slot to put the item in
                print("You are trying to equip a non-equipment item!")
                return False

            # if the slot it should go in is empty
            if self.inv[section][slot][1] == "":
                self.inv[section][slot][1] = itemID
                self.inv[section][slot][2] = count
                self.update_numbering()
                return True
            # if this slot already has an armour piece in
            else:
                print("You have donned an alternative already. Would you like to replace this?")
                print("\tY) Yes\n\tN) No")
                choice = validate_not_empty_input()
                if choice[0].lower() == "y":
                    # swap them, putting the old piece in the general inventory
                    cachedItem = self.inv[section][slot][:]
                    self.inv[section][slot][1] = itemID
                    self.inv[section][slot][2] = count
                    self.add_item("general",cachedItem[1],cachedItem[2])
                    return True
                else:
                    return False
            
        elif section == "general":
            section = 2
        elif section == "potions":
            section = 3
        else:
            print("Invalid section when trying to add item. Please choose from \"weapons\", \"equipment\", \"general\" or \"potions\" LUCA.") # only luca would make this mistake
            return False

        for itemIndex in range(len(self.inv[section])): # check if the item can go in a stack
            if self.inv[section][itemIndex][1] != "":
                if self.inv[section][itemIndex][1].get_name() == itemID.get_name() and self.inv[section][itemIndex][2] < itemID.maxStack: # if an item is found to stack it with
                    self.inv[section][itemIndex][2] += count
                    return True
        for itemIndex in range(len(self.inv[section])): # place the item in a blank spot
            if self.inv[section][itemIndex][1] == "":
                self.inv[section][itemIndex] = [0,itemID,count]
                self.update_numbering()
                return True
        return False





    def delete_item(self,itemID: object,count: int = 1,startingSection: str ="weapons") -> bool: # Removes a specified object from the inventory
        """
        Delete an item from the inventory.

        Args:
            itemID (object): The item you want to delete
            count (int, default is 1): How many of the object you want to delete
            startingSection (str, default is "weapons"): What section you want to start the search for the item in.

        Returns:
            bool: Whether the item was successfully deleted or not.
        """
        if startingSection == "weapons":
            startingSection = 0
        elif startingSection == "equipment":
            startingSection = 1
        elif startingSection == "general":
            startingSection = 2
        elif startingSection == "potions":
            startingSection = 3
        else:
            print("Invalid section when trying to add item. Please choose from \"weapons\", \"equipment\", \"general\" or \"potions\" LUCA.") # only luca would make this mistake
            return False

        for section in range(startingSection,len(self.inv)):
            for itemIndex in range(len(self.inv[section])):
                item = self.inv[section][itemIndex]
                if item[1] != "":
                    if item[1] == itemID:
                        self.inv[section][itemIndex][2] -= count
                        if self.inv[section][itemIndex][2] == 0:
                            self.inv[section][itemIndex][1] = ""
                        self.update_numbering()
                        return True
        
        print("You are trying to throw away an item which you do not have!")
        return False




    def update_potion_pouch(self): # Moves any potions from the general inventory to the potion pouch
        """
        Update the contents of the potion pouch. Moves any potions from the general inventory to the potion pouch

        Args:
            None

        Returns:
            Nothing.
        """
        if self.hasPotionPouch:
            for itemIndex in range(len(self.inv[2])):
                item = self.inv[2][itemIndex]
                if item[1] != "":
                    if "potion" in item[1].get_tags(): # if theres a potion in the general part
                        cachedItem = item[:]
                        self.delete_item(item[1],item[2]) # delete it from the general part
                        self.add_item("potions",cachedItem[1],cachedItem[2]) # add it to the pouch





    def switch_active_weapon(self,weaponID):
        for i in range(0,self.weaponSlotCount,1):
            if self.weaponsSection[i] == weaponID:
                return True,self.weaponsSection[i]
        print("You are not in possession of such a weapon.")
        return False