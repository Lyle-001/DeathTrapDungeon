from Ethanenemy import Monster, Goblin, Vampire, Thrall, Chained
from Ethanhero import Hero, Archer, WPriest, Warlock, Fool
import random

def randomAdj():
    adjList = ["Vile", "Putrid", "Godless", "Vicious", "Reprehensible", "Condemned"]
    adj = adjList[random.randint(0,len(adjList)-1)]
    return adj

def combat(hero, enemy):
    while hero.getHP() > 0 and enemy.getHitPoints() > 0:
        print("\n# " + hero.getName() + ": " + str(hero.getHP()) + " Health #" +
              "\n# " + enemy.getAdj() + " " + enemy.getSpecies() + ": " + str(enemy.getHitPoints())
              + " Health #")
        input("Hit enter to attack!")
        enemy.receiveDamage(hero.attack())
        if enemy.getHitPoints() > 0:
            print("The " + enemy.getSpecies() + " takes its chance to attack!")
            input("Hit enter to brace yourself!")
            hero.receiveDamage(enemy.attack())
        else:
            enemy.death()

def merchant(hero):
    alreadyBought = hero.getItems()
    print("You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you.")
    mysBought = False
    while True:
        print("\n" + hero.getName() + ": " + str(hero.getHP()) + " Health, " + str(hero.getGold()) + " Gold")
        print("1. Diluted Healing Elixir - Heals you for a small amount.\t\t 5 Gold")
        print("2. Impure Healing Elixir - Heals you for an average amount.\t\t 10 Gold")
        print("3. Distilled Healing Elixir - Heals you for a great amount.\t\t 20 Gold")
        priceList = [5,10,20] #keeps track of prices for options
        wareList = ["sh","mh","lh"] #keeps track of what each option is
        itemNo = 4 # modular shop list - new item? just increment number and you're good to go

        if not mysBought: # if you've not bought the mystery potion
            mysPrice = random.randint(8,20) # random price and random effects
            print(str(itemNo) + ". Mystery Elixir - An unknown elixir. Who knows what it does?\t\t " + str(mysPrice) + " Gold")
            priceList.append(mysPrice)
            wareList.append("me")
            itemNo += 1

        if "holy" not in alreadyBought and hero.getClass() == "wp":
            print(str(itemNo) + ". Holy Idol - A depiction of your god! Just seeing it empowers you. 7 Gold")
            priceList.append(15)
            wareList.append("holy")
            itemNo += 1
        elif "idol" not in alreadyBought and hero.getClass() != "wp":
            print(str(itemNo) + ". Religious Idol - A god unknown to you, made into a statue.\t\t 7 Gold")
            priceList.append(7)
            wareList.append("idol")
            itemNo += 1

        choice = input("Does much of anything catch your eye? Y/N ").upper()
        if choice == "N":
            return
        bought = False
        while not bought: #check they've chosen an option that's valid
            try:
                choice = input("After much deliberation, you decide to take item... ")
                choice = int(choice) - 1
                bought = hero.purchase(priceList[choice])
                if not bought:
                    print("You check your pouch, only to find you cannot afford the luxury of that item!")
                    choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                    if choice == "N":
                        return
            except:
                print("That's not right, you think, there is no option " + str(choice + 1) + "!")
                choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                if choice == "N":
                    return
        if wareList[choice] == "sh": #check what that option is
            hero.heal(random.randint(3,7))
            print("The weak elixir eases you slightly, but isn't the most pleasant...")
        elif wareList[choice] == "mh":
            hero.heal(random.randint(5,10))
            print("Your wounds feel somewhat better, and you feel full of a new vigour.")
        elif wareList[choice] == "lh":
            hero.heal(random.randint(15,20))
            print("As the formulation pours down your throat, you feel better in body and soul, ready to take on the next fight!")

        elif wareList[choice] == "me": #mystery potion code
            effect = random.randint(1,6)
            if effect <= 3: #weighted towards nothing
                print("As you drink it, you realise it is a phony elixir, with no effects other than an unpleasant taste.")
            elif effect == 4:
                print("The potion tastes vile, but turns out to be medicinal.")
                hero.heal(random.randint(1,6))
            elif effect == 5:
                print("You feel the flask's contents burning down your throat, causing you some discomfort.")
                hero.receiveDamage(random.randint(1,6))
            elif effect == 6:
                print("Too late you realise the recklessness of your drinking as the poison spills down your throat, taking its effect in minutes.")
                hero.receiveDamage(1000) #there's more elegant ways to kill you, yes. there's also more elegant ways to make a game and i don't see them used here
                return
            
        elif wareList[choice] == "holy":
            hero.gainItem("holy")
            alreadyBought = hero.getItems()
            print("Your deity! It is truly a sign that your faith has paid off, reinforcing both belief and body!")
            hero.gainMaxH(10)
            hero.heal(8)

        elif wareList[choice] == "idol" and hero.getClass() != "wa":
            hero.gainItem("idol")
            alreadyBought = hero.getItems()
            print("A religious statue of no relevance to you. You feel rage emanating from it, as if it is angered by your heresy.")
            choice = input("Cast it away? Y/N ")
            if choice == "Y":
                print("The statue breaks as it hits the floor, and you feel a sharp stab in your hand. The bleeding is painful, but it is better than angering a god.")
                hero.receiveDamage(3)
            elif choice == "N":
                print("You put the statue in your satchel, but feel drained by the extra weight.")
                hero.gainMaxH(-3)

        elif wareList[choice] == "idol":
            hero.gainItem("idol")
            alreadyBought = hero.getItems()
            print("This figure deserves no more respect than the beasts you slaughtered to get here. As you shatter it, you feel more assured that you can perform such affronts to divine beings.")
            hero.gainMaxD(3)
            hero.gainMinD(1)

