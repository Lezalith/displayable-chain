init -15 python:

    # Represents a character inside a battle.
    # TODO: There will be an extensive GameCharacter class and this will be made to hold only Chains used inside the battle.
    # TODO: So this will probably store all the attacks, spells... And disregard everything not equipped or present? 
    #
    # Arguments:
    # name is the name of this character
    # enterChain is the chain used for entering the battle
    # attackChain is the chain used for attacking
    # hitChain is the chain used when getting hit
    class BattleCharacter():

        def __init__(self, name, enterChain, hitChain, hp):

            # Name of the Character.
            self.name = name

            # Relevant Chains.
            self.enterChain = enterChain
            self.hitChain = hitChain

            # Stats
            self.hp = hp
            self.mp = 100.0
            self.ap = 100.0

            # Current Chain used.
            # This is basically the Displayable of this character.
            self.currentChain = None

        # Trigger a chain representing the entrance to the battle.
        def enter(self):

            self.currentChain = self.enterChain
            self.currentChain.beginChain()

        # Trigger a chain representing attacking.
        def attack(self, attack):


            if self.ap < attack.apCost:

                return renpy.notify("Not enough AP!")

            self.ap -= attack.apCost

            self.currentChain = attack.animationChain
            self.currentChain.beginChain()

        # Trigger a chain representing getting hit.
        def hit(self, attack):

            self.hp -= attack.getDamage()

            self.currentChain = self.hitChain
            self.currentChain.beginChain()

        # Get self.currentChain.
        def getChain(self):

            return self.currentChain

# Characters defined.
default allyCharacter = BattleCharacter( "Ally Character", allySpawnChain, allyHitChain, 100.0 )
default enemyCharacter = BattleCharacter( "Enemy Character", enemySpawnChain, enemyHitFancyChain, 46.0 )