import random

# Make sure to program durability and a gun into the game

class Monster:
    def _init_(self, colour): # Make sure to add a Mental Fortitude attribute and ego attribute
        messageBank = [
            'It stabs you with its knife-like talons!',
            'It catches you by surprise and tenderises you with its massive club!',
            'It beats you up like a bully!',
            'It hurts you emotionally by saying mean things :(',
            'It lightly scrapes you with its 18 foot long fangs.',
            'It reminds you of your traumatising childhood and laughs at you :('
            'It touches you inappropriately.',
            'Its scary aura engulfs you!!',
            'It whispers "scuderia" in your ear, shocking you to the bone.'
                    ]
        self.colour = colour
        self.species = 'Monster'
        self.healthPoints = random.randint(1,15)
        self.maxDamage = 15
        self.attackMessage = messageBank[random.randint(0, len(messageBank) - 1)]
        self.mentalFortitude = random.randint(0,100)
        self.ego = random.randint(0,100)

        # Getters
        
    def getHealthPoints(self):
        return self.healthPoints

    def getSpecies(self):
        return self.species

    def getColour(self):
        return self.species

    def getFortitude(self):
        return self.mentalFortitude

    def getEgo(self):
        return self.ego
        
        # Setters
        
    def monsterCry(self):
        highFortandEgo = ['May the best man win.', #Additional logic will be completed later, im lazy rn#
                          'En garde!',
                          'Show me you can fight, heathen!',
                          'Father, I will make you proud!',
                          'This is for my family',
                          'I will give you the honour of a swift death.',
                          'I promised my family I would get them food.',
                          "I'm sorry about this.",
                          'I will give you the honour of a respectable death.',
                          'STAND AND FIGHT, HUMAN!'
                          ]

        normalMonster = ['ROOOOAR',
                         'YOUR TIME ENDS NOW',
                         "I'M GOING TO SKIN YOU ALIVE",
                         'AFTER THIS I AM GOING FOR YOUR FAMILY',
                         "YOU'RE GOING TO TASTE SO DELICIOUS!",
                         "I'M GOING TO USE YOUR BLOOD FOR THE CHILLI COOK OFF NEXT WEEK!"
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

    def recieveDamage(self,damage):
        if damage == 0:
            print(f"Missed! {self.species} is too quick with it!")
        else:
            print(f"The {self.species} took an absolutely gargantuan {damage} points of damage from you.")
        self.healthPoints -= damage

    def attack(self):
        damage = random.randint(0, self.maxDamage)
        if damage == 0:
            print('The monster deals 0 damage to you! What a loser lmao')
        else:
            print(self.attackMessage)
            print(f"You recieve {damage} points of damage!")
        return damage
