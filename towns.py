from random import randint
import town_name_weights
import merchant
from ansi_codes import clearscreen

def generate_town_nameM1():
    name = ""
    for character in range(0,randint(2,10),1):
        name += chr(randint(97,122))
    return name

def generate_town_nameM2():

    name = ""
    lastLetter = "vowel"
    previousLetter = "consonant"

    def add_vowel(word,mostRecentLetter):
        vowels = ["a","e","i","o","u","y"]
        leastRecentLetter = mostRecentLetter
        mostRecentLetter = "vowel"
        word += vowels[randint(0,5)]
        return word,mostRecentLetter,leastRecentLetter

    def add_consonant(word,mostRecentLetter):
        consonants = ["b","c","d","f","g","h","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
        leastRecentLetter = mostRecentLetter
        mostRecentLetter = "consonant"
        word += consonants[randint(0,5)]
        return word,mostRecentLetter,leastRecentLetter

    for character in range(randint(2,10)):
        if lastLetter == "consonant":
            name,lastLetter,previousLetter = add_vowel(name,lastLetter)
        else:
            if previousLetter == "vowel":
                name,lastLetter,previousLetter = add_consonant(name,lastLetter)
            else:
                option = randint(0,1)
                if option == 0:
                    name,lastLetter,previousLetter = add_vowel(name,lastLetter)
                else:
                    name,lastLetter,previousLetter = add_consonant(name,lastLetter)
    return name

def generate_town_nameM3():

    def get_non_vowel_phoneme():
        plosives = ["p","t","k","b","d","g"]
        fricatives = ["f","v","s","z","sh","zh"]
        nasals = ["m","n","ng"]
        liquids = ["l","r"]
        glides = ["w","y"]
        phoneme = randint(0,4)
        if phoneme == 0:
            phoneme = plosives[randint(0,len(plosives)-1)]
        elif phoneme == 1:
            phoneme = fricatives[randint(0,len(fricatives)-1)]
        elif phoneme == 2:
            phoneme = nasals[randint(0,len(nasals)-1)]
        elif phoneme == 3:
            phoneme = liquids[randint(0,len(liquids)-1)]
        else:
            phoneme = glides[randint(0,len(glides)-1)]
        return phoneme

    def get_vowel_phoneme():
        vowels = ["a","e","i","o","u"]
        return vowels[randint(0,len(vowels)-1)]


    name = ""
    for syllableCount in range(randint(1,4)):
        syllable = ""
        if randint(1,100) < 80: # 80% chance to choose a starting phoneme
            syllable += get_non_vowel_phoneme()
        syllable += get_vowel_phoneme()
        if randint(1,100) < 80: # 80% chance to choose an ending phoneme
            syllable += get_non_vowel_phoneme()

        name += syllable
    return name

def generate_town_nameM4():
    alphabet = ["START","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'","&","END"]
    weights = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [37, 0, 20, 28, 17, 71, 11, 14, 156, 2, 1, 0, 34, 44, 11, 5, 12, 0, 41, 21, 27, 2, 1, 41, 0, 9, 1, 27, 4, 0, 0, 0], 
               [126, 6, 2, 0, 9, 8, 0, 6, 8, 0, 0, 6, 7, 21, 10, 3, 0, 0, 10, 21, 6, 0, 0, 6, 4, 4, 0, 12, 3, 0, 0, 0], 
               [90, 19, 0, 5, 3, 8, 0, 0, 1, 36, 0, 0, 2, 0, 17, 15, 0, 0, 10, 7, 13, 9, 0, 2, 0, 2, 0, 14, 2, 0, 0, 0], 
               [37, 32, 1, 0, 12, 32, 0, 4, 2, 51, 0, 0, 38, 0, 69, 31, 1, 0, 63, 6, 0, 11, 0, 2, 0, 6, 0, 4, 3, 0, 0, 0], 
               [35, 0, 35, 12, 55, 22, 9, 42, 71, 23, 0, 43, 169, 35, 69, 5, 28, 0, 97, 51, 83, 2, 42, 53, 1, 4, 2, 6, 2, 0, 0, 0], 
               [29, 7, 0, 0, 7, 8, 8, 4, 5, 4, 0, 2, 5, 2, 6, 5, 0, 0, 9, 11, 15, 1, 0, 0, 1, 0, 0, 4, 4, 0, 0, 0], 
               [27, 9, 0, 0, 34, 7, 0, 4, 1, 29, 0, 0, 0, 0, 99, 3, 0, 0, 5, 4, 1, 32, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
               [78, 1, 0, 80, 10, 14, 1, 69, 0, 2, 0, 6, 1, 0, 22, 2, 3, 0, 5, 87, 141, 0, 0, 11, 3, 1, 0, 10, 1, 0, 0, 0], 
               [12, 18, 20, 4, 12, 18, 22, 7, 71, 0, 0, 26, 39, 32, 8, 2, 9, 0, 66, 11, 15, 2, 5, 62, 0, 0, 1, 3, 11, 0, 0, 0], 
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
               [25, 5, 0, 45, 0, 1, 0, 0, 0, 0, 0, 0, 6, 0, 2, 9, 0, 0, 31, 8, 0, 1, 0, 3, 0, 1, 0, 1, 0, 0, 0, 0], 
               [44, 82, 14, 16, 21, 75, 5, 7, 7, 47, 0, 7, 67, 4, 7, 39, 5, 0, 24, 17, 24, 9, 0, 8, 1, 5, 0, 9, 9, 0, 0, 0], 
               [56, 121, 0, 0, 6, 12, 0, 0, 3, 7, 0, 0, 10, 1, 3, 24, 0, 0, 11, 3, 2, 5, 0, 2, 3, 8, 0, 21, 3, 0, 0, 0], 
               [44, 73, 0, 0, 5, 85, 1, 7, 1, 146, 0, 2, 5, 1, 7, 235, 0, 0, 45, 2, 4, 26, 0, 5, 0, 11, 0, 5, 1, 0, 0, 0], 
               [17, 0, 41, 38, 29, 4, 62, 5, 39, 1, 2, 0, 31, 34, 28, 35, 33, 0, 78, 31, 201, 0, 3, 57, 0, 4, 1, 3, 18, 0, 0, 0], 
               [37, 5, 0, 0, 1, 10, 0, 1, 1, 9, 0, 2, 2, 15, 0, 9, 8, 0, 10, 7, 0, 14, 0, 3, 0, 1, 0, 4, 1, 0, 0, 0], 
               [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
               [39, 92, 65, 21, 6, 133, 9, 22, 4, 44, 0, 2, 1, 0, 2, 199, 5, 0, 11, 0, 22, 69, 0, 1, 0, 0, 0, 10, 0, 0, 0, 0], 
               [130, 40, 0, 0, 24, 107, 0, 6, 1, 30, 0, 11, 27, 16, 36, 15, 11, 0, 35, 18, 5, 9, 0, 4, 1, 6, 0, 24, 16, 6, 0, 0], 
               [41, 49, 0, 2, 0, 50, 3, 31, 11, 36, 0, 1, 30, 0, 40, 24, 15, 0, 87, 172, 29, 42, 0, 7, 3, 7, 0, 7, 14, 0, 0, 0], 
               [6, 6, 54, 4, 9, 0, 3, 2, 18, 0, 1, 0, 6, 3, 2, 79, 2, 4, 9, 11, 4, 0, 0, 0, 0, 0, 0, 2, 11, 0, 0, 0], 
               [2, 16, 0, 0, 0, 11, 0, 0, 0, 6, 0, 0, 6, 0, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [103, 12, 0, 0, 4, 36, 0, 4, 11, 0, 0, 2, 2, 3, 5, 37, 1, 0, 11, 19, 13, 0, 0, 0, 0, 3, 0, 18, 8, 0, 0, 0], 
               [0, 6, 0, 0, 0, 9, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [5, 16, 25, 0, 1, 85, 0, 0, 4, 0, 0, 0, 16, 1, 3, 7, 0, 0, 38, 1, 4, 0, 1, 3, 0, 0, 0, 5, 0, 0, 0, 0], 
               [0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
               [0, 0, 1, 0, 21, 13, 3, 5, 25, 0, 0, 1, 7, 8, 23, 0, 1, 0, 10, 8, 43, 0, 0, 6, 0, 21, 0, 0, 0, 0, 2, 0], 
               [0, 1, 0, 0, 2, 13, 0, 0, 6, 0, 0, 2, 2, 3, 59, 0, 0, 0, 7, 3, 3, 0, 0, 2, 0, 9, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
               [0, 18, 0, 0, 117, 164, 0, 19, 102, 0, 0, 25, 40, 78, 180, 0, 3, 0, 42, 59, 46, 0, 0, 13, 4, 113, 0, 0, 0, 0, 0, 0], 
               [1023, 637, 278, 255, 405, 996, 137, 260, 548, 476, 4, 138, 553, 301, 711, 795, 140, 4, 757, 578, 701, 236, 52, 292, 21, 215, 5, 198, 112, 6, 2, 0]]

    previousCharacter = 0
    name = ""
    while True:
        cumulativeChoice = randint(0,weights[len(alphabet)][previousCharacter])
        total = 0
        for letterIndex in range(len(weights)):
            letter = weights[letterIndex]
            total += letter[previousCharacter]
            if total >= cumulativeChoice:
                character = alphabet[letterIndex]
                previousCharacter = letterIndex
                break
        if character != "END":
            name += character
        else:
            return name


def generate_town_name():
    weights = town_name_weights.weights

    alphabet = ["START","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'","&","END"]
    previousCharacters = [0,0]
    name = ""
    while True:
        cumulativeChoice = randint(0,weights[len(alphabet)][previousCharacters[1]][previousCharacters[0]])
        if cumulativeChoice != 0:
            total = 0
            for letterIndex in range(1,len(weights)-1):
                total += weights[letterIndex][previousCharacters[0]][previousCharacters[1]]
                if total >= cumulativeChoice:
                    character = alphabet[letterIndex]
                    previousCharacters[1] = previousCharacters[0]
                    previousCharacters[0] = letterIndex
                    break
            if character != "END":
                name += character
            else:
                newName = ""
                for letterIndex in range(0,len(name),1):
                    if letterIndex == 0:
                        newName += name[letterIndex].upper()
                    else:
                        if name[letterIndex-1] in ["-"," ","&"]:
                            newName += name[letterIndex].upper()
                        else:
                            newName += name[letterIndex]


                name = newName
                return name







class Towns:
    def __init__(self):
        self.towns = []

    def new_random_town(self,inventory):
        newTown = {}
        newTown["name"] = (generate_town_name())
        shops = []
        if randint(1,100) > 70: # 70% chance of generating an apothecary
            shops.append(merchant.Apothecary(inventory))
        if randint(1,100) > 70: # 70% chance of generating a blacksmith
            shops.append(merchant.Blacksmith(inventory))
        if randint(1,100) > 70: # 70% chance of generating a clothier's
            shops.append(merchant.Clothier(inventory))
        newTown["shops"] = (shops)
        self.towns.append(newTown)

    def visit_town(self,hero,inv):
        clearscreen()
        if randint(1,100) < 50 or len(self.towns) == 0: #50% chance of visiting a new town. 100% if it's the first town (obviously)
            self.new_random_town(inv)
            town = self.towns[-1]
            newTown = True
        else: # 50% chance of visiting an already visited town
            town = self.towns[randint(0,len(self.towns)-1)]
            newTown = False

        if newTown:
            print("You find yourself in the town of " + town["name"])
        else:
            print("You find yourself back in the town of " + town["name"])

        for shop in town["shops"]:
            shop.find()
        resting = True
        input("Press enter to continue...")
        while resting:
            print("Shop options:") # shoptions haha
            for i in range(0,len(town["shops"]),1):
                print("\t" + str(i + 1) + ") Enter the " + town["shops"][i].name)
            print("Options:")
            print("\tEnter a shop (type \"enter\" plus the number of the shop)")
            print("\tAccess Inventory (type inventory)")
            print("\tContinue Journey (type continue)")

            valid = False
            while not valid:
                choice = input()
                choice = choice.split(" ",1)
                if len(choice) == 2:
                    if choice[1].isdigit():
                        choice[1] = int(choice[1])
                        if choice[0] == "enter" and choice[1] > 0 and choice[1] < len(town["shops"]) + 1:
                            valid = True
                else:
                    choice = choice[0]
                    if choice == "inventory":
                        valid = True
                    elif choice == "continue":
                        valid = True
                if not valid:
                    print("Enter a valid command!")

            if choice == "inventory":
                 inv.access_inventory(hero)
                 if hero.get_hp() <= 0:
                     return
            elif choice == "continue":
                 resting = False
            else:
                theShop = town["shops"][choice[1] - 1]
                theShop.shop(hero,inv)