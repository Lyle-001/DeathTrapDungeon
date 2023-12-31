from ansi_codes import txt,clearscreen
class Armour:
    def __init__(self):
        pass

    def get_name(self):
        return self.name

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
        if inv.add_item(self,"equipment"):
            inv.delete_item(self,1,"general")
            clearscreen()
            print("{}Successfully equipped!{}".format(txt.col.fg.nml.yellow,txt.sty.reset))

class Helmet(Armour):
    def __init__(self):
        pass
    def get_tags(self=None):
        return ["armour","head","shopExclusive"]

    def get_equipment_type(self):
        return "head"

class Torso(Armour):
    def __init__(self):
        pass
    def get_tags(self=None):
        return ["armour","torso","shopExclusive"]

    def get_equipment_type(self):
        return "torso"

class Hands(Armour):
    def __init__(self):
        pass
    def get_tags(self=None):
        return ["armour","hands","shopExclusive"]

    def get_equipment_type(self):
        return "hands"

class Legs(Armour):
    def __init__(self):
        pass
    def get_tags(self=None):
        return ["armour","legs","shopExclusive"]

    def get_equipment_type(self):
        return "legs"

class Feet(Armour):
    def __init__(self):
        pass
    def get_tags(self=None):
        return ["armour","feet","shopExclusive"]

    def get_equipment_type(self):
        return "feet"

################################
#### Actual equipment pieces ###
################################


class MailHood(Helmet):
    def __init__(self):
        self.name = "mail hood"
        self.description = "A hood made of chainmail."
        self.inspectMessage = "A simple hood made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1
    def get_tags(self=None):
        return ["armour","head","mail","shopExclusive","blacksmithSellable"]

class MailHauberk(Torso):
    def __init__(self):
        self.name = "mail tauberk"
        self.description = "A shirt made of chainmail."
        self.inspectMessage = "A simple shirt made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1
    def get_tags(self=None):
        return ["armour","torso","mail","shopExclusive","blacksmithSellable"]

class MailGloves(Hands):
    def __init__(self):
        self.name = "mail gloves"
        self.description = "A pair of gloves made of chainmail."
        self.inspectMessage = "A pair of gloves made of chain links. Will protect from slashes, not so much arrows, smashes or stabs."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1
    def get_tags(self=None):
        return ["armour","hands","mail","shopExclusive","blacksmithSellable"]

class MailChausse(Legs):
    def __init__(self):
        self.name = "mail chausse"
        self.description = "Leg armour of mobile linked chains."
        self.inspectMessage = "Agile and protected, the best of both worlds! At least when it comes to slashes, these aren't good for much else."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1
    def get_tags(self=None):
        return ["armour","legs","mail","shopExclusive","blacksmithSellable"]

class MailBoots(Feet):
    def __init__(self):
        self.name = "mail boots"
        self.description = "Mail boots built around a leather sole."
        self.inspectMessage = "Best hope the leather doesn't stain. Handy for slashes and not much else."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 4
        self.pierceProt = 1
        self.smashProt = 1
    def get_tags(self=None):
        return ["armour","feet","mail","shopExclusive","blacksmithSellable"]

class LeatherGauntlets(Hands):
    def __init__(self):
        self.name = "leather gloves"
        self.description = "A pair of leather gloves."
        self.inspectMessage = "Decent for the cold, or for committing crimes. That and some smashing or slashing done to you."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 0
        self.slashProt = 2
        self.pierceProt = 0
        self.smashProt = 3
    def get_tags(self=None):
        return ["armour","hands","leather","clotherSellable","shopExclusive"]

class LeatherShoes(Feet):
    def __init__(self):
        self.name = "leather shoes"
        self.description = "Some real leather shoes."
        self.inspectMessage = "The day for foot protection has come, sans trench foot! Useful for blunt blows and some slashes."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 0
        self.slashProt = 2
        self.pierceProt = 0
        self.smashProt = 3
    def get_tags(self=None):
        return ["armour","feet","leather","clothierSellable","shopExclusive"]

class WoolGambeson(Torso):
    def __init__(self):
        self.name = "gambeson"
        self.description = "A thick shirt made of wool. Pairs well with chainmail."
        self.inspectMessage = "A bulky and heavy wool shirt. Helps protect from stabs or smashes."
        self.maxStack = 1
        self.value = 1
        self.armour = 1
        self.projProt = 1
        self.slashProt = 1
        self.pierceProt = 4
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","torso","wool","clotherSellable","shopExclusive"]

