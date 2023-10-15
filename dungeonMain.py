# feel trapped to keep this comment!!!

from Monster import Monster, Goblin, Vampire, Slime, RogueWarrior
from Heroes import Hero, Barbarian, Wizard, Warlock
from ansi_codes import txt, get_list_of_colours_bg, get_list_of_colours_fg, get_list_of_formats,icons
from merchant import shop
from validation import validate_int_input,validate_int_input_with_bounds,validate_not_empty_input

import Weapons
import Inventory

import random
import math

############################### Subroutines ##################################

def RandomColour(): # Choose random colour for monster.
    ColourList = ["black","red","green","yellow","blue","magenta","cyan","white"]
    Colour = ColourList[random.randint(0,len(ColourList)-1)]
    return Colour

# Run one fight until either hero or monster is dead
def Combat(myHero, myWeapon, myMonster ):
    while myHero.get_hp() > 0 and myMonster.get_hitPoints() > 0: #Fight continues until either combatant dies.
        print("\n######### " + name + ": " + str(myHero.get_hp()) + " " + icons.heart + " #########" +
              " " + myMonster.get_species().capitalize() + ": " + str(myMonster.get_hitPoints()) + " " + icons.heart + " #########\n")
        input("{}Press enter to attack!\n{}".format(txt.col.fg.nml.white,txt.sty.reset))
        heroDamage = math.floor(math.sqrt((myWeapon.attack() * myHero.attack())))
        myMonster.receive_damage(heroDamage) # Assign damage to monster
        if myMonster.get_hitPoints() > 0: # Monster only attacks if it's  still alive.
            print("The " + myMonster.get_species() + " attacks...")
            input("{}Press enter to defend!{}\n".format(txt.col.fg.nml.white,txt.sty.reset))
            myHero.receiveDamage(myMonster.attack()) # Subtract damage from hero

def name_and_format():#asks the user what they want their name to be and look like

    name = validate_not_empty_input("\n{}What is your name, mighty warrior?\n".format(txt.col.fg.nml.white))
    print("\nWhat colour do you want your name to be?\n")
    print("1. Black\n2. Red\n3. Green\n4. Yellow\n5. Blue\n6. Magenta\n7. Cyan\n8. White")
    fgcolour = validate_int_input_with_bounds(1,9) 
    print("\nDo you want the colour to be strong or normal?\n1. Strong\n2. Normal")
    fgstrength = validate_int_input_with_bounds(1,3)

    print("\nWhat colour do you want the background of your name to be?\n")
    print("1. Black\n2. Red\n3. Green\n4. Yellow\n5. Blue\n6. Magenta\n7. Cyan\n8. White")
    bgcolour = validate_int_input_with_bounds(1,9) 
    print("\nDo you want the colour to be strong or normal?\n1. Strong\n2. Normal")
    bgstrength = validate_int_input_with_bounds(1,3)

    print("\nWhat style do you want your name to be in?\n1. Normal\n2. Bold\n3. Underlined\n4. Both")
    format = validate_int_input_with_bounds(1,5)

    name = "{}{}{}".format(get_list_of_formats()[format-1],get_list_of_colours_bg()[bgstrength-1][bgcolour-1],get_list_of_colours_fg()[fgstrength-1][fgcolour-1]) + name + "{}".format(txt.sty.reset)
    return name #already includes all the formating

################################# Main Code ####################################

debuganswer = input("\nDebug?(true or false) ")
if debuganswer.lower() == "true":
    debug = True
    print("debug set to true")
else:
    debug = False
    print("debug set to false")

