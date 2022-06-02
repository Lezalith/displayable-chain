init -50:

    # Transforms used by the AnimationChain
    transform enterTransEnemy():

        xalign 0.7 yalign 0.5 xoffset 600 alpha 0.0
        linear 1.0 xoffset 0 alpha 1.0

    transform enterFancyTransEnemy():

        xalign 0.7 yalign 0.5 xoffset 1000 yoffset -1000 alpha 0.0

        block:
            parallel:
                ease 1.5 xoffset 0 yoffset 0

            parallel:
                pause 0.7
                ease 0.8 alpha 1.0

    transform idleTransEnemy():

        xalign 0.7 yalign 0.5

    transform moveForwardTransEnemy():

        xalign 0.7 yalign 0.5
        linear 1.0 xalign 0.4

    transform attackTransEnemy():

        xalign 0.4 yalign 0.5

        block:
            parallel:
                linear 0.4 xoffset -50
                pause 0.46
                linear 0.1 xoffset 0

            parallel:
                linear 0.24 xzoom -1.0
                linear 0.24 xzoom 1.0
                linear 0.24 xzoom -1.0
                linear 0.24 xzoom 1.0

    transform moveBackTransEnemy():

        xalign 0.4 yalign 0.5
        linear 1.0 xalign 0.7

    transform hitTransEnemy():

        xalign 0.7 yalign 0.5
        linear 0.3 xoffset 60
        linear 0.3 xoffset 0

    transform hitFancyTransEnemy():

        xalign 0.7 yalign 0.5

        block:

            parallel:
                linear 0.1 xoffset 20 yoffset 0
                linear 0.1 xoffset 30 yoffset -20
                linear 0.1 xoffset 45 yoffset -50
                linear 0.1 xoffset 65 yoffset -75

            parallel:
                alpha 1.0
                easein 0.2 alpha 0.0 
                easein 0.1 alpha 0.5

        easein 0.4 xoffset 0 yoffset 0 alpha 1.0

    transform deathEnemy():

        xalign 0.7 yalign 0.5 yoffset 0 alpha 1.0
        easeout 1.0 yoffset 100 alpha 0.0


    # Images definitions
    image enterStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("00FF7F"),
        (0, 0), Text("entering", size = 40, color = "f00"))

    image idleStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("7CFC00"),
        (0, 0), Text("idle", size = 40, color = "f00"))

    image moveStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("90EE90"),
        (0, 0), Text("moving", size = 40, color = "f00"))

    image attackStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("426f59"),
        (0, 0), Text("attacking", size = 40, color = "f00"))

    image hitStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("fc00fa"),
        (0, 0), Text("hit", size = 40, color = "f00"))

    image deathStateEnemy = Composite(
        (200, 200),
        (0, 0), Solid("00FF7F"),
        (0, 0), Text("dying", size = 40, color = "f00"))


# Animations of Enemy Character
init -25 python:

    enterEnemy = Animation("wind dervish", enterTransEnemy, 1.0)
    idleEnemy = Animation("wind dervish", idleTransEnemy, 0)
    moveForwardEnemy = Animation("wind dervish", moveForwardTransEnemy, 1.0)
    attackEnemy = Animation("wind dervish", attackTransEnemy, 1.1, trigger = True, triggerDelays = [0.1, 0.3, 0.5, 0.7])
    moveBackEnemy = Animation("wind dervish", moveBackTransEnemy, 1.0)
    hitEnemy = Animation("wind dervish", hitTransEnemy, 0.6)

    enterFancyEnemy = Animation("wind dervish", enterFancyTransEnemy, 1.5)
    hitFancyEnemy = Animation("wind dervish", hitFancyTransEnemy, 1.1)

    deathEnemy = Animation("wind dervish", deathEnemy, 2.0 )