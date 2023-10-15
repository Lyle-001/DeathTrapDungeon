from random import randint
import Items as it

def shop(hero):
    #alreadyBought = hero.getItems() - figure this shit out when items are implemented
    print("You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you.")
    mysBought = False
    while True:
        print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " Health, " + str(hero.get_gold()) + " ¤")
        print("1. Diluted Healing Elixir - Heals you for a small amount.\t\t 5 ¤")
        print("2. Impure Healing Elixir - Heals you for an average amount.\t\t 10 ¤")
        print("3. Distilled Healing Elixir - Heals you for a great amount.\t\t 20 ¤")
        priceList = [5,10,20] #keeps track of prices for options
        wareList = [it.DilutedHealingElixir(),it.ImpureHealingElixir(),it.DistilledHealingElixir()] #keeps track of what each option is
        itemNo = 4 # modular shop list - new item? just increment number and you're good to go

        if not mysBought: # if you've not bought the mystery potion
            mysPrice = randint(3,20) # random price and random effects
            print(str(itemNo) + ". Mystery Elixir - An unknown elixir. Who knows what it does?\t\t " + str(mysPrice) + " ¤")
            priceList.append(mysPrice)
            wareList.append(it.MysteryElixir)
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
                    print("You check your coin pouch, only to find you cannot afford the luxury of that item!")
                    choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                    if choice == "N":
                        return
            except:
                print("That's not right, you think, there is no option " + str(choice + 1) + "!")
                choice = input("You reconsider if you want any of these wares. (Y/N) ").upper()
                if choice == "N":
                    return
        item = wareList[choice]
        print()
        item.use(hero)
        if hero.get_hp() == 0:
            return