print("{}{}############# Welcome to Death Trap Dungeon! ############{}\n".format(txt.col.fg.strg.blue,txt.sty.bold,txt.sty.reset))
inv = Inventory.inventory()
detailsConfirmed = False
while not detailsConfirmed:

    name = name_and_format()

    valid = False
    while not valid:
        print("{}\nWhat manner of warrior are you?".format(txt.col.fg.nml.yellow))
        print("\t1)Barbarian\t({}{} 20-30 | {}{} 0-8)".format(icons.heart,txt.col.fg.nml.yellow,icons.damage,txt.col.fg.nml.yellow))
        print("\t2)Wizard\t({}{} 15-25 | {}{} 0-12)".format(icons.heart,txt.col.fg.nml.yellow,icons.damage,txt.col.fg.nml.yellow))
        print("\t3)Warlock\t({}{} 17-27 | {}{} 0-10)".format(icons.heart,txt.col.fg.nml.yellow,icons.damage,txt.col.fg.nml.yellow))
        choice = validate_int_input()
        valid = True
        if choice == 1:
            theHero = Barbarian(name)
        elif choice == 2:
            theHero = Wizard(name)
        elif choice == 3:
            theHero = Warlock(name)
        else:
            valid = False
            print("{}I suggest you look again for training.{}".format(txt.col.fg.strg.red,txt.sty.reset))
    if debug:
        print("#### DEBUG #### Wouldst thou like to set thy own health?")
        print("\tY) Yes\n\tN) No")
        if input().lower() == "y":
            print("What would you enjoy your health to be?")
            theHero.set_max_health(validate_int_input("Health: "))

    valid = False
    while not valid:
        print("{}What weapon is of your choosing?".format(txt.col.fg.nml.green))
        print("\t1) Sword\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t2) Axe\t\t({} {}0-8 | {} {}70%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t3) Dagger\t({} {}0-5 | {} {}100%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t4) Scimitar\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t5) Mace\t\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t6) Hammer\t({} {}0-9 | {} {}60%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        if debug:
            print("#### DEBUG ####")
            print("\t1000) AxeOfFlames\t({}{} 0-8 | {}{} 80%)".format(icons.damage,txt.col.fg.nml.blue,icons.hitchance,txt.col.fg.nml.blue))
            print("\t1001) SwordOfSouls\t({}{} 0-10 | {}{} 95%)".format(icons.damage,txt.col.fg.nml.blue,icons.hitchance,txt.col.fg.nml.blue))
        choice = validate_int_input()
        valid = True
        if choice == 1:
            weapon = Weapons.ClassicSword()
        elif choice == 2:
            weapon = Weapons.Axe()
        elif choice == 3:
            weapon = Weapons.Dagger()
        elif choice == 4:
            weapon = Weapons.Scimitar()
        elif choice == 5:
            weapon = Weapons.Mace()
        elif choice == 6:
            weapon = Weapons.Hammer()
        elif debug:
            if choice == 1000:
                weapon = Weapons.AxeOfFlames()
            elif choice == 1001:
                weapon = Weapons.SwordOfSouls()
            else:
                valid = False
                print("{}You have the ability to look into other planes and yet you still can't choose a weapon.{}".format(txt.col.fg.strg.red,txt.sty.reset))
        else:
            valid = False
            print("{}I suggest you ask for a weapon that exists in this plane.{}".format(txt.col.fg.strg.red,txt.sty.reset))

    print("\n{}Are you, sir, happy with these details?{}".format(txt.warning,txt.sty.reset))
    print("\n\tName: " + theHero.get_name())
    print("\tClass: {}{}{}".format(txt.col.fg.nml.yellow,theHero.get_class(),txt.sty.reset))
    print("\tWeapon: {}{}{}".format(txt.col.fg.nml.green,weapon.get_name().capitalize(),txt.sty.reset))
    print("Y) Yes\nN) No")
    choice = input()
    if choice.lower() == "y":
        detailsConfirmed = True
    else:
        print("{}Through the power of a mystical force you are sent back in time.{}".format(txt.col.fg.strg.magenta,txt.sty.reset))

weapon.randomise_modifier()
if debug:
        print("#### DEBUG #### Dost thou want to set thy own modifier?")
        print("\tY) Yes\n\tN) No")
        if input().lower() == "y":
            valid = False
            while not valid:
                print("What would you enjoy your modifier to be?")
                valid = weapon.set_modifier(input("Modifier: "))
print("You pick up a " + weapon.get_name())
weapon.inspect()
inv.add_weapon(weapon)

print()
victories = 0
while victories < 10 and theHero.get_hp() > 0: # Run until the hero wins ten matches or dies
    monsterChoice = random.randint(0,4)
    if monsterChoice == 0:
        theMonster = Monster(RandomColour())
    elif monsterChoice == 1:
        theMonster = Goblin(RandomColour())
    elif monsterChoice == 2:
        theMonster = Vampire(RandomColour())
    elif monsterChoice == 3:
        theMonster = Slime(RandomColour())
    else:
        theMonster = RogueWarrior(RandomColour())
    print("You are attacked by a {}".format(theMonster.getCode()) +  theMonster.get_colour() + " "
          + theMonster.get_species() + ".{}".format(txt.sty.reset))
    theMonster.talk()
    Combat(theHero, weapon, theMonster)
    if theHero.get_hp() > 0: # Check if the hero has won or lost
        gold = theMonster.getGold()
        print("The monster dropped " + str(gold) + " gold coins.")
        theHero.set_gold(gold)
        victories += 1
        anyKey = input("You are victorious! Press enter to descend deeper into the dungeon...\n ")
        print("You have " + str(theHero.gold) + icons.gold + ".\n")
        # Give user option of visiting the dungeon shop if they have another fight next
        if victories < 10:
            purchase = input("\nUp ahead lies a hastily-constructed shelter. Do you wish to enter the Merchant's Tent? Y/N ").upper()
            if purchase == "Y":
                shop(theHero)
        # Give user option of accessing inventory
        accessingInv = True
        while accessingInv:
            print("You have the option to sit and rest. Would you like to: \n\tAccess Inventory (type inventory) \n\tContinue Journey (type continue)")
            valid = False
            while not valid:
                choice = input()
                if choice.lower() == "continue":
                    accessingInv = False
                    valid = True
                elif choice.lower() == "inventory":
                    valid = True
                else:
                    print("{}Please enter a valid choice.{}".format(txt.warning,txt.sty.reset))
    else:
        print(theHero.get_name() + ", you are dead. Death Trap Dungeon claims another victim.")
if victories == 10: # Check if hero won the game
    print(theHero.get_name() + ", you are the Champion of Champions! Fame and fortune are yours!")
    print("You leave the dungeon with " + str(theHero.get_gold()) + icons.gold + "!")
print("######## GAME OVER ########")



# -penis2