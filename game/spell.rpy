init -30 python:

    # For damage and hit calculations.
    from random import randrange

    # Represents a spell ability.
    class Spell():

        # name is a string.
        # animationChain is AnimationChain object.
        # damage is a tuple of two ints representing the damage range: (min damage, max damage)
        # mpCost is the cost of MP to use this spell.
        def __init__(self, name, animationChain, damage, mpCost = 0):

            # Name of the Spell.
            self.name = name

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

        # Returns damage dealt, calculated from this spell's stats.
        def getDamage(self):

            return randrange( self.damage[0], self.damage[1] )
            
### (Defined in script.rpy) ###