from sys import getswitchinterval
from ansi_codes import txt
from validation import validate_int_input_with_bounds
import Items

class inventory:
    def __init__(self,isDebug):
        # config stats. may be used for rebalancing later on
        self.weaponSlots = 2
        self.equipmentSlots = 5
        self.quiverSize = 10
        self.generalSlots = 15
        self.hasPotionPouch = False
        self.potionPouchSlots = 5
        self.potionPouchCurrentSlots = 0
        
        # :smile:
        if isDebug:
            self.isDebug = True
        else:
            self.isDebug = False

        # initialise the weapons part of the inventory
        self.weapons = []
        for i in range(0,self.weaponSlots,1):
            slot = ["",0]
            self.weapons.append(slot)
        self.weaponsFull = False
        
        # initialise the equipment part of the inventory
        self.equipment = []
        for i in range(0,self.equipmentSlots,1):
            slot = ["",0]
            self.equipment.append(slot)

        # initialise the general part of the inventory
        self.general = []
        for i in range(0,self.generalSlots,1):
            slot = ["",0]
            self.general.append(slot)
        self.generalFull = False

        # initialise the potions part of the inventory
        self.potionPouch = []
        for i in range(0,self.potionPouchSlots,1):
            slot = ["",0]
            self.potionPouch.append(slot)
        self.potionPouchFull = False




    def access_inventory(self,hero):
        itemIncrement = 1 # used for the numbering of the items

        # print the weapons part of the inventory
        print("Weapons")
        emptySlots = 0
        for item in self.weapons:
            if item[0] != "":
                print("\t" + str(itemIncrement) + ". " + item[0].get_name() + txt.sty.reset + "\t" + str(item[1]))
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.weaponSlots:
            print("\t" + str(self.weaponSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slots.")

        # print the equipment part of the inventory
        print("Equipment")
        emptySlots = 0
        for item in self.equipment:
            if item[0] != "":
                print("\t" + str(itemIncrement) + ". " + item[0].name + txt.sty.reset + "\t" + str(item[1]))
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.equipmentSlots:
            print("\t" + str(self.equipmentSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slots.")

        # print the general part of the inventory
        print("General Slots")
        emptySlots = 0
        for item in self.general:
            if item[0] != "":
                print("\t" + str(itemIncrement) + ". " + item[0].name + txt.sty.reset + "\t" + str(item[1]))
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.generalSlots:
            print("\t" + str(self.generalSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slots.")

        # print the potions part of the inventory
        if self.hasPotionPouch:
            print("Potion Pouch")
            emptySlots = 0
            for item in self.potionPouch:
                if item[0] != "":
                    print("\t" + str(itemIncrement) + ". " + item[0].get_name() + txt.sty.reset + "\t" + str(item[1]))
                    itemIncrement += 1
                else:
                    emptySlots += 1
            if emptySlots == self.potionPouchCurrentSlots:
                print("\t" + str(self.potionPouchCurrentSlots) + " empty slots.")
            elif emptySlots != 0:
                if emptySlots == 1:
                    print("\tWith " + str(emptySlots) + " more empty slot.")
                else:
                    print("\tWith " + str(emptySlots) + " more empty slots.")
        else:
            print("You do not have a potion pouch. You might be able to find one at a clothier.")


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
                    if target < 1 or target >= itemIncrement:
                        valid = False
                else:
                    valid = False

            else:
                valid = False
            if not valid:
                print("Please enter a valid option.") # now the user input is validated


        itemFound = False # Find the item the user is referencing
        nonBlanks = 0
        for item in self.weapons:
            if item[0] != "":
                nonBlanks += 1
            if nonBlanks == target:
                target = item[0]
                itemFound = True
        if not itemFound:
            for item in self.equipment:
                if item[0] != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item[0]
                    itemFound = True
        if not itemFound:
            for item in self.general:
                if item[0] != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item[0]
                    itemFound = True
        if not itemFound:
            for item in self.potionPouch:
                if item[0] != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item[0]
                    itemFound = True


        # actually run the commands
        if command == "inspect":
            try:
                print(target.inspect())
            except:
                print("You cannot inspect this item.")
        elif command == "use":
            try:
                target.use(hero,self)
            except:
                print("You cannot use this item.")




    def get_weapons(self):
        return self.weapons

    def add_weapon(self,weaponID):
        for i in range(0,self.weaponSlots,1):
            if self.weapons[i][0] == "":
                if i + 1 == self.weaponSlots:
                    self.weaponsFull = True
                self.weapons[i] = weaponID
                return True
        self.weaponsFull = True
        print("Weapon slots full. Consider removing some old weapons.")
        return False

    def remove_weapon(self,weaponID):
        for i in range(0,self.weaponSlots,1):
            if self.weapons[i] == weaponID:
                self.weapons[i][0] = ""
                return True
        print("You are not in possession of such a weapon.")
        return False

    def switch_active_weapon(self,weaponID):
        for i in range(0,self.weaponSlots,1):
            if self.weapons[i] == weaponID:
                return True,self.weapons[i]
        print("You are not in possession of such a weapon.")
        return False




    def get_equipment(self):
        return self.equipment
    
    def swap_equipment(self,equipmentID):
        slot = equipmentID[0].get_equipment_type()
        if slot == "head":
            slot = 0
        elif slot == "torso":
            slot = 1
        elif slot == "hands":
            slot = 2
        elif slot == "legs":
            slot = 3
        elif slot == "feet":
            slot = 4
        else:
            print("equipment type not recognised.")
            return False

        if self.equipment[slot][0] == "":
            self.equipment[slot] = equipmentID
            print("Equipment equipped.")
            return True
        else:
            print("You have donned an alternative already. Would you like to replace this?")
            print("\t1) Yes\n\t2) No")
            choice = validate_int_input_with_bounds(1,3)
            if choice == 1:
                temp = self.equipment[slot]
                self.equipment[slot] = equipmentID
                self.add_general_item(temp)
                return True
            else:
                return False




    def get_general_slots(self):
        return self.general

    def add_general_item(self,itemID):
        for i in range(0,self.generalSlots,1):
            if self.general[i][0] != "" and itemID[0].get_type != "weapon" and itemID[0].get_type != "equipment":
                if self.general[i][0].name == itemID[0].name:
                    if self.general[i][0].maxStack > self.general[i][1]:
                        self.general[i][1] += itemID[1]
                        return True
        for i in range(0,self.generalSlots,1):
            if self.general[i][0] == "":
                if i + 1 == self.generalSlots:
                    self.generalFull = True
                self.general[i] = itemID
                return True
        self.generalFull = True
        print("You do not have space on your person for this item.")
        return False

    def destroy_general_item(self,itemID):
        for i in range(0,self.generalSlots,1):
            if self.general[i][0] != "":
                if self.general[i][0] == itemID[0]:
                    self.general[i][1] -= itemID[1]
                    if self.general[i][1] == 0:
                        self.generalFull = False
                        self.general[i][0] = ""
                    return True
        print("You are trying to throw away an item which you do not have!")
        return False




    def get_potion_pouch(self):
        if self.hasPotionPouch:
            return self.potionPouch
        else:
            return False

    def add_potion(self,itemID):
        for i in range(0,self.potionPouchSlots,1):
            if self.potionPouch[i][0] == "":
                if i + 1 == self.potionPouchSlots:
                    self.potionPouchFull = True
                self.potionPouch[i] = itemID
                return True
        print("You do not have space on your person for this potion.")
        return False

    def destroy_potion(self,itemID):
        for i in range(0,self.potionPouchSlots,1):
            if self.potionPouch[i][0] != "":
                if self.potionPouch[i][0] == itemID:
                    self.potionPouch[i][1] -= itemID[1]
                    if self.potionPouch[i][1] == 0:
                        self.potionPouchFull = False
                        self.potionPouch[i][0] = ""
                    return True
        print("You are trying to throw away an item which you do not have!")
        return False


    def update_potion_pouch(self):
        if not self.potionPouchFull:
            for item in self.general:
                if item[0] != "":
                    if item[0].get_type() == "potion": # potion in general slot found
                        self.add_potion(item)
                        self.destroy_general_item(item)