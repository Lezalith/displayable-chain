# Testing screen.
screen chainScreen():

    vbox:

        first_spacing 20

        # Buttons
        hbox:
            first_spacing 100
            spacing 20

            # textbutton "Spawn" action Function(m.start), Function(m.start)
            # textbutton "Ally Attack" action Function(m.allyChain.moveForward)
            # textbutton "Enemy Attack" action Function(m.enemyChain.moveForward)

            textbutton "Begin Spawn Chain" action Function(allySpawnChain.beginChain)
            textbutton "Begin Attack Chain" action Function(allyAttackChain.beginChain)
            textbutton "Begin Hit Chain" action Function(allyHitChain.beginChain)

            # textbutton "Ally Hit" action Function(m.allyChain.gotHit)
            # textbutton "Enemy Hit" action Function(m.enemyChain.gotHit)

        # # State info
        # text "Current Ally state: [m.allyChain.state]"
        # text "Current Enemy state: [m.enemyChain.state]"

        # Add info on currentAnimation and/or currentChild?

    # adding our CDD.
    add allySpawnChain
    add allyAttackChain
    add allyHitChain