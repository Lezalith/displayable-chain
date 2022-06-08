init -10 python:

    # Controls the entire Battle.
    class BattleManager(renpy.Displayable):

        # ally is BattleCharacter, the player
        # enemy is BattleCharacter, the opponent
        # TODO: Make these into lists for multiple participants in a battle!
        # noticeManager is an injection for displaying messages.
        def __init__(self, ally, enemy, noticeManager, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(BattleManager, self).__init__(**kwargs)

            # Participants of the battle.
            self.allyCharacter = ally
            self.enemyCharacter = enemy

            # Attack that's currently in play.
            self.currentAttack = None

            # List of Spells currently in play.
            # TODO: Remake this.
            self.spellChildren = []

            # NoticeManager for displaying messages.
            self.noticeManager = noticeManager

            # Current state of the BattleManager. Current states include:
            # - notStarted -- Before the battle begins.
            # - started ----- Battle started, characters entering.
            # - attack ------ In the middle of an Attack or Spell.
            # - idle -------- Inbetween turns.
            # - finished ---- When one Character is defeated.
            # TODO: Currently, finished state is not working.
            self.state = "notStarted"

            # Time pause after a state is changed.
            # TODO: Currently not working.
            self.statePauseDuration = 1.0

            # Whether controls are shown on screen.
            # Currently True only for "idle" state.
            # TODO: Make a list of states when controls are shown, and determine it from that.
            self.controlsShown = False

        # Begins the battle.
        def start(self):

            # Update state.
            self.setState("started")

            # Make both Characters enter.
            self.allyCharacter.enter()
            self.enemyCharacter.enter()

            # Trigger self.render, setting the battle into motion.
            renpy.redraw(self, 0)

        # Returns a list of all displayables held by the BattleManager.
        # Currently, it's only the two BattleCharacters.
        # TODO: Probably should include spellChildren, too.
        def getChildrenChains(self):

            return [self.allyCharacter.getChain(), self.enemyCharacter.getChain()]

        # Begins an attack.
        # type can be "ally" for when ally character is attacking, and "enemy" for when enemy character is.
        # TODO: This is a pretty dumb way.
        # attack is the Attack object of the attack used.
        def attack(self, type, attack):

            # Update the state.
            self.setState("attack")

            # Ally is attacking:
            if type == "ally":

                # Instigate allyCharacter to attack. 
                attack.attackUsed(self.allyCharacter, self.enemyCharacter)

                # Set info about the attack inside the attack object.
                self.allyCharacter.attack( attack, self.noticeManager )

            # Enemy is attacking:
            elif type == "enemy":

                # Set info about the attack inside the attack object.
                attack.attackUsed(self.enemyCharacter, self.allyCharacter)

                # Instigate enemyCharacter to attack. 
                self.enemyCharacter.attack( attack, self.noticeManager )

            # Set the current attack in play.
            self.currentAttack = attack

        # Casts a spell.
        # type can be "ally" for when ally character is casting the spell, and "enemy" for when enemy character is.
        # TODO: This is a pretty dumb way.
        # spell is the Spell object of the spell cast.
        def spell(self, type, spell):

            # Update the state.
            # I don't think it differs enough from the attack to warrant a separate state at this point.
            self.setState("attack")

            # Ally is casting the spell:
            if type == "ally":

                # Instigate allyCharacter to attack. 
                spell.spellUsed(self.allyCharacter, self.enemyCharacter)

                # Instigate allyCharacter to cast the spell.
                self.allyCharacter.spellCast( spell, self.noticeManager )

                # Adds the Spell object to a list remembered spells in play.
                # TODO: This is currently a stupid makeshift way of testing a single spell.
                self.spellChildren = [spell]

            # Ally is casting the spell. Currently, there are no enemy spells.
            elif type == "enemy":

                # Instigate allyCharacter to attack. 
                spell.spellUsed(self.enemyCharacter, self.allyCharacter)

                # Instigate enemyCharacter to cast the spell.
                self.enemyCharacter.spellCast( spell, self.noticeManager )

                # Adds the Spell object to a list remembered spells in play.
                # TODO: This is currently a stupid makeshift way of testing a single spell.
                self.spellChildren = [spell]

            # Set the current spell in play.
            # TODO: Wait, does it actually make sense to have spellChildren if only one spell is in play..?
            self.currentAttack = spell

        # Checks whether someone should get hit.
        def checkHit(self):

            # print("currentAttack: {}".format(self.currentAttack))
            # print("defender: {}".format(self.currentAttack.defender))
            # print("getChain: {}".format(self.currentAttack.defender.getChain()))
            # print("checkTrigger: {}".format(self.currentAttack.defender.getChain().checkTrigger()))

            # Check whether the current Animation of attacking Character has a trigger and whether it's gone off.
            if self.currentAttack.attacker.getChain().checkTrigger():

                print("triggered trigger of defender")

                # Instigate the attacked Character to get hit.
                self.currentAttack.defender.hit( self.currentAttack, self.noticeManager, self.currentAttack.defender.name )

                # Reset info about an attack.
                # TODO: This will be done elsewhere, once the Battle has been split into phases.
                # TODO: Currently only gets overwritten by a new attack, but that's not a problem. Not reseting it here allows for attacks that hit multiple times.
                # self.currentAttack = None

        # Check whether someone has died, i.e. someone has HP below 0.
        def checkDeaths(self):

            # None if nobody died.
            # Tuple if someone died, of (the killer, the killed)
            # TODO: Should probably derive from self.attacking and self.attacked, but I had Thornmail effects in mind when writing this part.
            whoDied = None

            # If it's the Ally with HP below 0.
            if self.allyCharacter.hp <= 0:

                whoDied = (self.enemyCharacter, self.allyCharacter)

                # Tell the Ally Character to die.
                self.allyCharacter.died()

            # If it's the Enemy with HP below 0.
            elif self.enemyCharacter.hp <= 0:

                whoDied = (self.allyCharacter, self.enemyCharacter)

                # Tell the Enemy Character to die.
                self.enemyCharacter.died()

            # If someone died...
            if whoDied is not None:

                # Display a message about an attack of one Character killed the other.
                self.noticeManager.addNotice("An attack of {} has killed {}!".format(whoDied[0].name, whoDied[1].name), color = "000")

                # TODO: Not working, the state stays idle.
                self.setState("finished")

        # Renders all displayables held. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            # If the state is "idle":
            if  self.state == "idle":

                # Show the controls on the screen.
                self.controlsShown = True

            # Check if someone is attacking. If so, check if someone got hit.
            if self.currentAttack is not None:
                self.checkHit()

            # Checks if AnimationChains of both Characters have finished. This is used to determine whether the state should be set to "idle".
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
            for spellChild in self.spellChildren:

                t = Transform(child = spellChild.animationChain)
                render.place(t)

            # Returns the render.
            return render

        # Sets the state of BattleManager.
        def setState(self, state):

            # If we're setting to anything but "finished":
            if not state == "finished":

                # If we're setting it to "idle":
                if state == "idle":

                    # Next if branch checks what the original state was.

                    # It was "attack":
                    if self.state == "attack":

                        # Check whether one of the Characters died.
                        self.checkDeaths()

                    # "It was started":
                    elif self.state == "started":

                        # Message about battle starting.
                        self.noticeManager.addNotice("Characters have entered the battle!", color = "000")

                        # TODO: Likely more stuff here once I code more on states.

                # Set the new state.
                self.state = state

            # If we're setting the state to "finished":
            if state == "finished":

                # Reset all the info related to attacking.
                self.currentAttack = None

        # Checks if AnimationChains of both Characters have finished.
        # This is used to determine whether the state should be set to "idle".
        def checkFinishedChains(self):

            # If the allyCharacter has a chain:
            if self.allyCharacter.getChain() is not None:

                # If it has finished:
                if self.allyCharacter.getChain().finished:

                    # If the enemyCharacter has a chain:
                    if self.enemyCharacter.getChain() is not None:

                        # If it has finished:
                        if self.enemyCharacter.getChain().finished:

                            # If the current state is "started", i.e. characters were entering, or "attack", i.e. attack was happening:
                            if self.state == "started" or self.state == "attack":

                                # Set the state to "idle".
                                self.setState("idle" )

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our childen's AnimationChains.
            for disp in self.getChildrenChains():

                # If child's AnimationChain is not triggered, there will be no displayable to pass an event to.
                if disp is not None:

                    disp.event(ev, x, y, st)

            for spell in self.spellChildren:

                spell.getChain().event(ev, x, y, st)

            # TODO: spellChildren??

        # Honestly not sure what this does, but it needs to return all displayables rendered.
        # TODO: spellChildren??
        def visit(self):

            allChildren = [spell.getChain() for spell in self.spellChildren]
            allChildren.extend(self.getChildrenChains())

            return allChildren

# BattleManager is defined inside the battle screen.