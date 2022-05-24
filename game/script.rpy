# The game starts here.
label start:

    python:

        allyRegular = Attack("Regular Attack", allyAttackChain)
        allyHeavy = Attack("Heavy Attack", allyAttackHeavyChain)
        allyFast = Attack("Fast Attack", allyAttackFastChain)

        enemyRegular = Attack("Regular Attack", enemyAttackChain)

    # Jump right to the testing screen.
    call screen chainScreen

    return