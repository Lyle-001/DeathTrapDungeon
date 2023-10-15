from random import randint
from ansi_codes import txt,icons
import Items as it
from validation import validate_int_input

def shop(hero):
    #alreadyBought = hero.getItems() - figure this shit out when items are implemented
    print("You enter the dimly lit tent, as a hunch-backed man gestures at the wares around you.")
    mysBought = False
    while True:
        wareList = [it.DilutedHealingElixir(),it.ImpureHealingElixir(),it.DistilledHealingElixir()] #keeps track of what each option is
        itemNo = 4 # modular shop list - new item? just increment number and you're good to go

        print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)
        for i in range(0,len(wareList),1):
            item = wareList[i]
            print(str(i+1) + ". " + item.name + " - " + item.description + "\t\t " + str(item.value) + icons.gold)

        if not mysBought: # if you've not bought the mystery potion
            mystElixir = it.MysteryElixir()
            print(str(itemNo) + ". " + mystElixir.name + " - " + mystElixir.description + "\t\t " + str(mystElixir.value) + icons.gold)
            wareList.append(mystElixir)
            itemNo += 1

        choice = input("Does much of anything catch your eye? Y/N ").upper()
        if choice == "N":
            return
        bought = False
        while not bought: #check they've chosen an option that's valid
            try:
                choice = validate_int_input("After much deliberation, you decide to take item... ") - 1
                bought = hero.purchase(wareList[choice].value)
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
        if item == mystElixir:
            mysBought = True
        print()
        item.use(hero)
        if hero.get_hp() == 0:
            return
