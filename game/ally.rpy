init -30:

    # Transforms used by the AnimationChain
    transform enterTrans():

        xalign 0.3 yalign 0.5 xoffset -600 alpha 0.0
        linear 1.0 xoffset 0 alpha 1.0

    transform idleTrans():

        xalign 0.3 yalign 0.5

    transform moveForwardTrans():

        xalign 0.3 yalign 0.5
        linear 1.0 xalign 0.6

    transform attackTrans():

        xalign 0.6 yalign 0.5
        linear 0.3 xoffset 50
        linear 0.3 xoffset 0

    transform attackHeavyTrans():

        xalign 0.6 yalign 0.5
        easein 0.6 xoffset -100
        linear 0.4 xoffset 50
        pause 0.3
        linear 0.3 xoffset 0

    transform attackFastTrans():

        xalign 0.6 yalign 0.5
        easeout 0.3 xoffset -150
        linear 0.4 xoffset 1000
        pause 0.1 xoffset -1000
        easein 0.4 xoffset 0

    transform moveBackTrans():

        xalign 0.6 yalign 0.5
        linear 1.0 xalign 0.3

    transform hitTrans():

        xalign 0.3 yalign 0.5
        linear 0.3 xoffset -60
        linear 0.3 xoffset 0

    transform deathTrans():

        xoffset 0 align (0.3, 0.5) xzoom -1.0
        linear 1.5 xoffset - 1000

    transform spellTransform():

        yalign 0.5 xoffset -510
        ease 0.8 xoffset 300
        ease 0.8 xoffset 600
        ease 0.8 xoffset 900
        ease 0.8 xoffset 1200
        ease 0.8 xoffset 1500


    # Images definitions
    image enterState = Composite(
        (200, 200),
        (0, 0), Solid("ffff7e"),
        (0, 0), Text("entering", size = 40, color = "00f"))

    image idleState = Composite(
        (200, 200),
        (0, 0), Solid("ff0"),
        (0, 0), Text("idle", size = 40, color = "00f"))

    image moveState = Composite(
        (200, 200),
        (0, 0), Solid("f70"),
        (0, 0), Text("moving", size = 40, color = "00f"))

    image attackState = Composite(
        (200, 200),
        (0, 0), Solid("f00"),
        (0, 0), Text("attacking", size = 40, color = "00f"))

    image hitState = Composite(
        (200, 200),
        (0, 0), Solid("C70039"),
        (0, 0), Text("hit", size = 40, color = "00f"))

    image spellImage = At(Solid("4287f5"), Transform(xysize = (200, 500)))


# Animations of Ally Character
init -25 python:

    spellAnimation = Animation("spellImage", spellTransform, 4.0, trigger = True, triggerDelays = [1.4, 1.7, 2.0, 2.3])

    enter = Animation("allyRunForward", enterTrans, 1.0)
    # enter = Animation("moveState", enterTrans, 1.0)

    # To be deleted.
    enter2 = Animation("enterState", enterTrans, 1.0)
    # enter2 = Animation("enterState", enterTrans, 1.0)


    moveForward = Animation("allyRunForward", moveForwardTrans, 1.0)
    moveBack = Animation("allyRunBack", moveBackTrans, 1.0)
    # moveForward = Animation("moveState", moveForwardTrans, 1.0)
    # moveBack = Animation("moveState", moveBackTrans, 1.0)

    idle = Animation("allyIdle", idleTrans, 0)
    # idle = Animation("idleState", idleTrans, 0)

    # TODO: There needs to be a Transform solely with the position where movein ends, moveback begins and attack takes place.
    # TODO: Right now bypassed with the align = (0.6, 0.5)
    attack = Animation("allyAttackMedium", Transform(align = (0.6, 0.5)), 0.6, trigger = True, triggerDelays = [0.2])
    # attack = Animation("attackState", attackTrans, 0.6, trigger = True, triggerDelay = 0.3)

    hit = Animation("allyHit", Transform(align = (0.3, 0.5)), 0.1)
    # hit = Animation("hitState", hitTrans, 0.6)

    attackHeavy = Animation("allyAttackHeavy", Transform(align = (0.6, 0.5)), 1.0, trigger = True, triggerDelays = [0.18, 0.6])
    attackFast = Animation("allyAttackQuick", Transform(align = (0.6, 0.5)), 0.4, trigger = True, triggerDelays = [0.1])
    # attackHeavy = Animation("attackState", attackHeavyTrans, 1.6, trigger = True, triggerDelay = 1.0)
    # attackFast = Animation("attackState", attackFastTrans, 1.8, trigger = True, triggerDelay = 0.4)

    death = Animation("allyRunBack", deathTrans, 1.5)