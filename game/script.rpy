# The game starts here.
label start:

    python:

        # BattleActions of the Player.
        allyRegular = BattleAction("Regular Attack", allyAttackChain, (5, 10), "attack")
        allyFast = BattleAction("Fast Attack", allyAttackFastChain, (5, 20), "attack", apCost = 15.0)
        allyHeavy = BattleAction("Heavy Attack", allyAttackHeavyChain, (20, 30), "attack", apCost = 35.0)
        allySpell = BattleAction("Snowflake Cluster", allySpellChain, (24, 44), "spell", mpCost = 42.0, associatedChain = allySpellCastChain)

        a = [allyRegular, allyFast, allyHeavy, allySpell]

        # Let Player learn the Actions.
        for action in a:
            store.playerCharacter.learnAction(action)

        #########################################################################################################################################

        # BattleActions of the Enemy.
        enemyRegular = BattleAction("Regular Attack", enemyAttackChain, (3, 6), "attack")

        # Let Enemy learn the Actions.
        store.enemyCharacter.learnAction(enemyRegular)

    # Black background.
    scene expression Solid("000")

    # Jump right to the testing screen.
    call screen battleScreen

    return