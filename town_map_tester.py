import town_generator
from random import randint

while True:
    town = town_generator.road_generator(50,50)
    town = town_generator.add_buildings(town,10)
    town_generator.print_map(town)
    input()