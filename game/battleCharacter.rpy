init -15 python:

    class BattleCharacter():

        # TODO: Do not require chains, displayable (Animation?) alone is fine
        def __init__(self, name, enterChain, attackChain, hitChain):

            # Name of the Character.
            self.name = name

            self.enterChain = enterChain
            self.attackChain = attackChain
            self.hitChain = hitChain

            self.currentChain = None

        def enter(self):

            # print("{} entering".format(self.name))

            self.currentChain = self.enterChain
            self.currentChain.beginChain()

        def attack(self):

            self.currentChain = self.attackChain
            self.currentChain.beginChain()

        def hit(self):

            self.currentChain = self.hitChain
            self.currentChain.beginChain()

        def getChain(self):

            return self.currentChain

default allyCharacter = BattleCharacter( "Ally Character", allySpawnChain, allyAttackChain, allyHitChain )
default enemyCharacter = BattleCharacter( "Enemy Character", enemySpawnChain, enemyAttackChain, enemyHitChain )