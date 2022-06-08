# Animations of Enemy Character.
init -45 python:

    enterEnemy = Animation("wind dervish", enterTransEnemy, 1.5)

    idleEnemy = Animation("wind dervish", idleTransEnemy, 0)

    moveForwardEnemy = Animation("wind dervish", moveForwardTransEnemy, 1.0)
    moveBackEnemy = Animation("wind dervish", moveBackTransEnemy, 1.0)

    attackEnemy = Animation("wind dervish", attackTransEnemy, 1.1, trigger = True, triggerDelays = [0.1, 0.3, 0.5, 0.7])

    hitEnemy = Animation("wind dervish", hitTransEnemy, 1.1)

    deathEnemy = Animation("wind dervish", deathEnemy, 2.0 )