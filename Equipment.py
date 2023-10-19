class Armour:
    def __init__(self):
        self.inspectMessage = "ignore this"
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0

    def inspect(self):
        return self.inspectMessage

    def protect_proj(self,damage):
        return damage - self.projProt

    def protect_slash(self,damage):
        return damage - self.slashProt

    def protect_pierce(self,damage):
        return damage - self.pierceProt

    def get_type(self):
        return "equipment"

    def use(self,hero,inv):
        inv.swap_equipment([self,1])
        inv.destroy_general_item([self,1])

class Helmet(Armour):
    def __init__(self):
        self.name = "blank helmet"
        self.description = "how did you get this"
        self.inspectMessage = "a helmet made of nothing. you've broken the game if you've managed to get this."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0

    def get_equipment_type(self):
        return "head"

class MailHood(Helmet):
    def __init__(self):
        self.name = "mail hood"
        self.description = "A hood made of chainmail."
        self.inspectMessage = "A simple hood made of chain links. Will protect from slashes, not so much arrows or stabs."
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1

class Hat(Helmet):
    def __init__(self):
        self.name = "hat"
        self.description = "Will protect your head from the rain."
        self.inspectMessage = "A cloth hat. Provides no aid in the midst of battle."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0