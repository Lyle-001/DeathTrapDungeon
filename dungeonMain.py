# feel trapped to keep this comment!!!

from Monster import Monster, Goblin, Vampire, Slime, RogueWarrior
from Heroes import Hero, Barbarian, Wizard, Warlock
from ansi_codes import txt
import Weapons

import random
import math

############################### Subroutines ##################################
def validate_int_input(message=""):
    while True:
        try:
            answer = int(input(message))
            return answer
        except:
            print("{}Please choose a numeral.{}".format(txt.col.fg.strg.red,txt.sty.reset))


def RandomColour(): # Choose random colour for monster.
    ColourList = ["green","yellow","red","purple","black"]
    Colour = ColourList[random.randint(0,len(ColourList)-1)]
    return Colour

# Run one fight until either hero or monster is dead
def Combat(myHero, myWeapon, myMonster ):
    while myHero.getCurrentHPs() > 0 and myMonster.get_hitPoints() > 0: #Fight continues until either combatant dies.
        print("\n######### Hero: " + str(myHero.getCurrentHPs()) + " ♡ #########" +
              " " + myMonster.get_species().capitalize() + ": " + str(myMonster.get_hitPoints()) + " ♡ #########\n")
        anyKey = input("Press enter to attack!")
        heroDamage = math.floor(math.sqrt((myWeapon.attack() * myHero.attack())))
        myMonster.receive_damage(heroDamage) # Assign damage to monster
        if myMonster.get_hitPoints() > 0: # Monster only attacks if it's  still alive.
            print("The " + myMonster.get_species() + " attacks...")
            anyKey = input("Press enter to defend!")
            myHero.receiveDamage(myMonster.attack()) # Subtract damage from hero

# Lets the hero buy items providing they have enough gold.
def shop(myHero):
    cont = "Y"
    while cont == "Y":
        output = "\n############## Welcome to Ye Olde Dungeon Shoppe! ##########\n"
        output += "1) Buy basic health potion (+2-8 ♡)\t\t 2¤\n"
        output += "2) Buy standard health potion (+4-12 ♡)\t\t 4¤\n"
        output += "3) Buy Axe of Fire (⚔ 0-8 | ⚄ 80%)\t\t 8¤\n"
        output += "4) Buy Sword of Souls (⚔ 0-10 | ⚄ 95%)\t\t12¤\n"
        output += "5) Exit shoppe\n"
        output += "Your current gold: " + str(myHero.getGold()) + "\n"
        output += "Select option: "
        choice = input(output)
        if choice == "1":
            healthPotion = random.randint(2,8)
            if myHero.purchase(2) == True: # Check if hero has enough gold
                print("\nYou swig a health potion. You recover " + str(healthPotion) + " HPs.")
                myHero.heal(healthPotion)
            else:
                print("\nYou do not have enough gold.")
        elif choice == "2":
            healthPotion = random.randint(4,12)
            if myHero.purchase(4) == True: # Check if hero has enough gold
                print("\nYou swig a health potion. You recover " + str(healthPotion) + " HPs.")
                myHero.heal(healthPotion)
            else:
                print("\nYou do not have enough gold.")
        elif choice == "3":
            if myHero.purchase(8) == True: # Check if hero has enough gold
                weapon = Weapons.AxeOfFlames()
                weapon.randomise_modifier()
                print("You pick up a " + weapon.get_name())
                weapon.inspect()
            else:
                print("\nYou do not have enough gold.")
        elif choice == "4":
            if myHero.purchase(12) == True: # Check if hero has enough gold
                weapon = Weapons.SwordOfSouls()
                weapon.randomise_modifier()
                print("You pick up a " + weapon.get_name())
                weapon.inspect()
            else:
                print("\nYou do not have enough gold.")
        elif choice == "5":
            return
        cont = input("\nDo you want to make another purchase? Y/N ").upper()

################################# Main Code ####################################
debug = True
        



print("{}{}############# Welcome to Death Trap Dungeon! ############{}\n".format(txt.col.fg.strg.white,txt.sty.bold,txt.sty.reset))
detailsConfirmed = False
while not detailsConfirmed:

    name = input("\nWhat is your name, mighty warrior?\n")

    valid = False
    while not valid:
        print("What manner of warrior are you?")
        print("\t1)Barbarian\t(♡ 20-30 | ⚔ 0-8)")
        print("\t2)Wizard\t(♡ 15-25 | ⚔ 0-12)")
        print("\t3)Warlock\t(♡ 17-27 | ⚔ 0-10)")
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
while victories < 10 and theHero.getCurrentHPs() > 0: # Run until the hero wins three matches or dies/
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
    if theHero.getCurrentHPs() > 0: # Check if the hero has won or lost
        gold = theMonster.getGold()
        print("The monster dropped " + str(gold) + " gold coins.")
        theHero.setGold(gold)
        victories += 1
        anyKey = input("You are victorious! Press enter for the next attack!\n ")
        print("Gold coins: " + str(theHero.gold) + "\n")
        # Give user option of visiting the dungeon shop if they have another fight next
        if victories < 10:
            purchase = input("\nDo you want to visit Ye Olde Dungeon Shoppe? Y/N ").upper()
            if purchase == "Y":
                shop(theHero)
    else:
        print(theHero.get_name() + ", you are dead. Death Trap Dungeon claims another victim.")
if victories == 10: # Check if hero won the game
    print(theHero.get_name() + ", you are the Champion of Champions! Fame and fortune are yours!")
    print("You leave the dungeon with " + str(theHero.getGold()) + " gold coins!")
print("######## GAME OVER ########")



# -penis2