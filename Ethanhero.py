import random

class Hero():
    def __init__(self, Name):
        self.name = Name
        self.maxHP = random.randint(20,30)
        self.currHP = self.maxHP
        self.maxDamage = 6
        self.minDamage = 0
        self.gold = 0
        self.items = []
        
    def getName(self):
        return self.name

    def getHP(self):
        return self.currHP

    def getGold(self):
        return self.gold

    def setGold(self, gold):
        self.gold += gold
        
    def attack(self):
        damage = random.randint(self.minDamage,self.maxDamage)
        if damage < 0:
            damage = 0
        return damage

    def receiveDamage(self,damage):
        self.currHP -= damage

    def getClass(self):
        return self.char

    def purchase(self, cost):
        if cost <= self.gold:
            self.gold -= cost
            return True
        else:
            return False

    def heal(self, healing):
        if healing + self.currHP <= self.maxHP:
            self.currHP += healing
        else:
            self.currHP = self.maxHP

    def getItems(self):
        return self.items

    def gainItem(self, item):
        self.items.append(item)

    def gainMaxH(self, gain):
        self.maxHP += gain

    def gainMaxD(self, gain):
        self.maxDamage += gain

    def gainMinD(self, gain):
        self.minDamage += gain
            
        
class Archer(Hero):
    def __init__(self,Name):
        self.name = Name + ", the Deadeye"
        self.maxHP = random.randint(10,20)
        self.currHP = self.maxHP
        self.maxDamage = 15
        self.minDamage = -3
        self.char = "ar"
        self.gold = 0
        self.miss = "Your arrow falls short, missing them entirely."
        self.glance = "Your arrow only hits their foot, before falling out. 1 damage."
        self.hit = "Flying straight and true, your arrow perfectly hits their centre of mass."
        self.items = []

class WPriest(Hero):
    def __init__(self,Name):
        self.name = Name + ", the Blessed"
        self.maxHP = random.randint(30,40)
        self.currHP = self.maxHP
        self.maxDamage = 7
        self.minDamage = -1
        self.char = "wp"
        self.gold = 0
        self.miss = "Your blow misses, as you fervently whisper a prayer."
        self.glance = "Your mace strikes their arm, but your god is not happy with your prayers. 1 damage."
        self.hit = "Your divine righteousness manifests in raw strength, crashing down on them with the power of your god."
        self.items = []

class Warlock(Hero):
    def __init__(self,Name):
        self.name = Name + ", the Scourge"
        self.maxHP = random.randint(20,30)
        self.currHP = self.maxHP
        self.maxDamage = 5
        self.minDamage = 3
        self.char = "wa"
        self.gold = 0
        self.items = []

class Fool(Hero):
    def __init__(self,Name):
        self.name = Name + ", the Foolish"
        self.maxHP = random.randint(1,5)
        self.currHP = self.maxHP
        self.maxDamage = 1
        self.minDamage = 0
        self.char = "fo"
        self.gold = 0
        self.items = []
