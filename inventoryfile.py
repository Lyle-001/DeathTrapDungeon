from ansi_codes import txt
from validation import validate_int_input_with_bounds
import Items

class inventory:
    def __init__(self):
        self.weaponSlots = 2
        self.equipmentSlots = 5
        self.quiverSize = 10
        self.generalSlots = 15
        self.hasPotionPouch = False
        self.potionPouchSlots = 5
        self.potionPouchCurrentSlots = 0

        self.weapons = []
        for i in range(0,self.weaponSlots,1):
            self.weapons.append("")
        
        self.equipment = []
        for i in range(0,self.equipmentSlots,1):
            self.equipment.append("")

        self.general = []
        for i in range(0,self.generalSlots,1):
            self.general.append("")

        self.potionPouch = []
        for i in range(0,self.potionPouchSlots,1):
            self.potionPouch.append("")




    def access_inventory(self,hero):
        itemIncrement = 1

        print("Weapons") # Weapons section
        emptySlots = 0
        for item in self.weapons:
            if item != "":
                print("\t" + str(itemIncrement) + ". " + item.get_name() + txt.sty.reset)
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.weaponSlots:
                print("\t" + str(self.weaponSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slot.")


        print("Equipment") # Equipment section
        emptySlots = 0
        for item in self.equipment:
            if item != "":
                print("\t" + str(itemIncrement) + ". " + item.get_name() + txt.sty.reset)
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.equipmentSlots:
                print("\t" + str(self.equipmentSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slot.")


        print("General Slots") # General Slots
        emptySlots = 0
        for item in self.general:
            if item != "":
                print("\t" + str(itemIncrement) + ". " + item.get_name() + txt.sty.reset)
                itemIncrement += 1
            else:
                emptySlots += 1
        if emptySlots == self.generalSlots:
                print("\t" + str(self.generalSlots) + " empty slots.")
        elif emptySlots != 0:
            if emptySlots == 1:
                print("\tWith " + str(emptySlots) + " more empty slot.")
            else:
                print("\tWith " + str(emptySlots) + " more empty slot.")


        if self.hasPotionPouch: # Potion Pouch
            print("Potion Pouch")
            emptySlots = 0
            for item in self.potionPouch:
                if item != "":
                    print("\t" + str(itemIncrement) + ". " + item.get_name() + txt.sty.reset)
                else:
                    emptySlots += 1
            if emptySlots == self.potionPouchCurrentSlots:
                print("\t" + str(self.potionPouchCurrentSlots) + " empty slots.")
                itemIncrement += 1
            elif emptySlots != 0:
                if emptySlots == 1:
                    print("\tWith " + str(emptySlots) + " more empty slot.")
                else:
                    print("\tWith " + str(emptySlots) + " more empty slot.")
        else:
            print("You do not have a potion pouch. You might be able to find one at a clothier.")


        print("\nWhat would you like to do?")
        print("Inspect item (\"inspect\" + item number)")
        print("Use item (\"use\" + item number)")
        print("Exit (\"exit\")")
        valid = False
        while not valid:
            valid = True
            choice = input()
            if choice.lower() == "exit":
                return
            choice = choice.split(" ",1) # splits on the space key once. splits the command into the keyword and the target item
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
                print("Please enter a valid option.")


        itemFound = False # Find the item the user is referencing
        nonBlanks = 0
        for item in self.weapons:
            if item != "":
                nonBlanks += 1
            if nonBlanks == target:
                target = item
                itemFound = True
        if not itemFound:
            for item in self.equipment:
                if item != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item
                    itemFound = True
        if not itemFound:
            for item in self.general:
                if item != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item
                    itemFound = True
        if not itemFound:
            for item in self.potionPouch:
                if item != "":
                    nonBlanks += 1
                if nonBlanks == target:
                    target = item
                    itemFound = True

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
            if self.weapons[i] == "":
                self.weapons[i] = weaponID
                return True
        print("Weapon slots full. Consider removing some old weapons.")
        return False

    def remove_weapon(self,weaponID):
        for i in range(0,self.weaponSlots,1):
            if self.weapons[i] == weaponID:
                self.weapons[i] = ""
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
        slot = equipmentID.get_type()
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
            print("equipmentID not recognised.")
            return False

        if self.equipment[slot] == "":
            self.equipment[slot] = equipmentID
            return True
        else:
            print("You have donned an alternative already. Would you like to replace this?")
            print("\t1) Yes\n\t2) No")
            choice = validate_int_input_with_bounds(1,3)
            if choice == 1:
                temp = self.equipment[slot]
                self.equipment[slot] = equipmentID
                return True
            else:
                return False




    def get_general_slots(self):
        return self.general

    def add_general_item(self,itemID):
        for i in range(0,self.generalSlots,1):
            if self.general[i] == "":
                self.general[i] = itemID
                return True
        print("You do not have space on your person for this item.")
        return False

    def destroy_general_item(self,itemID):
        for i in range(0,self.generalSlots,1):
            if self.general[i] != "":
                if self.general[i] == itemID:
                    self.general[i] = ""
                    return True
        print("You are trying to throw away an item which you do not have!")
        return False




    def get_potion_pouch(self):
        if self.hasPotionPouch:
            return self.potionPouch
        else:
            return False