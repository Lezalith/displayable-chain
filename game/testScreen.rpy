# Testing screen.
screen chainScreen():

    vbox:

        spacing 20

        # Buttons
        hbox:
            spacing 20

            textbutton "Spawn" action Function(m.start)
            textbutton "Ally Regular Attack" action Function(m.attack, "ally", allyRegular)
            textbutton "Ally Heavy Attack" action Function(m.attack, "ally", allyHeavy)
            textbutton "Ally Fast Attack" action Function(m.attack, "ally", allyFast)
            textbutton "Enemy Regular Attack" action Function(m.attack, "enemy", enemyRegular)

        vbox:
            spacing -8

            textbutton "Enemy has regular dodge" action SetField(m.enemyCharacter, "hitChain", enemyHitChain)
            textbutton "Enemy has fancy dodge" action SetField(m.enemyCharacter, "hitChain", enemyHitFancyChain)

            # textbutton "Begin Spawn Chain" action Function(allySpawnChain.beginChain)
            # textbutton "Begin Attack Chain" action Function(allyAttackChain.beginChain)
            # textbutton "Begin Hit Chain" action Function(allyHitChain.beginChain)

            # textbutton "Ally Hit" action Function(m.allyChain.gotHit)
            # textbutton "Enemy Hit" action Function(m.enemyChain.gotHit)

        # # State info
        # text "Current Ally state: [m.allyChain.state]"
        # text "Current Enemy state: [m.enemyChain.state]"

        # Add info on currentAnimation and/or currentChild?

    add m

    # adding our CDD.
    # add allySpawnChain
    # add allyAttackChain
    # add allyHitChain