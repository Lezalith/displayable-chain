# The game starts here.
label start:

    python:

        allyRegular = Attack("Regular Attack", allyAttackChain, (5, 10))
        allyHeavy = Attack("Heavy Attack", allyAttackHeavyChain, (20, 30), apCost = 35.0)
        allyFast = Attack("Fast Attack", allyAttackFastChain, (5, 20), apCost = 15.0)

        enemyRegular = Attack("Regular Attack", enemyAttackChain, (3, 6))

        allySpell = Spell("Snowflake Cluster", allySpellChain, allySpellCastChain, (24, 44), mpCost = 42.0)

    # Black background.
    scene expression Solid("000")

    # Jump right to the testing screen.
    call screen battleScreen

    return