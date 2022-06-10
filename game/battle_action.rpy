init -40 python:

    # For damage and hit calculations.
    from random import randrange

    # Was supposed to be a parentclass of Attack and Spell, but ended up representing them both.
    class BattleAction():

        # name is a string.
        # animationChain is AnimationChain object.
        # damage is a tuple of two ints representing the damage range: (min damage, max damage)
        # type is a string of either "attack" or "spell"
        # apCost is int, the cost of AP to use this attack.
        # mpCost is int, the cost of MP to use this attack.
        # hpCost is int, the cost of HP to use this attack.
        # associatedChain - if type is "spell", the AnimationChain of the spell used in BattleCharacter.spellCast
        # TODO: associatedChain for "attack"s could be a second version/animation of the same attack. A function here would need to check that, like a critical hit.
        def __init__(self, name, animationChain, damage, type, apCost = 0, mpCost = 0, hpCost = 0, associatedChain = None):

            # Non self-explanatory vars marked by "#*" are explained in __init__ arguments.

            # Basic info about the BattleAction.
            self.name = name
            self.type = type
            self.mpCost = int(mpCost)
            self.apCost = int(apCost)
            self.hpCost = int(hpCost)

            # Attack stats
            self.damage = [ int(damage[0]), int(damage[1]) ]

            # Yet to be implemented.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None

            # AnimationChain of the Attack.
            self.animationChain = animationChain #*
            # AnimationChain of the spell cast.
            self.associatedChain = associatedChain #*

            # Instance info - Info of an attack when it is used. 
            # TODO: Make instanceInfo into one var, a dict maybe?
            # The Character that began the attack.
            self.attacker = None 
            # The Character that is under attack.
            self.defender = None

        # Returns damage dealt, calculated from this attack's stats.
        def getDamage(self):

            # Random number between minimal damage and maximum damage.
            return randrange( self.damage[0], self.damage[1] )

        # Return the attack's AnimationChain.
        def getChain(self):
            return self.animationChain

        # Sets instance info.
        def setInstanceInfo(self, attacker, defender):

            self.attacker = attacker
            self.defender = defender

        # Called right before the Action is used. 
        def actionUsed(self, attacker, defender):

            # Sets instance info.
            self.setInstanceInfo(attacker, defender)

        # Returns the associated chain (explained in __init__).
        def getAssociatedChain(self):
            return self.associatedChain
