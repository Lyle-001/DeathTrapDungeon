class Armour:
    def __init__(self):
        self.inspectMessage = "ignore this"
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

    def inspect(self):
        return self.inspectMessage

    def protect_proj(self,damage):
        return damage - self.projProt

    def protect_slash(self,damage):
        return damage - self.slashProt

    def protect_pierce(self,damage):
        return damage - self.pierceProt

    def protect_smash(self,damage):
        return damage - self.smashProt

    def get_type(self):
        return "equipment"

    def use(self,hero,inv):
        if inv.swap_equipment([self,1]):
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
        self.smashProt = 0

    def get_equipment_type(self):
        return "head"

class Torso(Armour):
    def __init__(self):
        self.name = "blank torso piece"
        self.description = "how did you get this"
        self.inspectMessage = "a torso piece made of nothing. you've broken the game if you've managed to get this."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

    def get_equipment_type(self):
        return "torso"

class Hands(Armour):
    def __init__(self):
        self.name = "blank hands piece"
        self.description = "how did you get this"
        self.inspectMessage = "a pair of gloves made of nothing. you've broken the game if you've managed to get this."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

    def get_equipment_type(self):
        return "hands"

class Legs(Armour):
    def __init__(self):
        self.name = "blank legs piece"
        self.description = "how did you get this"
        self.inspectMessage = "a pair of leggings made of nothing. you've broken the game if you've managed to get this."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

    def get_equipment_type(self):
        return "legs"

class Feet(Armour):
    def __init__(self):
        self.name = "blank feet piece"
        self.description = "how did you get this"
        self.inspectMessage = "a pair of shoes made of nothing. you've broken the game if you've managed to get this."
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

    def get_equipment_type(self):
        return "feet"






class MailHood(Helmet):
    def __init__(self):
        self.name = "mail hood"
        self.description = "A hood made of chainmail."
        self.inspectMessage = "A simple hood made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1

class MailHauberk(Torso):
    def __init__(self):
        self.name = "mail tauberk"
        self.description = "A shirt made of chainmail."
        self.inspectMessage = "A simple shirt made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1

class MailGloves(Hands):
    def __init__(self):
        self.name = "mail gloves"
        self.description = "A pair of gloves made of chainmail."
        self.inspectMessage = "A pair of gloves made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1

class MailChausse(Legs):
    def __init__(self):
        self.name = "mail chausse"
        self.description = "mail chausse"
        self.inspectMessage = "mail chausse"
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1

class MailBoots(Feet):
    def __init__(self):
        self.name = "mail boots"
        self.description = "mail boots"
        self.inspectMessage = "mail boots"
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1

class LeatherGauntlets(Hands):
    def __init__(self):
        self.name = "leather gloves"
        self.description = "leather gloves"
        self.inspectMessage = "leather gloves"
        self.value = 1
        self.armour = 1
        self.projProt = 0
        self.slashProt = 3
        self.pierceProt = 0
        self.smashProt = 2

class LeatherShoes(Feet):
    def __init__(self):
        self.name = "leather shoes"
        self.description = "leather shoes"
        self.inspectMessage = "leather shoes"
        self.value = 1
        self.armour = 1
        self.projProt = 0
        self.slashProt = 3
        self.pierceProt = 0
        self.smashProt = 2

class WoolGambeson(Torso):
    def __init__(self):
        self.name = "gambeson"
        self.description = "A thick shirt made of wool. Pairs well with chainmail."
        self.inspectMessage = "A bulky and heavy wool shirt. Helps protect from stabs or smashes."
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 1
        self.pierceProt = 4
        self.smashProt = 4

class ClothHat(Helmet):
    def __init__(self):
        self.name = "hat"
        self.description = "Will protect your head from the rain."
        self.inspectMessage = "A cloth hat. Provides no aid in the midst of battle."
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

class ClothShirt(Torso):
    def __init__(self):
        self.name = "shirt"
        self.description = "A simple beggar's shirt."
        self.inspectMessage = "A cloth shirt. Provides no aid in the midst of battle."
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

class ClothGloves(Hands):
    def __init__(self):
        self.name = "gloves"
        self.description = "gloves"
        self.inspectMessage = "gloves"
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

class ClothTrousers(Legs):
    def __init__(self):
        self.name = "trousers"
        self.description = "trousers"
        self.inspectMessage = "trousers"
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

class ClothCloths(Feet):
    def __init__(self):
        self.name = "cloths"
        self.description = "cloths"
        self.inspectMessage = "cloths"
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0

class SteelHelm(Helmet):
    def __init__(self):
        self.name = "steel helm"
        self.description = "A helm made of steel."
        self.inspectMessage = "An ornate helmet made of steel. Will protect from slashes or smashes, not so much arrows or stabs."
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4

class SteelBreastplate(Torso):
    def __init__(self):
        self.name = "steel breastplate"
        self.description = "a breastplate made of steel."
        self.inspectMessage = "i cant be bothered to make up these messages anymore someone else do it please."
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4

class SteelGauntlets(Hands):
    def __init__(self):
        self.name = "steel gauntlets"
        self.description = "steel gauntlets"
        self.inspectMessage = "steel gauntlets"
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4

class SteelGreaves(Legs):
    def __init__(self):
        self.name = "steel greeves"
        self.description = "steel greeves"
        self.inspectMessage = "steel greeves"
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4

class SteelSabatons(Feet):
    def __init__(self):
        self.name = "steel sabatons"
        self.description = "steel sabatons"
        self.inspectMessage = "steel sabatons"
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4