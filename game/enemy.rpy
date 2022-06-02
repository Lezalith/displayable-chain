init -50:

    # Transforms used by the AnimationChain
    transform enterTransEnemy():

        xalign 0.7 yalign 0.5 xoffset 600 alpha 0.0
        linear 1.0 xoffset 0 alpha 1.0

    transform enterFancyTransEnemy():

        xalign 0.7 yalign 0.5 yoffset -1000 alpha 0.0

        parallel:
            ease 1.2 yoffset 0

        parallel:
            pause 0.85
            ease 0.35 alpha 1.0

    transform idleTransEnemy():

        xalign 0.7 yalign 0.5

    transform moveForwardTransEnemy():

        xalign 0.7 yalign 0.5
        linear 1.0 xalign 0.4

    transform attackTransEnemy():

        xalign 0.4 yalign 0.5
        linear 0.1 xoffset -5
        linear 0.1 xoffset 0

    transform moveBackTransEnemy():

        xalign 0.4 yalign 0.5
        linear 1.0 xalign 0.7

    transform hitTransEnemy():

        xalign 0.7 yalign 0.5
        linear 0.3 xoffset 60
        linear 0.3 xoffset 0

    transform hitFancyTransEnemy():

        xalign 0.7 yalign 0.5
        linear 0.5 xoffset 100 alpha 0.0
        easein 0.8 xoffset 0 alpha 1.0        


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


# Animations of Enemy Character
init -25 python:

    enterEnemy = Animation("enterStateEnemy", enterTransEnemy, 1.0)
    idleEnemy = Animation("idleStateEnemy", idleTransEnemy, 0)
    moveForwardEnemy = Animation("moveStateEnemy", moveForwardTransEnemy, 1.0)
    attackEnemy = Animation("attackStateEnemy", attackTransEnemy, 0.2, trigger = True, triggerDelays = [0.1])
    moveBackEnemy = Animation("moveStateEnemy", moveBackTransEnemy, 1.0)
    hitEnemy = Animation("hitStateEnemy", hitTransEnemy, 0.6)

    enterFancyEnemy = Animation("enterStateEnemy", enterFancyTransEnemy, 1.2)
    hitFancyEnemy = Animation("hitStateEnemy", hitFancyTransEnemy, 1.3)