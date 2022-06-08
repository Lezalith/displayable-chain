init -30 python:

    # For damage and hit calculations.
    from random import randrange

    # Represents a spell ability.
    class Spell():

        # name is a string.
        # animationChain is AnimationChain object.
        # damage is a tuple of two ints representing the damage range: (min damage, max damage)
        # mpCost is the cost of MP to use this spell.
        def __init__(self, name, animationChain, castChain, damage, mpCost = 0):

            # Name of the Spell.
            self.name = name

            # Chain used by the Character to cast the spell.
            self.castAnimationChain = castChain

            # AnimationChain of the Spell.
            self.animationChain = animationChain

            # Spell stats
            self.damage = [ int(damage[0]), int(damage[1]) ]
            self.mpCost = int(mpCost)

            # Yet to be implemented.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

            # Instance info - Info of a spell when it is used.
            # The Character that began the spell.
            self.attacker = None 
            # The Character that is under spell.
            self.defender = None

        # Returns damage dealt, calculated from this spell's stats.
        def getDamage(self):

            return randrange( self.damage[0], self.damage[1] )

        # Return the spell's AnimationChain.
        def getChain(self):
            return self.animationChain

        def setInstanceInfo(self, attacker, defender):

            self.attacker = attacker
            self.defender = defender

        def spellUsed(self, attacker, defender):

            self.setInstanceInfo(attacker, defender)

### (Defined in script.rpy) ###