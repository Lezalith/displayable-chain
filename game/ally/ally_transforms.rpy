# Transforms used by the Animations in allyAnimations.rpy.
init -46:
    transform enterTrans():

        xalign 0.3 yalign 0.5 xoffset -600 alpha 0.0
        linear 1.0 xoffset 0 alpha 1.0

    transform idleTrans():

        xalign 0.3 yalign 0.5

    transform moveForwardTrans():

        xalign 0.3 yalign 0.5
        linear 1.0 xalign 0.6

    transform moveBackTrans():

        xalign 0.6 yalign 0.5
        linear 1.0 xalign 0.3

    transform attackTrans():

        xalign 0.6 yalign 0.5
        linear 0.3 xoffset 50
        linear 0.3 xoffset 0

    transform attackFastTrans():

        xalign 0.6 yalign 0.5
        easeout 0.3 xoffset -150
        linear 0.4 xoffset 1000
        pause 0.1 xoffset -1000
        easein 0.4 xoffset 0

    transform attackHeavyTrans():

        xalign 0.6 yalign 0.5
        easein 0.6 xoffset -100
        linear 0.4 xoffset 50
        pause 0.3
        linear 0.3 xoffset 0

    transform hitTrans():

        xalign 0.3 yalign 0.5
        linear 0.3 xoffset -60
        linear 0.3 xoffset 0

    transform deathTrans():

        xoffset 0 align (0.3, 0.5)
        linear 1.5 xoffset - 1000

    transform snowflakeTransform():
        xoffset -1000 yoffset -1000 yalign 1.0
        pause 1.0
        function snowflakeTransformFunc

    transform slidePauseTrans():
        xalign 0.3 yalign 0.5
        pause 0.3

    transform slideTrans():
        xalign 0.3 yalign 0.5
        ease 0.8 xalign 0.5

    transform slideFinishTrans():
        xalign 0.5 yalign 0.5
        pause 0.1

    transform moveBackAfterSlideTrans():
        xalign 0.5 yalign 0.5
        linear 0.5 xalign 0.3
        
    transform spellTransform():

        yalign 0.5 xoffset -510
        ease 0.8 xoffset 300
        ease 0.8 xoffset 600
        ease 0.8 xoffset 900
        ease 0.8 xoffset 1200
        ease 0.8 xoffset 1500

init -47 python:

    def snowflakeTransformFunc(trans, st, at):

        # Make it faster
        st = st * 5.5

        # The swing.
        trans.xoffset = st * 450
        trans.yoffset = - ((1 / (st + 1.5)) * 950)

        # Total duration.
        if st / 5.5 <= 1.4:
            return 0

        return None