class ClothHat(Helmet):
    def __init__(self):
        self.name = "hat"
        self.description = "Headwear from tailored cloth."
        self.inspectMessage = "It's useless for defence, but you'll look good while bleeding out!"
        self.maxStack = 1
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0
    def get_tags(self=None):
        return ["armour","head","cloth","clothierSellable","shopExclusive"]

class ClothShirt(Torso):
    def __init__(self):
        self.name = "shirt"
        self.description = "A simple beggar's shirt."
        self.inspectMessage = "A cloth shirt. Provides no aid in the midst of battle."
        self.maxStack = 1
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0
    def get_tags(self=None):
        return ["armour","torso","cloth","clothierSellable","shopExclusive"]

class ClothGloves(Hands):
    def __init__(self):
        self.name = "gloves"
        self.description = "A comfy pair of gloves."
        self.inspectMessage = "They'll help against the cold, I guess. Not any attacks though. Fit like a- hang on..."
        self.maxStack = 1
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0
    def get_tags(self=None):
        return ["armour","hands","cloth","clothierSellable","shopExclusive"]

class ClothTrousers(Legs):
    def __init__(self):
        self.name = "trousers"
        self.description = "Some nicely fitting trousers."
        self.inspectMessage = "Hey, there's some change in here! Actually, it's just a button. Could've afforded some actual protection instead of these."
        self.maxStack = 1
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0
    def get_tags(self=None):
        return ["armour","legs","cloth","clothierSellable","shopExclusive"]

class ClothCloths(Feet):
    def __init__(self):
        self.name = "cloths"
        self.description = "Shoes for those who can't afford shoes."
        self.inspectMessage = "One day these'll protect your feet. Or give you trench foot. There's not much protection today though."
        self.maxStack = 1
        self.value = 1
        self.armour = 0
        self.projProt = 0
        self.slashProt = 0
        self.pierceProt = 0
        self.smashProt = 0
    def get_tags(self=None):
        return ["armour","feet","cloth","clothierSellable","shopExclusive"]

class SteelHelm(Helmet):
    def __init__(self):
        self.name = "steel helm"
        self.description = "A helm made of steel."
        self.inspectMessage = "An ornate helmet made of steel. Will protect from slashes or smashes, not so much arrows or stabs."
        self.maxStack = 1
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","head","steel","shopExclusive","blacksmithSellable"]

class SteelBreastplate(Torso):
    def __init__(self):
        self.name = "steel breastplate"
        self.description = "A breastplate made of steel."
        self.inspectMessage = "A well crafted steel breastplate. Useful against blades and blows, but not so much points or projectiles."
        self.maxStack = 1
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","torso","steel","shopExclusive","blacksmithSellable"]

class SteelGauntlets(Hands):
    def __init__(self):
        self.name = "steel gauntlets"
        self.description = "A pair of steel gauntlets."
        self.inspectMessage = "These will definitely help with the cold! And even blade strokes and blunt strikes!"
        self.maxStack = 1
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","hands","steel","shopExclusive","blacksmithSellable"]

class SteelGreaves(Legs):
    def __init__(self):
        self.name = "steel greaves"
        self.description = "Steel armour for your shins."
        self.inspectMessage = "Shinpads made for proper footie! Handy for tackles- I mean blunts strikes and slashes."
        self.maxStack = 1
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","legs","steel","shopExclusive","blacksmithSellable"]

class SteelSabatons(Feet):
    def __init__(self):
        self.name = "steel sabatons"
        self.description = "Steel-forged boots."
        self.inspectMessage = "Good for stomping on things really hard. And for protecting against slashes and smashes."
        self.maxStack = 1
        self.value = 1
        self.armour = 2
        self.projProt = 2
        self.slashProt = 5
        self.pierceProt = 2
        self.smashProt = 4
    def get_tags(self=None):
        return ["armour","feet","steel","shopExclusive","blacksmithSellable"]




equipmentList = [MailHood,MailHauberk,MailGloves,MailChausse,MailBoots,
                 LeatherGauntlets,LeatherShoes,
                 WoolGambeson,
                 ClothHat,ClothShirt,ClothGloves,ClothTrousers,ClothCloths,
                 SteelHelm,SteelBreastplate,SteelGauntlets,SteelGreaves,SteelSabatons]