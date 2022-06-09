init -13 python:

    # For choosing an attack.
    from random import choice 

    class EnemyCharacter(BattleCharacter):

        def __init__(self, name, dictOfChains, hp):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(EnemyCharacter, self).__init__(name, dictOfChains, hp)

        # How enemy acts during turns. Only in EnemyCharacter subclass.
        def enemyTurnAI(self):

            return choice(self.knownActions)

default enemyCharacter = EnemyCharacter( "Enemy Character", {"enter" : enemySpawnChain, "hit" : enemyHitFancyChain, "death" : enemyDeathChain}, 46.0 )