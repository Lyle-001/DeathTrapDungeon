from random import randint

# Genders of all enemies are male right now, but later it will be randomised for extra detail
# Currently, only the Monster has random pre-attack talking lines depending on mental states. This will be extended to all enemies soon but im lazy rn whoops!

class Monster:
    # Construction
    def __init__(self,colour):
        monsterMessageBank = [
            'He stabs you with his knife-like talons!',
            'He catches you by surprise and tenderises you with his massive club!',
            'He beats you up like a bully!',
            'He hurts you emotionally by saying mean things :(',
            'He lightly scrapes you with his 18 foot long fangs.',
            'He reminds you of your traumatising childhood and laughs at you :('
            'He touches you inappropriately.',
            'His scary aura engulfs you!!',
            'He whispers "scuderia" in your ear, shocking you to the bone.'
        ]
        self.colour = colour
        self.species = "monster"
        self.hitPoints = 10
        self.maxDamage = 5
        self.attackMessage = monsterMessageBank[random.randint(0, len(monsterMessageBank) - 1)]
        self.gold = randint(4,6)
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)

    # Getters
    def get_colour(self):
        return self.colour

    def get_species(self):
        return self.species

    def get_hitPoints(self):
        return self.hitPoints

    def getGold(self):
        return self.gold

    def getFortitude(self):
        return self.mentalFortitude

    def getEgo(self):
        return self.ego

    # Methods
    def attack(self): # Defines monster attack behaviour and returns the damage inflicted.
        damage = randint(0,self.maxDamage)
        if damage == 0:
            print("You successfully dodge the blow!")
        elif damage == 1:
            print("A glancing blow! You take 1 ♡.")
        else:
            print(self.attackMessage + " You take "
                  + str(damage) + " ♡.")
        return damage

    def receive_damage(self,damage): # Subtracts damage from the monster and prints out related message.
        if damage == 0:
            print("Miss! The " + self.species + " is too fast for you.")
        elif damage == 1:
            print("You strike a glancing blow for 1 point of damage.")
        else:
            print("The " + self.species + " takes " + str(damage)
                  + " ♡.")
        self.hitPoints -= damage

    def talk(self): # Prints monster's battle cry
        highFortandEgo = ['May the best man win.', #Additional logic will be completed later, im lazy rn
                          'En garde!',
                          'Show me you can fight, heathen!',
                          'Father, I will make you proud!',
                          'This is for my family',
                          'I will give you the honour of a swift death.',
                          'I promised my family I would get them food.',
                          "I'm sorry about this.",
                          'I will give you the honour of a respectable death.',
                          'STAND AND FIGHT, HUMAN!',
                          'RALLY, AND FIGHT!',
                          'IN THE NAME OF GOD AND COUNTRY, I WILL END YOU!',
                          'May God have mercy on your poor soul.'
                          'There is nothing personal about this.'
                          ]

        normalMonster = ['ROOOOAR!!',
                         'YOUR TIME ENDS NOW',
                         "I'M GOING TO SKIN YOU ALIVE",
                         'AFTER THIS I AM GOING FOR YOUR FAMILY',
                         "YOU'RE GOING TO TASTE SO DELICIOUS!",
                         "I'M GOING TO USE YOUR BLOOD FOR THE CHILLI COOK OFF NEXT WEEK!",
                         'I WILL WIPE THE FLOOR WITH YOU!',
                         "I'M GOING TO CLEAN MY TEETH WITH YOUR BONES!",
                         'GAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH',
                         'RRAAAARRL!!',
                         'YEEEAAARRRGGGGHHH!!',
                         'SKREEEEEEEENNNNKKK!!',
                         'HWOOOOAAAARRR!!'
                         ]

        fortitude = self.getFortitude()
        ego = self.getEgo()

        bothCheck = False
        highFort = False
        highEgo = False

        if fortitude >= 70:
            highFort = True

        if ego >= 70:
            highEgo = True

        if highFort == True and highEgo == True:
            print('The Monster says: ' + '"' + highFortandEgo[random.randint(0, len(highFortandEgo) - 1)] + '"') # This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Monster says: ' + '"' + normalMonster[random.randint(0, len(normalMonster) - 1)] + '"') # This will be changed later depending on the Mental Fortitude and Ego attribute!!

