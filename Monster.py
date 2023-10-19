from random import randint
from ansi_codes import txt,get_list_of_colours_fg,icons
# Genders of all enemies are male right now, but later it will be randomised for extra detail
# Currently, only the Monster has random pre-attack talking lines depending on mental states. This will be extended to all enemies soon but im lazy rn whoops!
# Fort and Ego checks because later there will be additional dialogue for scenarios like high ego and low fortitude and etc. 

class Monster:
    # Construction
    def __init__(self,colour,adj):
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
        self.resists = [["smash",0],["pierce",0],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "monster"
        self.hitPoints = 10
        self.maxDamage = 5
        self.attackMessage = monsterMessageBank[randint(0, len(monsterMessageBank) - 1)]
        self.gold = randint(6,9)
        self.mentalFortitude = randint(0,100)
        self.ego = randint(0,100)

    # Getters
    def get_adj(self):
        return self.adj

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

    def getCode(self):
        return self.colourcode

    def getResists(self):
        return self.resists

    # Methods
    def attack(self): # Defines monster attack behaviour and returns the damage inflicted.
        damage = randint(0,self.maxDamage)
        if damage == 0:
            print("You successfully dodge the blow!")
        elif damage == 1:
            print("A glancing blow! You take 1 {}.".format(icons.heart))
        else:
            print(self.attackMessage + " You take "
                  + str(damage) + " {}.".format(icons.heart))
        return damage

    def receive_damage(self,damage,damagetype): # Subtracts damage from the monster and prints out related message.
        for loop in self.resists:
            if loop[0] == damagetype:
                damage -= loop[1]
        if damage <= 0:
            damage = 0
            print("Miss! The " + self.colourcode + self.species + "{} is too fast for you.".format(txt.sty.reset))
        elif damage == 1:
            print("You strike a glancing blow for 1 point of damage.")
        else:
            print("The " + self.colourcode + self.species + "{} takes ".format(txt.sty.reset) + str(damage)
                  + " {}.".format(icons.heart))
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
            print('The Monster says: {}"{}"{}'.format(self.colourcode,highFortandEgo[randint(0, len(highFortandEgo) - 1)],txt.sty.reset))# This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Monster says: {}"{}"{}'.format(self.colourcode,normalMonster[randint(0, len(normalMonster) - 1)],txt.sty.reset)) # This will be changed later depending on the Mental Fortitude and Ego attribute!!

class Goblin(Monster):
    # Construction
    def __init__(self,colour,adj):
        goblinMessageBank = [
            'He vocalises menacingly!',
            'He starts spinning around in a frightening manner!',
            'He swings his Scimitar!',
            'He fires a shot from his Shortbow!',
            'He bites your knees!',
            'He headbutts your calves!'
            'He scratches your feet!',
            'He jumps and punches your nipples!',
            'He beats your shins!',
            'He fires a falafaluten!'
        ]
        self.resists = [["smash",0],["pierce",0],["slash",2]]
        self.adj = adj
        self.colourcode = colour
        self.species = "goblin"
        self.hitPoints = 12
        self.maxDamage = 6
        self.attackMessage = goblinMessageBank[randint(0, len(goblinMessageBank) - 1)]
        self.gold = randint(6,18)
        self.mentalFortitude = randint(0,100)
        self.ego = randint(0,100)
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
            print('The Goblin says: {}"{}"{}'.format(self.colourcode,highFortandEgo[randint(0, len(highFortandEgo) - 1)],txt.sty.reset))# This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Goblin says: {}"{}"{}'.format(self.colourcode,normalMonster[randint(0, len(normalMonster) - 1)],txt.sty.reset)) # This will be changed later depending on the Mental Fortitude and Ego attribute!!

class Vampire(Monster):

    # Construction
    def __init__(self,colour,adj):
        vampireMessageBank = [
            'He shrieks grievously!',
            'He flashes his teeth!',
            'He sinks his fangs into your neck!',
            'He munches at your ears!',
            'He bites at your face!',
            'He chomps at your torso!'
            'He swings his rapier!!',
            'He bashes you with his mace!',
            'He sweeps you off your feet!',
            'He glares at you with evil eyes, filling you with terror.'
        ]
        self.resists = [["smash",0],["pierce",4],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "vampire"
        self.hitPoints = 20
        self.maxDamage = 7
        self.attackMessage = vampireMessageBank[randint(0, len(vampireMessageBank) - 1)]
        self.gold = randint(5,15)
        self.mentalFortitude = randint(0,100)
        self.ego = randint(0,100)

    # Methods
    def talk(self):

        highFortandEgo = ["En guarde, warrior!", 
                          'Quiver at my elegance!',
                          "Do me a favour, and try not to die so early :)",
                          'Finally, some action!',
                          "I've been looking for a challenge.",
                          'Another head to add to my collection!',
                          'Your skin would look so beautiful as my rug.',
                          "This may hurt a little",
                          "I'll try not to play with your corpse too much.",
                          'Ooooh, another scalp to add to my wall. How lucky!',
                          "I'll slit your throat and drink the sweet nectar that pours out!",
                          'Try not to get too much blood on me, I have a wedding to attend after this',
                          "Finally, something to cure my boredom!",
                          'Can we hurry this up? I have a ritual to make an appearence at.'
        ]

        normalMonster = ['SNARRLLLLLL!!',
                         "HIIIISSSSSSSSS!!!",
                         "I LOVE BLOOD!",
                         "I'LL CARVE MY NAME IN YOUR FLESH!",
                         "I'M GOING TO DESTROY YOU, MEATSACK!",
                         "SATAN, ACCEPT THIS OFFERING!",
                         "I'LL BATHE IN YOUR ENTRAILS!",
                         "I'LL SKIN YOU ALIVE.",
                         'BLOOD BLOOD BLOOD BLOOD BLOOOOOOOOOOOOOOD!!!!',
                         "GRRRRRRAHHHHHH!",
                         "I'LL PLUCK YOUR EYES OUT!",
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
            print('The Vampire says: {}"{}"{}'.format(self.colourcode,highFortandEgo[randint(0, len(highFortandEgo) - 1)],txt.sty.reset))# This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Vampire says: {}"{}"{}'.format(self.colourcode,normalMonster[randint(0, len(normalMonster) - 1)],txt.sty.reset)) # This will be changed later depending on the Mental Fortitude and Ego attribute!!


class Slime(Monster):

    # Construction
    def __init__(self,colour,adj):
        slimeMessageBank = [
            'He spews gooey liquid at you!',
            'He jumps at you!',
            'He traps you in his slime!',
            'He cries "waka waka whaaat" and englufs you!',
            'He grips you with his sticky liquid!',
            'He swallows you whole and spits you back out!'
            'He squishes you underneath his slimy weight!',
            'He traps you under his folds, rendering you unable to breathe!',
            'He slips you off your feet with his slime trail!',
            'His sticky substance burns your soul!'
        ]
        self.resists = [["smash",5],["pierce",0],["slash",0]]
        self.adj = adj
        self.colourcode = colour
        self.species = "slime"
        self.hitPoints = 8
        self.maxDamage = 4
        self.attackMessage = slimeMessageBank[randint(0, len(slimeMessageBank) - 1)]
        self.gold = randint(2,9)
        self.mentalFortitude = randint(0,100)
        self.ego = randint(0,100)

    # Methods
        highFortandEgo = ["Hey! Get a move on!", 
                          "I'm boinging here!",
                          "I'm going to slam you into outer space!",
                          'Look upon my stickiness, and despair!',
                          "Wait until I whip out the slime sword!.",
                          'Wait until I hit you with a slimecicle!',
                          'Goo Powers, ACTIVATE!',
                          "I'm gonna slime you up and down!",
                          "Wait until you see my slime whip!",
                          "I'm going to use my special goo-fusion attack if you're not careful!",
                          "I'm going to cover your organs in goo!",
                          "I can't wait to see you collapse under my folds!",
                          "I'm as bored as a slime in a sentient rock convention!",
                          "You're not ready to fight a gelatinous cube."
        ]

        normalMonster = ['BOOOIIINNNGGG!!',
                         "BOING!",
                         "BOING BOING BOING!",
                         "blub blurp",
                         "blup bluuup",
                         "bluurrp blurp",
                         "BLURPPPPPPPPPP BLORP",
                         "BLAHHHHHHGH.",
                         'BLURP BLURP BOING!',
                         "BLOBBBOB!",
                         "BlibbleBlobble!",
                         'EEEEEEEEEEEEEEEEEEEEEEEEEE!!',
                         'BLAGHBLAHBLAGH!!'
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
            print('The slime says: {}"{}"{}'.format(self.colourcode,highFortandEgo[randint(0, len(highFortandEgo) - 1)],txt.sty.reset))# This will be changed later depending on the Mental Fortitude and Ego attribute!!
        else:
            print('The Vampire says: {}"{}"{}'.format(self.colourcode,normalMonster[randint(0, len(normalMonster) - 1)],txt.sty.reset)) # This will be changed later depending on the Mental Fortitude and Ego attribute!!

class RogueWarrior(Monster):

    # Construction
    def __init__(self,colour,adj):
        self.resists = [["smash",4],["pierce",2],["slash",3]]
        self.adj = adj
        self.colourcode = colour
        self.species = "rogue warrior"
        self.hitPoints = 25
        self.maxDamage = 6
        self.attackMessage = "They slash at you."
        self.gold = randint(12,27)
        self.mentalFortitude = randint(0,100)
        self.ego = randint(0,100)

    # Methods
    def talk(self):
        print("{}I'll kill you!{}".format(self.colourcode,txt.sty.reset))
