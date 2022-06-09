init -40 python:

    # For damage and hit calculations.
    from random import randrange

    # Was supposed to be a parentclass of Attack and Spell, but ended up representing them both.
    class BattleAction():

        # name is a string.
        # animationChain is AnimationChain object.
        # damage is a tuple of two ints representing the damage range: (min damage, max damage)
        # apCost is int, the cost of AP to use this attack.
        # mpCost is int, the cost of MP to use this attack.
        # associatedChain - castChain of Spell class
        def __init__(self, name, animationChain, damage, apCost = 0, mpCost = 0, associatedChain = None):

            # Basic info about the BattleAction.
            self.name = name
            self.mpCost = int(mpCost)
            self.apCost = int(apCost)

            # Yet to be implemented.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

            # Attack stats
            self.damage = [ int(damage[0]), int(damage[1]) ]

            # AnimationChain of the Attack.
            self.animationChain = animationChain
            # AnimationChain of the spell cast.
            self.associatedChain = associatedChain

            # Instance info - Info of an attack when it is used.
            # The Character that began the attack.
            self.attacker = None 
            # The Character that is under attack.
            self.defender = None

        # Returns damage dealt, calculated from this attack's stats.
        def getDamage(self):

            return randrange( self.damage[0], self.damage[1] )

        # Return the attack's AnimationChain.
        def getChain(self):
            return self.animationChain

        def setInstanceInfo(self, attacker, defender):

            self.attacker = attacker
            self.defender = defender

        def actionUsed(self, attacker, defender):

            self.setInstanceInfo(attacker, defender)

        def getAssociatedChain(self):
            return self.associatedChain
