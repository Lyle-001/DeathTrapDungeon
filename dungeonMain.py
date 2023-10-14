# feel trapped to keep this comment!!!

from Monster import Monster, Goblin, Vampire, Slime, RogueWarrior
from Heroes import Hero, Barbarian, Wizard, Warlock
from ansi_codes import txt, get_list_of_colours_bg, get_list_of_colours_fg, get_list_of_formats,icons
from merchant import shop
import Weapons

import random
import math

############################### Subroutines ##################################
def validate_not_empty_input(message=""):#asks until non empty input entered
    while True:
        answer = input(message)
        if answer != "":
            return answer

def validate_int_input(message=""):
    while True:
        try:
            answer = int(input(message))
            return answer
        except:
            print("{}Please choose a numeral.{}".format(txt.col.fg.strg.red,txt.sty.reset))

def validate_int_input_with_bounds(lowbound,upperbound,message=""):#upper bound is exclusive lower bound inclusive
    while True:
        try:
            answer = int(input(message))
            if answer >= lowbound and answer < upperbound:
                return answer
        except:
            print("{}Please choose a valid number.{}".format(txt.col.fg.strg.red,txt.sty.reset))

def RandomColour(): # Choose random colour for monster.
    ColourList = ["green","yellow","red","purple","black"]
    Colour = ColourList[random.randint(0,len(ColourList)-1)]
    return Colour

# Run one fight until either hero or monster is dead
def Combat(myHero, myWeapon, myMonster ):
    while myHero.get_hp() > 0 and myMonster.get_hitPoints() > 0: #Fight continues until either combatant dies.
        print("\n######### Hero: " + str(myHero.get_hp()) + " " + heart + " #########" +
              " " + myMonster.get_species().capitalize() + ": " + str(myMonster.get_hitPoints()) + " " + heart + " #########\n")
        input("Press enter to attack!")
        heroDamage = math.floor(math.sqrt((myWeapon.attack() * myHero.attack())))
        myMonster.receive_damage(heroDamage) # Assign damage to monster
        if myMonster.get_hitPoints() > 0: # Monster only attacks if it's  still alive.
            print("The " + myMonster.get_species() + " attacks...")
            input("Press enter to defend!")
            myHero.receiveDamage(myMonster.attack()) # Subtract damage from hero

def name_and_format():#asks the user what they want their name to be and look like

    name = validate_not_empty_input("\n{}What is your name, mighty warrior?\n".format(txt.col.fg.nml.cyan))
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

    print("\nWhat style do you want your name to be in?\n1. Normal\n2.Bold\n3.Underlined\n4.Both")
    format = validate_int_input_with_bounds(1,5)

    name = "{}{}{}".format(get_list_of_formats()[format-1],get_list_of_colours_bg()[bgstrength-1][bgcolour-1],get_list_of_colours_fg()[fgstrength-1][fgcolour-1]) + name + "{}".format(txt.sty.reset)
    return name #already includes all the formating

################################# Main Code ####################################
debug = True
 
heart = "{}♡{}".format(txt.col.fg.nml.red,txt.sty.reset)
globals = heart

print("{}{}############# Welcome to Death Trap Dungeon! ############{}\n".format(txt.col.fg.strg.blue,txt.sty.bold,txt.sty.reset))
detailsConfirmed = False
while not detailsConfirmed:

    name = name_and_format()

    valid = False
    while not valid:
        print("{}What manner of warrior are you?".format(txt.col.fg.nml.blue))
        print("\t1)Barbarian\t("  + heart + "{} 20-30 | ⚔ 0-8)".format(txt.col.fg.nml.blue))
        print("\t2)Wizard\t("  + heart + "{} 15-25 | ⚔ 0-12)".format(txt.col.fg.nml.blue))
        print("\t3)Warlock\t("  + heart + "{} 17-27 | ⚔ 0-10)".format(txt.col.fg.nml.blue))
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
        print("\ty) Yes\n\tn) No")
        if input().lower() == "y":
            print("What would you enjoy your health to be?")
            theHero.set_max_health(validate_int_input("Health: "))

    valid = False
    while not valid:
        print("What weapon is of your choosing?")
        print("\t1) Sword\t(⚔ 0-6 | ⚄ 90%)")
        print("\t2) Axe\t\t(⚔ 0-8 | ⚄ 70%)")
        print("\t3) Dagger\t(⚔ 0-5 | ⚄ 100%)")
        print("\t4) Scimitar\t(⚔ 0-6 | ⚄ 90%)")
        print("\t5) Mace\t\t(⚔ 0-6 | ⚄ 90%)")
        print("\t6) Hammer\t(⚔ 0-9 | ⚄ 60%)")
        if debug:
            print("#### DEBUG ####")
            print("\t1000) AxeOfFlames\t(⚔ 0-8 | ⚄ 80%)")
            print("\t1001) SwordOfSouls\t(⚔ 0-10 | ⚄ 95%)")
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

    print("\nAre you, sir, happy with these details?")
    print("\tName: " + theHero.get_name())
    print("\tClass: " + theHero.get_class())
    print("\tWeapon: " + weapon.get_name().capitalize())
    print("Y) Yes\nN) No")
    choice = input()
    if choice.lower()[0] == "y":
        detailsConfirmed = True
    else:
        print("Through the power of a mystical force you are sent back in time.")


weapon.randomise_modifier()
if debug:
        print("#### DEBUG #### Dost thou want to set thy own modifier?")
        print("\ty) Yes\n\tn) No")
        if input().lower() == "y":
            valid = False
            while not valid:
                print("What would you enjoy your modifier to be?")
                valid = weapon.set_modifier(input("Modifier: "))
print("You pick up a " + weapon.get_name())
weapon.inspect()


print()
victories = 0
while victories < 10 and theHero.get_hp() > 0: # Run until the hero wins three matches or dies/
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
    print("You are attacked by a " + theMonster.get_colour() + " "
          + theMonster.get_species() + ".")
    theMonster.talk()
    Combat(theHero, weapon, theMonster)
    if theHero.get_hp() > 0: # Check if the hero has won or lost
        gold = theMonster.getGold()
        print("The monster dropped " + str(gold) + " gold coins.")
        theHero.set_gold(gold)
        victories += 1
        anyKey = input("You are victorious! Press enter to descend deeper into the dungeon...\n ")
        print("You have " + str(theHero.gold) + " ¤.\n")
        # Give user option of visiting the dungeon shop if they have another fight next
        if victories < 10:
            purchase = input("\nUp ahead lies a hastily-constructed shelter. Do you wish to enter the Merchant's Tent? Y/N ").upper()
            if purchase == "Y":
                shop(theHero)
    else:
        print(theHero.get_name() + ", you are dead. Death Trap Dungeon claims another victim.")
if victories == 10: # Check if hero won the game
    print(theHero.get_name() + ", you are the Champion of Champions! Fame and fortune are yours!")
    print("You leave the dungeon with " + str(theHero.get_gold()) + " ¤!")
print("######## GAME OVER ########")



# -penis2