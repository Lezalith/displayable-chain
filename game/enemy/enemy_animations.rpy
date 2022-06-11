# Animations of Enemy Character.

init -46:

    define enemyIdlePosition = Transform( align = (0.7, 0.5) )
    define enemyAttackPosition = Transform( align = (0.4, 0.5) )

init -45 python:

    enterEnemy = BattleAnimation("wind dervish", enterTransEnemy, 1.5)

    idleEnemy = BattleAnimation("wind dervish", idleTransEnemy, 0)

    moveForwardEnemy = BattleAnimation("wind dervish", moveForwardTransEnemy, 1.0)
    moveBackEnemy = BattleAnimation("wind dervish", moveBackTransEnemy, 1.0)

    attackEnemy = BattleAnimation("wind dervish", attackTransEnemy, 1.1, trigger = True, triggerDelays = [0.1, 0.3, 0.5, 0.7])

    hitEnemy = BattleAnimation("wind dervish", hitTransEnemy, 1.1)

    deathEnemy = BattleAnimation("wind dervish", deathEnemy, 2.0 )