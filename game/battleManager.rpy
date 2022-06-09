init -10 python:

    # Controls the entire Battle.
    class BattleManager(renpy.Displayable):

        # ally is BattleCharacter, the player
        # enemy is BattleCharacter, the opponent
        # TODO: Make these into lists for multiple participants in a battle!
        # noticeManager is an injection for displaying messages.
        def __init__(self, player, enemy, noticeManager, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(BattleManager, self).__init__(**kwargs)

            # Participants of the battle.
            self.playerCharacter = player
            self.enemyCharacter = enemy

            # Attack that's currently in play.
            self.currentAttack = None

            # List of Spells currently in play.
            self.spellsInPlay = []

            # NoticeManager for displaying messages.
            self.noticeManager = noticeManager

            # Current state of the BattleManager. Current states include:
            # - notStarted -- Before the battle begins.
            # - started ----- Battle started, characters entering.
            # - attack ------ In the middle of an Attack or Spell.
            # - playerTurn -------- Inbetween turns.
            # - playerAttack ------ 
            # - enemyTurn ---------
            # - enemyAttack -------
            # - finished ---- When one Character is defeated.
            self.state = "notStarted"

            # Time pause after a state is changed.
            # TODO: Currently not working.
            self.statePauseDuration = 1.0

            # Whether controls are shown on screen.
            self.controlsShown = False
            # States in which controls are shown.
            self.statesAllowingControls = ["playerTurn", "enemyTurn"]

        # Returns a list of all displayables held by the BattleManager.
        # Currently, it's only the two BattleCharacters.
        def getChildrenChains(self):

            return [self.playerCharacter.getChain(), self.enemyCharacter.getChain()]

        # Check whether someone has died, i.e. someone has HP below 0.
        def checkDeaths(self):

            # None if nobody died.
            # Tuple if someone died, of (the killer, the killed)
            # TODO: Should probably derive from self.attacking and self.attacked, but I had Thornmail effects in mind when writing this part.
            whoDied = None

            # If it's the Ally with HP below 0.
            if self.playerCharacter.hp <= 0:

                whoDied = (self.enemyCharacter, self.playerCharacter)

                # Tell the Ally Character to die.
                self.playerCharacter.died()

            # If it's the Enemy with HP below 0.
            elif self.enemyCharacter.hp <= 0:

                whoDied = (self.playerCharacter, self.enemyCharacter)

                # Tell the Enemy Character to die.
                self.enemyCharacter.died()

            # If someone died...
            if whoDied is not None:

                # Display a message about an attack of one Character killed the other.
                self.noticeManager.addNotice("An attack of {} has killed {}!".format(whoDied[0].name, whoDied[1].name), color = "000")

                self.setState("finished")

        # Gets a BattleAction from the EnemyCharacter's ai and execute it.
        def playEnemyTurn(self):

            ai = self.enemyCharacter.enemyTurnAI()

            self.action(origin = "enemy", action = ai)

        # Sets the state of BattleManager.
        def setState(self, state):

            # If the game was already finished, ignore all this:
            if self.state == "finished":
                return None

            # If we're setting it to "playerTurn":
            if state in ["playerTurn", "enemyTurn"]:

                # Next if branch checks what the original state was.

                # It was "attack":
                if self.state in ["playerAttack", "enemyAttack"]:

                    print("Checking deaths.")

                    # Check whether one of the Characters died.
                    self.checkDeaths()

                # "It was started":
                elif self.state == "started":

                    # Message about battle starting.
                    self.noticeManager.addNotice("Characters have entered the battle!", color = "000")

                    # TODO: Likely more stuff here once I code more on states.

            self.currentAttack = None

            # Set the new state, unless it became finished somewhere along the way, like in checkDeaths().
            if not self.state == "finished":

                # Set the new state.
                self.state = state

            if self.state == "enemyTurn":

                self.playEnemyTurn()

        # Checks whether someone should get hit.
        def checkHit(self):

            # Check whether the current Animation of attacking Character has a trigger and whether it's gone off.
            if self.currentAttack.attacker.getChain().checkTrigger():

                print("triggered trigger of defender from an attack.")

                # Instigate the attacked Character to get hit.
                self.currentAttack.defender.hit( self.currentAttack, self.noticeManager, self.currentAttack.defender.name )

            # Check for hits from spells in play.
            for spell in self.spellsInPlay:

                if spell.getChain().checkTrigger():

                    print("triggered trigger of defender from a spell")

                    # Instigate the attacked Character to get hit.
                    self.currentAttack.defender.hit( self.currentAttack, self.noticeManager, self.currentAttack.defender.name )

        # Begins the battle.
        def start(self):

            # Update state.
            self.setState("started")

            # Make both Characters enter.
            self.playerCharacter.enter()
            self.enemyCharacter.enter()

            # Trigger self.render, setting the battle into motion.
            renpy.redraw(self, 0)

        # Checks if AnimationChains of both Characters have finished.
        # This is used to determine whether the state should be set to "playerTurn".
        def checkFinishedChains(self):

            # Check for spells that have finished casting.
            for spell in self.spellsInPlay:
                if spell.getChain().finished:
                    self.spellsInPlay.remove(spell)

            # If the playerCharacter has a chain:
            if self.playerCharacter.getChain() is not None:

                # If it has finished:
                if self.playerCharacter.getChain().finished:

                    # If the enemyCharacter has a chain:
                    if self.enemyCharacter.getChain() is not None:

                        # If it has finished:
                        if self.enemyCharacter.getChain().finished:

                            # Check whether an attack is going on:
                            if self.currentAttack is not None:

                                # Check whether the AnimationChain of the attack has finished as well:
                                if not self.currentAttack.getChain().finished:

                                    return None

                            # If the current state is "started", i.e. characters were entering, or "attack", i.e. attack was happening,
                            # BUT the game hasn't finished yet.
                            if (self.state == "started" or self.state == "enemyAttack"):

                                # Set the state to "playerTurn".
                                self.setState("playerTurn" )

                            elif self.state == "playerAttack":

                                # Set the state to "enemyTurn".
                                self.setState("enemyTurn" )

        # Plays out a BattleAction.
        def action(self, origin, action):

            # Ally is using the action:
            if origin == "player":

                # If the Ally doesn't have enough AP or MP, end the function straight away.
                if not self.playerCharacter.checkCost(action, self.noticeManager):
                    return None

                # Set info about the action inside the action object.
                action.actionUsed(self.playerCharacter, self.enemyCharacter)

                if action.type == "attack":

                    # Instigate playerCharacter to attack. 
                    self.playerCharacter.attack( action, self.noticeManager )

                elif action.type == "spell":

                    # Instigate playerCharacter to cast the spell.
                    self.playerCharacter.spellCast( action, self.noticeManager )

                # Update the state.
                self.setState("playerAttack")

            # Enemy is using the action:
            elif origin == "enemy":

                # If the Ally doesn't have enough AP or MP, end the function straight away.
                # TODO: Not really point of this I think, since it won't be cast by the AI function in the first place.
                if not self.enemyCharacter.checkCost(action, self.noticeManager):
                    return None

                # Set info about the action inside the action object.
                action.actionUsed(self.enemyCharacter, self.playerCharacter)

                if action.type == "attack":

                    # Instigate enemyCharacter to attack. 
                    self.enemyCharacter.attack( action, self.noticeManager )

                elif action.type == "spell":

                    # Instigate enemyCharacter to cast the spell.
                    self.enemyCharacter.spellCast( action, self.noticeManager )

                # Update the state.
                self.setState("enemyAttack")

            # Set the current attack in play.
            # TODO: Rename to currentAction or actionInPlay.
            self.currentAttack = action

            if action.type == "spell":

                # Begin the chain of the spell.
                action.getChain().beginChain()

                # Adds the Spell object to a list remembering spells in play.
                self.spellsInPlay.append(action)

        # Renders all displayables held. Called with every renpy.redraw.
        def render(self, width, height, st, at):
            
            # Show the controls on the screen if in the "playerTurn" state.
            self.controlsShown = (True if self.state in self.statesAllowingControls else False)

            # Check if someone is attacking. If so, check if someone got hit.
            if self.currentAttack is not None:
                self.checkHit()

            # Checks if AnimationChains of both Characters have finished. This is used to determine whether the state should be set to "playerTurn".
            # Currently used to pass between states.
            self.checkFinishedChains()

            # Prepare a render. It is the size of the whole screen.
            render = renpy.Render(config.screen_width, config.screen_height)

            # Place every displayable held onto the render.
            for chain in self.getChildrenChains():

                # print("placing {}".format(chain))

                t = Transform(child = chain)
                render.place(t)

            # Place all Spell children onto the render.
            for spell in self.spellsInPlay:

                t = Transform(child = spell.getChain())
                render.place(t)

            # Returns the render.
            return render

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our childen's AnimationChains.
            for disp in self.getChildrenChains():

                # If child's AnimationChain is not triggered, there will be no displayable to pass an event to.
                if disp is not None:

                    disp.event(ev, x, y, st)

            # Pass the event to AnimationChains of all the spells in play.
            for spell in self.spellsInPlay:

                spell.getChain().event(ev, x, y, st)

        # Honestly not sure what this does, but it needs to return all displayables rendered.
        def visit(self):

            allChildren = [spell.getChain() for spell in self.spellsInPlay]
            allChildren.extend(self.getChildrenChains())

            return allChildren

# BattleManager is defined inside the battle screen.