# feel trapped to keep this comment!!! no i wont

#if you see a comment 'formatted' that means that the file has been completely formatted and is just a note that it is done 
#it will be on EVERY file, even if there is no text

from turtle import clear
from Monster import Monster, Goblin, Vampire, Slime, RogueWarrior
from Heroes import Barbarian, Wizard, Warlock
from ansi_codes import txt, get_list_of_colours_bg, get_list_of_colours_fg, get_list_of_formats,icons,clearscreen
import merchant
from validation_and_functions import validate_int_input,validate_int_input_with_bounds,validate_not_empty_input,validate_input_from_array,RandomColour
import towns

import dungeon_maze
import Weapons
import inventoryfile

import random
import math

############################### Subroutines ##################################


def RandomAdjective():
    array = ["Strong","Big","Huge","Small","Silly","Putrid","Godless"]
    intensifiers = ["Very ","Not Very ", ""]
    return intensifiers[random.randint(0,len(intensifiers)-1)] + array[random.randint(0,len(array)-1)]

def makeWeaponlist(weapon):
    string = "How do you wish to attack?\n"
    for loop in weapon.get_attacks():
        string += loop + "\n"
    return string 
        
# Run one fight until either hero or monster is dead
def Combat(myHero, myWeapon, myMonster ):
    while myHero.get_hp() > 0 and myMonster.get_hitPoints() > 0: #Fight continues until either combatant dies.
        print("\n######### " + name + ": " + str(myHero.get_hp()) + " " + icons.heart + " #########" +
              " "+ myMonster.getCode() + myMonster.get_species().capitalize() + ":{} ".format(txt.sty.reset) + str(myMonster.get_hitPoints()) + " " + icons.heart + " #########\n")
        
        choice = validate_input_from_array(weapon.get_attacks(),makeWeaponlist(myWeapon))   

        heroDamage = math.floor(math.sqrt((myWeapon.attack() * myHero.attack())))
        myMonster.receive_damage(heroDamage,choice) # Assign damage to monster
        if myMonster.get_hitPoints() > 0: # Monster only attacks if it's  still alive.
            print("The " + myMonster.getCode() + myMonster.get_species() + "{} attacks...".format(txt.sty.reset))
            input("{}Press enter to defend!{}\n".format(txt.col.fg.nml.white,txt.sty.reset))
            myHero.receiveDamage(myMonster.attack()) # Subtract damage from hero
            input()
            clearscreen()

def name_and_format():#asks the user what they want their name to be and look like

    name = validate_not_empty_input("\n{}What do you wish your name to be?\n".format(txt.col.fg.nml.white))
    
    choice = validate_not_empty_input("\n{}Do you wish for deeper customisation? \n{}Y) Yes\tN) No{}".format(txt.col.fg.nml.white,txt.col.fg.strg.grey,txt.sty.reset))
    if choice.lower()[0] == "y":
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
    else:
        return name
    
################################# Main Code ####################################

debuganswer = input("Debug? (True or False) ")
if debuganswer.lower() == "true":
    debug = True
else:
    debug = False

print("{}{}############# Welcome to Death Trap Dungeon! ############{}\n".format(txt.col.fg.strg.blue,txt.sty.bold,txt.sty.reset))
inv = inventoryfile.inventory()
townGenerator = towns.Towns()
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
        print("{}\tY) Yes\tN) No{}".format(txt.col.fg.strg.grey,txt.sty.reset))
        if input().lower() == "y":
            print("What would you enjoy your health to be?")
            theHero.set_max_health(validate_int_input("Health: "))

    print("{}What weapon is of your choosing?".format(txt.col.fg.nml.green))
    print("\t1) Sword\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    print("\t2) Axe\t\t({} {}0-8 | {} {}70%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    print("\t3) Dagger\t({} {}0-5 | {} {}100%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    print("\t4) Scimitar\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    print("\t5) Mace\t\t({} {}0-6 | {} {}90%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    print("\t6) Hammer\t({} {}0-9 | {} {}60%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
    if debug:
        print("#### DEBUG ####")
        print("\t1000) AxeOfFlames\t({}{} 0-8 | {}{} 80%)".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green))
        print("\t1001) SwordOfSouls\t({}{} 0-10 | {}{} 95%){}".format(icons.damage,txt.col.fg.nml.green,icons.hitchance,txt.col.fg.nml.green,txt.sty.reset))
    valid = False
    while not valid:    
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
    print("{}\tY) Yes\tN) No{}".format(txt.col.fg.strg.grey,txt.sty.reset))
    choice = validate_not_empty_input()
    if choice.lower()[0] == "y":
        detailsConfirmed = True
    else:
        print("{}Through the power of a mystical force you are sent back in time.{}".format(txt.col.fg.strg.magenta,txt.sty.reset))

weapon.randomise_modifier()
""" if debug:               doesnt work cause modifier names include formatting, not important rn though
    print("#### DEBUG #### Dost thou want to set thy own modifier?")
    print("\tY) Yes\n\tN) No")
    if input().lower() == "y":
        valid = False
        while not valid:
            print("What would you enjoy your modifier to be?")
            valid = weapon.set_modifier(input("Modifier: ")) """
print("You pick up a " + weapon.get_name())
weapon.inspect()
input()
inv.add_item(weapon,"weapons",1)

if debug:
    print(txt.sty.reset + "#### DEBUG #### do you want some money?")
    print("{}\tY) Yes\tN) No{}".format(txt.col.fg.strg.grey,txt.sty.reset))
    if input().lower() == "y":
        valid = False
        while not valid:
            print("how much money")
            valid = theHero.set_gold(validate_int_input("money: "))

print()
victories = 0
while victories < 10 and theHero.get_hp() > 0: # Run until the hero wins ten matches or dies
    r = RandomColour()
    a = RandomAdjective()
    monsters = [Monster(r,a),Goblin(r,a),Vampire(r,a),Slime(r,a),RogueWarrior(r,a)]
    theMonster = monsters[random.randint(0,len(monsters)-1)]
    clearscreen()
    print("You are attacked by a {}".format(theMonster.getCode()) +  theMonster.get_adj() + " "
          + theMonster.get_species() + ".{}".format(txt.sty.reset))
    theMonster.talk()
    weapon = inv.get_active_weapon()
    Combat(theHero, weapon, theMonster)
    if theHero.get_hp() > 0: # Check if the hero has won or lost
        gold = theMonster.getGold()
        print("The monster dropped {}{} gold coins.{}".format(txt.col.fg.nml.yellow,str(gold),txt.sty.reset))
        theHero.set_gold(gold)
        victories += 1
        anyKey = input("You are {}victorious!{} Press enter to descend deeper into the dungeon...\n ".format(txt.col.fg.nml.green,txt.sty.reset))
        print("You have " + str(theHero.gold) + icons.gold + ".\n")
        # Give user option of visiting the dungeon shop or accessing inventory if they have another fight next
        if victories < 10:
            townGenerator.visit_town(theHero,inv)
if victories == 10: # Check if hero won the game
    print(theHero.get_name() + ", you are the Champion of Champions! Fame and fortune are yours!")
    print("You leave the dungeon with " + str(theHero.get_gold()) + icons.gold + "!")
else:
    print(theHero.get_name() + ", you are dead. Death Trap Dungeon claims another victim.")
print("{}######## GAME OVER ########".format(txt.col.fg.strg.red))
input() # keeps the console open after the game ends



# -penis3
