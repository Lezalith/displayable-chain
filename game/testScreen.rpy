# Testing screen.
init python:
    config.per_frame_screens.append("chainScreen")

screen chainScreen():

    vbox:

        spacing 20

        # Buttons
        vbox:
            spacing -8

            textbutton "Spawn" action Function(m.start)
            textbutton "Ally Regular Attack (5 - 10 damage)" action Function(m.attack, "ally", allyRegular)
            textbutton "Ally Fast Attack (5 - 20 damage) (Costs 15 AP)" action Function(m.attack, "ally", allyFast)
            textbutton "Ally Heavy Attack (20 - 30 damage) (Costs 35 AP)" action Function(m.attack, "ally", allyHeavy)
            textbutton "Enemy Regular Attack" action Function(m.attack, "enemy", enemyRegular)

        vbox:
            spacing -8

            textbutton "Enemy has fancy dodge" action SetField(m.enemyCharacter, "hitChain", enemyHitFancyChain)
            textbutton "Enemy has regular dodge" action SetField(m.enemyCharacter, "hitChain", enemyHitChain)

            # textbutton "Begin Spawn Chain" action Function(allySpawnChain.beginChain)
            # textbutton "Begin Attack Chain" action Function(allyAttackChain.beginChain)
            # textbutton "Begin Hit Chain" action Function(allyHitChain.beginChain)

            # textbutton "Ally Hit" action Function(m.allyChain.gotHit)
            # textbutton "Enemy Hit" action Function(m.enemyChain.gotHit)

        # Characte stats
    vbox:
        align (0.0, 0.8)

        text "Ally HP: [m.allyCharacter.hp]"
        text "Ally AP: [m.allyCharacter.ap]"

    vbox:
        align (1.0, 0.8)

        text "Enemy HP: [m.enemyCharacter.hp]"
        text "Enemy AP: [m.enemyCharacter.ap]"


    add NoticeManager

    vbox:

        align (1.0, 1.0)

        textbutton "Notice 1" action Function(NoticeManager.addNotice, text = "First notice.")
        textbutton "Notice 2" action Function(NoticeManager.addNotice, text = "Slightly longer second notice.")
        

        # Add info on currentAnimation and/or currentChild?

    add m

    # adding our CDD.
    # add allySpawnChain
    # add allyAttackChain
    # add allyHitChain