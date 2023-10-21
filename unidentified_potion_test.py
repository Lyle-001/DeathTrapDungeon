import Items
import Heroes
import inventoryfile

player = Heroes.Hero("[PLAYER NAME]")
inventory = inventoryfile.inventory(False)
while True:
    input()
    potion = Items.UnidentifiedElixir()
    inventory.add_general_item([potion,1])
    print(potion.identity)
    print(potion.inspect())
    potion.use(player,inventory)