init -30 python:

    class Attack():

        def __init__(self, name, animationChain):

            # Name of the Attack.
            self.name = name

            # AnimationChain of the Attack.
            self.animationChain = animationChain

            # Prepared for the future.
            self.damage = ("Minimal", "Maximal")
            self.hitChance = 0.0
            self.critChance = 0.0
            self.element = None
            self.type = None

### (Defined in script.rpy) ###