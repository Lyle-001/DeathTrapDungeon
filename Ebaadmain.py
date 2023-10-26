from Monster import Monster
import random

def randomColour():
    colourList = ['green', 'yellow', 'red', 'purple', 'black']
    colour = colourList[random.randint(0, len(colourList) - 1)]
    return colour

def combat(heroHP, enemy):
    MonsterHP = enemy.getHealthPoints()
    HeroHP = heroHP
    while HeroHP > 0 and MonsterHP > 0:
        print('\n######### Hero: ' + str(heroHP) + 'HP #########' +
              ' Monster: ' + str(MonsterHP) + 'HP #########\n')
        key = input('Press enter to attack! ') #Lazy fight system, I'll revamp it to be more engaging later
        print()
        heroDamage = random.randint(0,15)
        enemy.recieveDamage(heroDamage)
        if MonsterHP > 0:
            print('The ' + str(enemy.getSpecies()) + ' attacks!')
            print()
            key = input('Press enter to defend! ')
            print()
            HeroHP -= enemy.attack()
    return HeroHP



print('#####  WELCOME TO DEATH TRAP DUNGEON!  ######')
print('')

heroHealth = random.randint(10,32)
victories = 0

while victories < 3 and heroHealth > 0:
    monster = Monster(randomColour())
    monster.monsterCry()
    heroHealth = combat(heroHealth, monster)

    if heroHealth > 0:
        victories += 1
        key = input('Hooray! You won! Press any key for the next attack')
    else:
        print('You died!')


if victories == 3:
    print('You won the entire game! WOAH!')
