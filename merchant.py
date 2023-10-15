from random import randint
from ansi_codes import txt,icons
import Items as it
from validation import validate_int_input

def potion_shop(hero,inventory):
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
        print()
        if inventory.add_general_item(item):
            if item == mystElixir:
                mysBought = True
            print("You successfully bought the item.")
        else:
            hero.set_gold(item.value)
            print("You have been refunded.")



def clothier(hero,inventory):
    #alreadyBought = hero.getItems() - figure this shit out when items are implemented
    print("You enter the homely building. An old man is sitting behind the counter, sewing together a boy's shirt.")
    while True:
        wareList = [] #keeps track of what each option is
        itemNo = 1 # modular shop list - new item? just increment number and you're good to go

        print("\n" + hero.get_name() + ": " + str(hero.get_hp()) + " {}, ".format(icons.heart) + str(hero.get_gold()) + icons.gold)
        for i in range(0,len(wareList),1):
            item = wareList[i]
            print(str(i+1) + ". " + item.name + " - " + item.description + "\t\t " + str(item.value) + icons.gold)

        if not inventory.hasPotionPouch: # if you've not bought the potion pouch
            wareList.append(it.PotionPouch())
            print(str(itemNo) + ". " + it.PotionPouch().name + " - " + it.PotionPouch().description + "\t\t " + str(it.PotionPouch().value) + icons.gold)
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
        print()
        if inventory.add_general_item(item):
            if item == it.PotionPouch():
                inventory.hasPotionPouch = True
            print("You successfully bought the item.")
        else:
            hero.set_gold(item.value)
            print("You have been refunded.")