from Weapons import ClassicSword

legendary = godly = epic = mighty = rare = common = shoddy = awful = broken = 0
for loop in range(0,50000,1):
    sword = ClassicSword()
    sword.randomise_modifier(0)
    name = sword.get_name()
    if name[0] == "l":
        legendary += 1
    elif name[0] == "g":
        godly += 1
    elif name[0] == "e":
        epic += 1
    elif name[0] == "m":
        mighty += 1
    elif name[0] == "r":
        rare += 1
    elif name[0] == "c":
        common += 1
    elif name[0] == "s":
        shoddy += 1
    elif name[0] == "a":
        awful += 1
    elif name[0] == "b":
        broken += 1
print("legendary: " + str(legendary))
print("godly: " + str(godly))
print("epic: " + str(epic))
print("mighty: " + str(mighty))
print("rare: " + str(rare))
print("common: " + str(common))
print("shoddy: " + str(shoddy))
print("awful: " + str(awful))
print("broken: " + str(broken))
