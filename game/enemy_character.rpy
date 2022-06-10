init -13 python:

    # For choosing an attack.
    from random import choice 

    # Subclass of BattleCharacter from battle_character.rpy.
    class EnemyCharacter(BattleCharacter):

        # name is a string.
        # dictOfChains is a dictionary. Keys are keywords, values are AnimationChains. Valid keywords are:
        # - "enter" - Chain used for entering the battle.
        # - "hit" - Chain used for getting hit.
        # - "death" - Chain used for death/exiting the battle.
        # hp is the starting health of the Character.
        def __init__(self, name, dictOfChains, hp):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(EnemyCharacter, self).__init__(name, dictOfChains, hp)

        # How enemy acts during turns. Only in EnemyCharacter subclass.
        def enemyTurnAI(self):

            # Random known Action.
            return choice(self.knownActions)

default enemyCharacter = EnemyCharacter( "Enemy Character", {"enter" : enemySpawnChain, "hit" : enemyHitFancyChain, "death" : enemyDeathChain}, 46.0 )