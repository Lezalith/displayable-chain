init -10 python:

    # Controls the Battle.
    #
    # Arguments:
    # ally is the player
    # enemy is the opponent
    # TODO: Make these into lists for multiple participants in a battle!
    class BattleManager(renpy.Displayable):

        def __init__(self, ally, enemy, noticeManager, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(BattleManager, self).__init__(**kwargs)

            # Participants of the battle.
            self.allyCharacter = ally
            self.enemyCharacter = enemy

            # attacking is a character currently attacking.
            # attacked is a character currently *being* attacked.
            # TODO: Make these into lists, for AoE attacks!
            self.attacking = None
            self.attacked = None

            self.currentAttack = None

            self.noticeManager = noticeManager

            self.state = "notStarted"
            self.statePauseDuration = 1.0

            self.controlsShown = False

        # Begins the battle.
        # Currently only spawns the participants.
        def start(self):

            self.setState("started")

            self.allyCharacter.enter()
            self.enemyCharacter.enter()

            # Trigger render of this object, triggering the first render of participants.
            renpy.redraw(self, 0)

        # Returns a list of all displayables held by the BattleManager.
        def getChildrenChains(self):

            return [self.allyCharacter.getChain(), self.enemyCharacter.getChain()]

        # Begins an attack.
        # type can be "ally" for when ally character is attacking, and "enemy" for when enemy character is. 
        def attack(self, type, attack):

            self.state = "attack"

            # Ally attacking
            if type == "ally":

                # Trigger an AnimationChain of the attack.
                self.allyCharacter.attack( attack, self.noticeManager )

                # Set attacking character and attacked character.
                self.attacking = self.allyCharacter
                self.attacked = self.enemyCharacter

            # Enemy attacking
            elif type == "enemy":

                # Trigger an AnimationChain of the attack.
                self.enemyCharacter.attack( attack, self.noticeManager )

                # Set attacking character and attacked character.
                self.attacking = self.enemyCharacter
                self.attacked = self.allyCharacter

            self.currentAttack = attack

        # Triggers the hit AnimationChain of the attacked character.
        def checkHit(self):

            # Check whether the current Animation of attacking Character has a trigger and whether it's gone off.
            if self.attacking.getChain().checkTrigger():

                # Trigger hit AnimationChain of attacked.
                self.attacked.hit( self.currentAttack, self.noticeManager, self.attacking.name )

                # Reset info about an attack.
                # TODO: This will be done elsewhere, once the Battle has been split into phases.
                # TODO: Currently only gets overwritten by a new attack, but that's not a problem. Not reseting it here allows for attacks that hit multiple times.
                # self.attacking = None
                # self.attacked = None
                # self.currentAttack = None

        def checkDeaths(self):

            whoDied = None

            if self.allyCharacter.hp <= 0:

                whoDied = (self.enemyCharacter, self.allyCharacter)

                self.allyCharacter.died()

            elif self.enemyCharacter.hp <= 0:

                whoDied = (self.allyCharacter, self.enemyCharacter)

                self.enemyCharacter.died()

            if whoDied is not None:

                self.noticeManager.addNotice("An attack of {} has killed {}!".format(whoDied[0].name, whoDied[1].name))

                # TODO: Not working, the state stays idle.
                self.setState("finished")

        # Renders all displayables held. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            if not self.state == "idle":
                self.controlsShown = False

            # Check if someone is attacking. If so, check if they should trigger a hit.
            if self.attacking is not None:
                self.checkHit()

            self.checkFinishedChains()

            # Prepare a render. It is the size of the whole screen.
            render = renpy.Render(config.screen_width, config.screen_height)

            # Places every displayable held into the render.
            for chain in self.getChildrenChains():

                # print("placing {}".format(chain))

                t = Transform(child = chain)
                render.place(t)

            # Returns the render.
            return render

        def setState(self, state):

            if not state == "finished":


                if state == "idle":

                    # What the original state was
                    if self.state == "attack":

                        self.checkDeaths()

                    elif self.state == "started":

                        self.noticeManager.addNotice("Characters have entered the battle!")

                self.state = state

            if state == "idle" or state == "finished":
                self.currentAttack = None
                self.attacking = None
                self.attacked = None

                self.controlsShown = True

        # TODO: Bugged - Triggers when the same Chain is repeated.
        def checkFinishedChains(self):

            if self.allyCharacter.getChain() is not None:

                if self.allyCharacter.getChain().finished:

                    if self.enemyCharacter.getChain() is not None:

                        if self.enemyCharacter.getChain().finished:

                            if self.state == "started":

                                self.setState("idle" )

                            elif self.state == "attack":

                                self.setState("idle" )

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our childen's AnimationChains.
            for disp in self.getChildrenChains():

                # If child's AnimationChain is not triggered, there will be no displayable to pass an event to.
                if disp is not None:

                    disp.event(ev, x, y, st)

        # Honestly not sure what this does, but it needs to return all displayables rendered.
        def visit(self):
            return self.getChildrenChains()


# BattleManager is defined inside the battle screen.