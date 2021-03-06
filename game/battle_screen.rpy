# Screen of the battle.

# Makes sure screen is rendered every frame, not every interaction.
# This is currently used for on-screen info, and will be removed once there's a CDD to contain the info.
init python:
    config.per_frame_screens.append("battleScreen")

# Default black color of the text, since BG is white.
style battleScreenStyles_button_text:
    color "000"
style battleScreennStyles_text:
    color "000"

screen battleScreen():

    # Use styles.
    style_prefix "battleScreenStyles"

    # White background.
    add Solid("fff")

    # Define a Notice Manager.
    # Arg is a float of for how long the messages stay on screen.
    default noticeManager = NoticeManager(4.0)

    # Define a Battle Manager.
    # This is a CDD that controls the entire battle.
    default m = BattleManager( player = playerCharacter, enemy = enemyCharacter, noticeManager = noticeManager )

    # Makeshift controls.
    vbox:
        spacing 20

        # Button to start a battle, only if not already started.
        if m.state == "notStarted":
            textbutton "Begin Battle" action Function(m.start)

        # Controls are hidden during Enters, Attacks or Spells.
        showif m.controlsShown:

            # Action buttons
            vbox:
                spacing -8

                # Loop showing all usable Actions on player's turn.
                for action in m.playerCharacter.knownActions:

                    textbutton "Player [action.name] ([action.damage[0]] - [action.damage[1]] damage, costs [action.apCost] AP and [action.mpCost] MP)":
                        action Function(m.action, "player", action)

                # TODO: Can be changed to two separate for loops:
                # for attack in m.playerCharacter.getKnownActions(type = "attack")
                # for spell in m.playerCharacter.getKnownActions(type = "spell")

                null height 20
                textbutton "Enemy Regular Attack" action Function(m.action, "enemy", enemyRegular)

    # Player Character stats
    vbox:
        align (0.0, 0.8)

        text "Player HP: [m.playerCharacter.hp]" color "000"
        text "Player AP: [m.playerCharacter.ap]" color "000"
        text "Player MP: [m.playerCharacter.mp]" color "000"

    # Enemy Character stats
    vbox:
        align (1.0, 0.8)

        text "Enemy HP: [m.enemyCharacter.hp]" color "000"
        text "Enemy AP: [m.enemyCharacter.ap]" color "000"
        text "Enemy MP: [m.enemyCharacter.mp]" color "000"

    # Add NoticeManager.
    add noticeManager

    # Debug - Text of BattleManager.state.
    text "[m.state]" align (1.0, 1.0) color "000"

    # Add BattleManager.
    add m