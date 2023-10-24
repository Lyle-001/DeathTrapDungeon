import towns
import os


print("what version (1-6)")
version = int(input())


if version == 1:
    while True:
        print(towns.generate_town_nameM1().capitalize(),end="")
        input()
elif version == 2:
    while True:
        print(towns.generate_town_nameM2().capitalize(),end="")
        input()
elif version == 3:
    while True:
        print(towns.generate_town_nameM3().capitalize(),end="")
        input()
elif version == 4:
    while True:
        print(towns.generate_town_nameM4().capitalize(),end="")
        input()
elif version == 5:
    while True:
        print(towns.generate_town_nameM5(),end="")
        input()
elif version == 6:
    while True:
        print(towns.generate_town_nameM6(),end="")
        input()