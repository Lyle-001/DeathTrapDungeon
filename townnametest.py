import towns

print("what version (1-5)")
version = int(input())

if version == 1:
    while True:
        print(towns.generate_town_nameM1().capitalize())
        input()
elif version == 2:
    while True:
        print(towns.generate_town_nameM2().capitalize())
        input()
elif version == 3:
    while True:
        print(towns.generate_town_nameM3().capitalize())
        input()
elif version == 4:
    while True:
        print(towns.generate_town_nameM4().capitalize())
        input()
elif version == 5:
    while True:
        print(towns.generate_town_nameM5())
        input()