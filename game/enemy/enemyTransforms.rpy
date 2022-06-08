init -46:

    # Transforms used by the AnimationChains
    transform enterTransEnemy():

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

    transform moveBackTransEnemy():

        xalign 0.4 yalign 0.5
        linear 1.0 xalign 0.7

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

    transform hitTransEnemy():

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