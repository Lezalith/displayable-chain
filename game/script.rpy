# The game starts here.
label start:

    python:

        allyRegular = BattleAction("Regular Attack", allyAttackChain, (5, 10), "attack")
        allyHeavy = BattleAction("Heavy Attack", allyAttackHeavyChain, (20, 30), "attack", apCost = 35.0)
        allyFast = BattleAction("Fast Attack", allyAttackFastChain, (5, 20), "attack", apCost = 15.0)

        enemyRegular = BattleAction("Regular Attack", enemyAttackChain, (3, 6), "attack")

        allySpell = BattleAction("Snowflake Cluster", allySpellChain, (24, 44), "spell", mpCost = 42.0, associatedChain = allySpellCastChain)

    # Black background.
    scene expression Solid("000")

    # Jump right to the testing screen.
    call screen battleScreen

    return