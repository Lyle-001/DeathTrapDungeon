import town_generator
from random import randint

while True:
    while True:
        town = town_generator.random_odd_value(randint(-5,0),randint(0,8))
        if town == "failed":
            break
    input()