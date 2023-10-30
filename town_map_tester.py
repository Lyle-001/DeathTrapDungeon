import town_generator
from random import randint

while True:
    town = town_generator.town_generator2(50,50)
    town_generator.print_map(town)
    input()