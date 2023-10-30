from random import randint
import town_name_weights_dictionary
import merchant
from ansi_codes import clearscreen,txt
from town_generator import map_generator,print_map
from validation_and_functions import RandomColour
            
def generate_town_nameM6():
    # this version is too good at generating english names that i need to check whether the generated name already exists or not
    file = open("test_scripts/placenames.txt","r")  # open the existing names file and sanitise it  
    existingNames = []
    for line in file:
        line = line.split("\t",1)
        if len(line) >= 2:
            del line[1]
        line = line[0]
        existingNames.append(line)
    file.close()
    
    weights = town_name_weights_dictionary.weights
    depth = 3
    mutations = True
    checkName = True
    
    alphabet = ["S","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'","&","E"]
    previousCharacters = ""
    for i in range(depth):
        previousCharacters += "S"
    name = ""
    while True:
        if previousCharacters in weights["TOTAL"]:
            cumulativeChoice = randint(1,weights["TOTAL"][previousCharacters])
            total = 0
            for letter,values in weights.items():
                if previousCharacters in values:
                    total += values[previousCharacters]
                if total >= cumulativeChoice:
                    if mutations:
                        if randint(1,100) < 98:
                            character = letter
                        else:
                            validChoiceFound = False
                            while not validChoiceFound:
                                character = alphabet[randint(1,27)]
                                if previousCharacters[1:] + character in weights["TOTAL"]:
                                    validChoiceFound = True
                    else:
                        character = letter
                    newPreviousCharacters = previousCharacters[1:] + character
                    previousCharacters = newPreviousCharacters
                    break
            if character != "E":
                name += character
            else:
                newName = ""
                for letterIndex in range(0,len(name),1):
                    if letterIndex == 0:
                        newName += name[letterIndex].upper()
                    else:
                        if name[letterIndex-1]  == " ":
                            newName += name[letterIndex].upper()
                        else:
                            newName += name[letterIndex]
                if checkName:
                    if newName in existingNames or len(newName) == 3:
                        name = ""
                        previousCharacters = ""
                        for i in range(depth):
                            previousCharacters += "S"
                    else:
                        return newName
                elif len(newName) == 3:
                    name = ""
                    previousCharacters = ""
                    for i in range(depth):
                        previousCharacters += "S"
                else:
                    return newName





class Towns:
    def __init__(self):
        self.towns = []
        self.pity = 0

    def new_random_town(self,inventory):
        newTown = {}
        newTown["name"] = (generate_town_nameM6())
        sizes = {1: "outpost",
                 2: "settlement",
                 3: "village",
                 4: "town",
                 5: "great town"}
        sizeValue = randint(1,5)
        newTown["size"] = [sizeValue,sizes[sizeValue]]
        newTown["map"] = map_generator(3 * newTown["size"][0],3 * newTown["size"][0])
        shops = []
        if randint(1,100) > 70: # 70% chance of generating an apothecary
            shops.append(merchant.Apothecary(inventory))
        if randint(1,100) > 70: # 70% chance of generating a blacksmith
            shops.append(merchant.Blacksmith(inventory))
        if randint(1,100) > 70: # 70% chance of generating a clothier's
            shops.append(merchant.Clothier(inventory))
        newTown["shops"] = (shops)
        newTown["colour"] = RandomColour()
        self.towns.append(newTown)

    def visit_town(self,hero,inv):
        clearscreen()
        chance = ((1-0.5**(self.pity+1))/0.5)*50
        if randint(1,100) < chance or len(self.towns) == 0: #50% base chance of visiting a new town. 100% if it's the first town (obviously)
            self.new_random_town(inv)                       #progressively increases chance if you dont visit a new town, the chance increases based on the sum of the series 1/2^n
            town = self.towns[-1]
            newTown = True
            self.pity = 0
        else: # 50% chance of visiting an already visited town
            self.pity += 1
            town = self.towns[randint(0,len(self.towns)-1)]
            newTown = False

        if newTown:
            print("You find yourself in the " + town["size"][1] + " of " + town["colour"] + town["name"] + txt.sty.reset)
        else:
            print("You find yourself back in the " + town["size"][1] + " of " + town["colour"] + town["name"] + txt.sty.reset)
            
        print()
        print_map(town["map"])
        print()

        for shop in town["shops"]:
            shop.find()
        resting = True
        input("Press enter to continue...")
        while resting:
            print("{}Shop options:{}".format(txt.col.fg.nml.blue,txt.sty.reset)) # shoptions haha
            for i in range(0,len(town["shops"]),1):
                print("\t" + str(i + 1) + ") Enter the " + town["shops"][i].name)
            print("\n{}What would you like to do?{}".format(txt.col.fg.nml.yellow,txt.sty.reset))
            print("{}\"Help\" for help{}".format(txt.col.fg.strg.grey,txt.sty.reset))

            valid = False
            leave = False
            while not leave:
                choice = input()
                choice = choice.split(" ",1)
                if len(choice) == 2:
                    choice[0] = choice[0].lower()
                    if choice[1].isdigit():
                        choice[1] = int(choice[1])
                        if (choice[0] == "enter" or choice[0] == "e") and choice[1] > 0 and choice[1] < len(town["shops"]) + 1:
                            valid = True
                            leave = True
                else:
                    choice = choice[0].lower()
                    if choice == "inventory" or choice == "i":
                        valid = True
                        leave = True
                    elif choice == "continue" or choice == "c":
                        valid = True
                        leave = True
                    elif choice == "help" or choice == "h":
                        valid = True
                        print("{}\nEnter a shop (type \"enter\" plus the number of the shop)".format(txt.col.fg.nml.green))
                        print("Access Inventory (type inventory)")
                        print("Continue Journey (type continue)")
                        print("Abbreviations are: \"e\", \"i\", \"c\" and \"h\" for more help{}".format(txt.sty.reset))
                if not valid:
                    print("{}Enter a valid command!{}".format(txt.warning,txt.sty.reset))

            if choice == "inventory" or choice == "i":
                 inv.access_inventory(hero)
                 if hero.get_hp() <= 0:
                     return
            elif choice == "continue" or choice == "c":
                 resting = False
            else:
                theShop = town["shops"][choice[1] - 1]
                theShop.shop(hero,inv)