class Goblin(Monster):
    # Construction
    def __init__(self,colour):
        goblinMessageBank = [
            'He vocalises menacingly!',
            'He starts spinning around in a frightening manner!',
            'He swings his Scimitar!',
            'He fies a shot from its Shortbow!',
            'He bites your knees!',
            'He headbutts your calves!'
            'He scratches your feet!',
            'He jumps and punches your nipples!',
            'He beats your shins!',
            'He fires a falafaluten!'
        ]
        self.colour = colour
        self.species = "goblin"
        self.hitPoints = 12
        self.maxDamage = 6
        self.attackMessage = goblinMessageBank[random.randint(0, len(goblinMessageBank) - 1)]
        self.gold = randint(4,12)
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)
    # Methods
    def talk(self):
        highFortandEgo = ["I'm sorry, my family needs money.", 
                          'I will do you the honour of not desecrating your corpse.',
                          "Please, don't make this harder than it has to be.",
                          'I promised my wife we could eat tonight.',
                          "I just want to sell your weapon, not fight.",
                          'May God rest your soul.',
                          'I wish it could have been any other way, but I need some money.',
                          "I'm sorry about this.",
                          'I will give you the honour of a respectable death.',
                          'I owe money to some vampire debt collectors. Please make this easy.',
                          'My family is in a grave debt to the slimes. Please let me sell your tailbone.',
                          'When I kill you, I promise I will do you the honour of a proper burial.',
                          'May God have mercy on your poor soul.',
                          'There is nothing personal about this.'
                          ]

        normalMonster = ['Tee hee hee, you will never get my riches',
                         'THESE ARE MY TREASURES!',
                         "I SMELL MONEYYY",
                         "I'm going to take all your money!!!",
                         "The Pawn Shop will give me an great deal for that there weapon of yours!",
                         "Bloodied armour sells especially well with collectors nowadays!",
                         'I SEE MONEYYYYY',
                         "I'M GOING TO CLEAN MY TEETH WITH YOUR BONES!",
                         'MONEY MONEY MONEY MONEY MONEY',
                         "I'll sell your teeth to my dentist!",
                         'Nice hair. Would be a shame if I took your scalp and sold it to my dermatologist.',
                         'EEEEEEEEEEEEEEEEEEEEEEEEEE!!',
                         'GAHGAHGAHGAHGAH!!'
                         ]

        fortitude = self.getFortitude()
        ego = self.getEgo()

        bothCheck = False
        highFort = False
        highEgo = False

        if fortitude >= 70:
            highFort = True

        if ego >= 70:
            highEgo = True

        if highFort == True and highEgo == True:
            print('The Goblin says: ' + '"' + highFortandEgo[random.randint(0, len(highFortandEgo) - 1)] + '"') # This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Goblin says: ' + '"' + normalMonster[random.randint(0, len(normalMonster) - 1)] + '"') # This will be changed later depending on the Mental Fortitude and Ego attribute!!

class Vampire(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "vampire"
        self.hitPoints = 20
        self.maxDamage = 7
        self.attackMessage = "It sinks its fangs into your neck."
        self.gold = randint(3,10)
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)

    # Methods
    def talk(self):
        print("I vant to drink your blood!")

class Slime(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour
        self.species = "slime"
        self.hitPoints = 8
        self.maxDamage = 4
        self.attackMessage = "It tries to engulf you."
        self.gold = randint(0,6)
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)

    # Methods
    def talk(self):
        print("Boooiiinnnggg!")

class RogueWarrior(Monster):

    # Construction
    def __init__(self,colour):
        self.colour = colour +  "-shielded"
        self.species = "rogue warrior"
        self.hitPoints = 25
        self.maxDamage = 6
        self.attackMessage = "They slash at you."
        self.gold = randint(8,18)
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)

    # Methods
    def talk(self):
        print("I'll kill you!")
