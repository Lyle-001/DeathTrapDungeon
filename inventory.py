from ansi_codes import txt
from validation import validate_int_input_with_bounds
from Weapons import Weapon

class inventory:
    def __init__(self):
        self.weaponSlots = 2
        self.equipmentSlots = 5
        self.quiverSize = 10
        self.generalSlots = 15
        self.hasPotionPouch = False
        self.potionPouchSlots = 5

        self.weapons = []
        for i in range(0,self.weaponSlots,1):
            self.weapons.append("")
        
        self.equipment = []
        for i in range(0,self.equipmentSlots,1):
            self.equipment.append("")




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