from random import randint

class Hero():
    def __init__(self,name):
        self.name = name
        self.className = "Hero"
        self.originalHPs = randint(20,30)
        self.currentHPs = self.originalHPs
        self.maxDamage = 6
        self.gold = 0

    # Getters
    def get_name(self):
        return self.name

    def getCurrentHPs(self):
        return self.currentHPs

    def getGold(self):
        return self.gold

    def get_class(self):
        return self.className

    # Setters
    def setGold(self,gold):
        self.gold += gold

    def setMaxDamage(self,damage):
        self.maxDamage += damage

    def set_max_health(self,health):
        self.originalHPs = health
        self.currentHPs = health

    # Methods
    def attack(self): # Returns the amount of damage inflicted
        damage = randint(0,self.maxDamage)
        return damage

    def receiveDamage(self,damage): # Subtracts damage from the hero
        self.currentHPs -= damage

    def purchase(self,cost): # Allows purchase of shop items if enough gold
        if cost <= self.gold:
            self.gold -= cost
            return True
        else:
            return False

    def heal(self,health):
        if health + self.currentHPs <= self.originalHPs: # Hero can't go over original HPs
            self.currentHPs += health
        else:
            self.currentHPs = self.originalHPs
        
class Barbarian(Hero):
    def __init__(self,name):
        self.name = name
        self.className = "Barbarian"
        self.originalHPs = randint(20,30)
        self.currentHPs = self.originalHPs
        self.maxDamage = 8
        self.gold = 0

class Wizard(Hero):
    def __init__(self,name):
        self.name = name
        self.className = "Wizard"
        self.originalHPs = randint(15,25)
        self.currentHPs = self.originalHPs
        self.maxDamage = 12
        self.gold = 0

class Warlock(Hero):
    def __init__(self,name):
        self.name = name
        self.className = "Warlock"
        self.originalHPs = randint(17,27)
        self.currentHPs = self.originalHPs
        self.maxDamage = 10
        self.gold = 0
