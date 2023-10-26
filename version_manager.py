print("Which version of Death Trap Dungeon do you want to play?")
print("\t1) Dan's version")
print("\t2) Ethan's version")
print("\t3) Ebaad's version")

valid = False
while not valid:
    try:
        version = int(input())
        if version >= 1 and version <= 3:
            valid = True
        else:
            raise Exception
    except:
        print("Please enter a number between 1 and 3.")

if version == 1:
    import DanDeath_Trap_Dungeon
elif version == 2:
    import Ethanmain
else:
    import Ebaadmain
