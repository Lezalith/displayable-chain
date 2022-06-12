image modifiedSnowflake = At("snowflake", Transform(zoom = 0.5))
image snowflakeStorm = Composite( (250, 250),
                                (0, 0), "modifiedSnowflake",
                                (210, 90), "modifiedSnowflake",
                                (40, 180), "modifiedSnowflake",
                                (90, 90), "modifiedSnowflake",
                                (160, 250), "modifiedSnowflake",
                                (250, 250), "modifiedSnowflake",
                                (310, 70), "modifiedSnowflake",
                                )

init -46:

    define playerIdlePosition = Transform( align = (0.3, 0.5) )
    define playerAttackPosition = Transform( align = (0.6, 0.5) )

    define sizeTrans = Transform( xysize = (200, 200) )

    # image allyAttackMedium = At( anim.Filmstrip("images/allyAttackMedium.png", framesize = (120, 80), gridsize = (6, 1), delay = 0.1), sizeTrans) 
    image allyAttackQuick = At( anim.Filmstrip("images/allyAttackQuick.png", framesize = (120, 80), gridsize = (4, 1), delay = 0.1), sizeTrans) 
    image allyAttackHeavy = At( anim.Filmstrip("images/allyAttackHeavy.png", framesize = (120, 80), gridsize = (10, 1), delay = 0.1), sizeTrans) 

# Animations of Player Character.
init -45 python:

    spellAnimation = BattleAnimation("snowflakeStorm", snowflakeTransform, 1.4, trigger = True, triggerDelays = [1.15])

    slidePause = BattleAnimation("allyIdle", slidePauseTrans, 0.3)
    slide = BattleAnimation("allySlide", slideTrans, 0.8)
    slideFinish = BattleAnimation("allySlideFinish", slideFinishTrans, 0.1)
    moveBackAfterSlide = BattleAnimation("allyRunBack", moveBackAfterSlideTrans, 0.5)

    enter = BattleAnimation("allyRunForward", enterTrans, 1.0)

    idle = BattleAnimation("allyIdle", idleTrans, 0)

    moveForward = BattleAnimation("allyRunForward", moveForwardTrans, 1.0)
    moveBack = BattleAnimation("allyRunBack", moveBackTrans, 1.0)

    attack = BattleAnimation("allyAttackMedium", playerAttackPosition, 0.6, trigger = True, triggerDelays = [0.3])
    attackFast = BattleAnimation("allyAttackQuick", playerAttackPosition, 0.4, trigger = True, triggerDelays = [0.1])
    attackHeavy = BattleAnimation("allyAttackHeavy", playerAttackPosition, 1.0, trigger = True, triggerDelays = [0.18, 0.6])

    hit = BattleAnimation("allyHit", playerIdlePosition, 0.1)

    death = BattleAnimation("allyRunBack", deathTrans, 1.5)