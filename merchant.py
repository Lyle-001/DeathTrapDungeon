def shop(hero):
    #alreadyBought = hero.getItems() - figure this shit out when items are implemented
    print("You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you.")
    mysBought = False
    while True:
        print("\n" + hero.getName() + ": " + str(hero.getHP()) + " Health, " + str(hero.getGold()) + " ¤")
        print("1. Diluted Healing Elixir - Heals you for a small amount.\t\t 5 ¤")
        print("2. Impure Healing Elixir - Heals you for an average amount.\t\t 10 ¤")
        print("3. Distilled Healing Elixir - Heals you for a great amount.\t\t 20 ¤")
        priceList = [5,10,20] #keeps track of prices for options
        wareList = ["sh","mh","lh"] #keeps track of what each option is
        itemNo = 4 # modular shop list - new item? just increment number and you're good to go

        if not mysBought: # if you've not bought the mystery potion
            mysPrice = random.randint(3,20) # random price and random effects
            print(str(itemNo) + ". Mystery Elixir - An unknown elixir. Who knows what it does?\t\t " + str(mysPrice) + " ¤")
            priceList.append(mysPrice)
            wareList.append("me")
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
                hero.heal(random.randint(5,10))
            elif effect == 5:
                print("You feel the flask's contents burning down your throat, causing you some discomfort.")
                hero.receiveDamage(random.randint(3,5))
            elif effect == 6:
                print("Too late you realise the recklessness of your drinking as poison spills down your throat, taking its effect in seconds.")
                hero.receiveDamage(1000) #there's more elegant ways to kill you, yes. there's also more elegant ways to make a game and i don't see them used here
                return
            


