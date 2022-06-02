init -30 python:

    from random import randrange

    class Attack():

        def __init__(self, name, animationChain, damage, apCost = 0):

            # Name of the Attack.
            self.name = name

            # AnimationChain of the Attack.
            self.animationChain = animationChain

            # Attack stats
            self.damage = damage
            self.apCost = apCost
            self.damage = [ int(damage[0]), int(damage[1]) ]

            # Prepared for the future.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

        def getDamage(self):

            return randrange( self.damage[0], self.damage[1] )

### (Defined in script.rpy) ###