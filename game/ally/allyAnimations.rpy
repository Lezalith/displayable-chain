# TODO: spells.rpy
image spellImage = At(Solid("4287f5"), Transform(xysize = (200, 500)))


# Animations of Ally Character.
init -45 python:

    spellAnimation = Animation("spellImage", spellTransform, 4.0, trigger = True, triggerDelays = [1.4, 1.7, 2.0, 2.3])

    enter = Animation("allyRunForward", enterTrans, 1.0)

    idle = Animation("allyIdle", idleTrans, 0)

    moveForward = Animation("allyRunForward", moveForwardTrans, 1.0)
    moveBack = Animation("allyRunBack", moveBackTrans, 1.0)

    # TODO: There needs to be a Transform solely with the position where movein ends, moveback begins and attack takes place.
    # TODO: Right now bypassed with the align = (0.6, 0.5)
    attack = Animation("allyAttackMedium", Transform(align = (0.6, 0.5)), 0.6, trigger = True, triggerDelays = [0.2])
    attackFast = Animation("allyAttackQuick", Transform(align = (0.6, 0.5)), 0.4, trigger = True, triggerDelays = [0.1])
    attackHeavy = Animation("allyAttackHeavy", Transform(align = (0.6, 0.5)), 1.0, trigger = True, triggerDelays = [0.18, 0.6])

    hit = Animation("allyHit", Transform(align = (0.3, 0.5)), 0.1)

    death = Animation("allyRunBack", deathTrans, 1.5)