print("The gore-coated hallways of Deathtrap Dungeon await you.")
name = input("But who is it they await? ")
print("Many have tried before you. What will bring you success?")
print("Are you an Archer? Your strikes may be deadly but your aim is not perfect and your weapon of choice leaves little room for protection.")
print("Are you a Warrior Priest? Your deity will help defend you but your weaponry falls short of others.")
print("Are you a Warlock? Your eldritch magicks are inescapable, but do little against the foul beings in these halls.")
choice = input("\t 1) Archer \n\t 2) Warrior Priest \n\t 3) Warlock\n")
if choice == "1":
    player = Archer(name)
elif choice == "2":
    player = WPriest(name)
elif choice == "3":
    player = Warlock(name)
else:
    player = Fool(name)
victories = 0
while victories < 10 and player.getHP() > 0:
    encounter = random.randint(0,20)
    if encounter == 20:
        monster = Chained()
    elif encounter > 15:
        monster = Vampire(randomAdj())
    elif encounter > 12:
        monster = Goblin(randomAdj())
    elif encounter > 5:
        monster = Monster(randomAdj())
    else:
        monster = Thrall(randomAdj())
    print("\nA " + monster.getAdj() + " " + monster.getSpecies() + " emerges from the dark!")
    monster.talk()
    combat(player, monster)
    if player.getHP() > 0:
        gold = monster.getGold()
        player.setGold(gold)
        victories += 1
        print("Scattered around are coins. You gather them up, finding " + str(gold) + " coins.")
        print("You drop them into your pouch, bringing you to " + str(player.getGold()) + " coins total.")
        choice = input("Up ahead, you see a cloth structure set up in one of the chambers of the dungeon. Would you like to investigate? (Y/N) ").upper()
        if choice == "Y":
            merchant(player)
        else:
            print("You trek on, ignoring the glow from within it.")
if victories == 10:
    print("Having swept through the dungeon, you finally leave with " + str(player.getGold) + " coins in your pocket. The title of Champion is yours, until the monstrosities return...")
elif player.getHP() <= 0:
        if player.getClass() == "ar":
            print("Your bowstring snapped and fragile body broken, your accuracy was not great enough to save you.")
        elif player.getClass() == "wp":
            print("Your prayers go unanswered as you slip into Death's embrace. Your god cares not for failures.")
        elif player.getClass() == "wa":
            print("Your pact with the darkness broken, both magick and soul slip from your body, leaving a single word engraved on your forehead: \"Betrayer\".")
        elif player.getClass() == "fo":
            print("Your existence was erroneous, not meant for this world. Destiny has taken its revenge on you.")
        print(player.getName() + " is lost from the memory of the people, and your body is not found for your family.")
