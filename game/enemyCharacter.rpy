init -13 python:

    class EnemyCharacter(BattleCharacter):

        def __init__(self, name, dictOfChains, hp):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(EnemyCharacter, self).__init__(name, dictOfChains, hp)


default enemyCharacter = EnemyCharacter( "Enemy Character", {"enter" : enemySpawnChain, "hit" : enemyHitFancyChain, "death" : enemyDeathChain}, 46.0 )