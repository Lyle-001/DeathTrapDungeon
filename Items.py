from random import randint

class DilutedHealingElixir:
    def __init__(self):
        self.name = "Diluted Healing Elixir"
        self.description = "Heals small wounds."
        self.inspect = "This vial contains a semi-red liquid. There are a few glittery particles inside."
        self.value = 4
        self.healingPower = [3,7]

    def get_value(self):
        return self.value

    def inspect(self):
        return self.inspect

    def use(self,hero):
        hero.heal(randint(self.healingPower[0],self.healingPower[1]))