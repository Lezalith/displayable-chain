# Testing screen.
init python:
    config.per_frame_screens.append("chainScreen")

style chainScreenStyles_button_text:
    color "000"
style chainScreenStyles_text:
    color "000"

screen chainScreen():

    style_prefix "chainScreenStyles"

    add Solid("fff")

    default noticeManager = NoticeManager()

    default m = BattleManager( ally = allyCharacter, enemy = enemyCharacter, noticeManager = noticeManager )


    vbox:

        textbutton "Spawn" action Function(m.start)

        spacing 20

        showif m.controlsShown:

            # Buttons
            vbox:
                spacing -8

                textbutton "Ally Regular Attack (5 - 10 damage)" action Function(m.attack, "ally", allyRegular)
                textbutton "Ally Fast Attack (5 - 20 damage) (Costs 15 AP)" action Function(m.attack, "ally", allyFast)
                textbutton "Ally Heavy Attack (20 - 30 damage) (Costs 35 AP)" action Function(m.attack, "ally", allyHeavy)
                textbutton "Ally Spell" action Function(m.spell, "ally", allySpell)
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


    vbox:

        align (1.0, 1.0)

        text "Manager State: {}".format(m.state)
        textbutton "Notice 1" action Function(noticeManager.addNotice, text = "First notice.")
        textbutton "Notice 2" action Function(noticeManager.addNotice, text = "Slightly longer second notice.")

    add noticeManager

    add m