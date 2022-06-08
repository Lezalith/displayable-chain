init -30 python:

    from random import randrange

    class Spell():

        def __init__(self, name, animationChain, damage, mpCost = 0):

            self.name = name
            self.animationChain = animationChain

            # Attack stats
            self.damage = [ int(damage[0]), int(damage[1]) ]
            self.mpCost = int(mpCost)

            # Prepared for the future.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

        def getDamage(self):

            return randrange( self.damage[0], self.damage[1] )