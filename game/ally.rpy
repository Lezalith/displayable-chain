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

    transform moveBackTrans():

        xalign 0.6 yalign 0.5
        linear 1.0 xalign 0.3

    transform hitTrans():

        xalign 0.3 yalign 0.5
        linear 0.3 xoffset -60
        linear 0.3 xoffset 0


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