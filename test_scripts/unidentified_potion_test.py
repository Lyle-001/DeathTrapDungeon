import Items
import Heroes
import inventoryfile

player = Heroes.Hero("[PLAYER NAME]")
inventory = inventoryfile.inventory()
while True:
    input()
    potion = Items.UnidentifiedElixir()
    inventory.add_item("general",potion,1)
    inventory.access_inventory(player)
    print(potion.identity)
    print(potion.inspect(inventory))
    potion.use(player,inventory)