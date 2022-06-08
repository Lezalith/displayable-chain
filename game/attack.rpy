init -30 python:

    # For damage and hit calculations.
    from random import randrange

    # Represents an attack ability.
    class Attack():

        # name is a string.
        # animationChain is AnimationChain object.
        # damage is a tuple of two ints representing the damage range: (min damage, max damage)
        # apCost is the cost of AP to use this attack.
        def __init__(self, name, animationChain, damage, apCost = 0):

            # Name of the Attack.
            self.name = name

            # AnimationChain of the Attack.
            self.animationChain = animationChain

            # Attack stats
            self.damage = [ int(damage[0]), int(damage[1]) ]
            self.apCost = int(apCost)

            # Yet to be implemented.
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

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

        def attackUsed(self, attacker, defender):

            self.setInstanceInfo(attacker, defender)

### (Defined in script.rpy) ###