init -10 python:

    # Controls the Battle.
    #
    # Arguments:
    # ally is the player
    # enemy is the opponent
    # TODO: Make these into lists for multiple participants in a battle!
    class BattleManager(renpy.Displayable):

        def __init__(self, ally, enemy, **kwargs):

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

        # Begins the battle.
        # Currently only spawns the participants.
        def start(self):

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

            # Ally attacking
            if type == "ally":

                # Trigger an AnimationChain of the attack.
                self.allyCharacter.attack( attack )

                # Set attacking character and attacked character.
                self.attacking = self.allyCharacter
                self.attacked = self.enemyCharacter

            # Enemy attacking
            elif type == "enemy":

                # Trigger an AnimationChain of the attack.
                self.enemyCharacter.attack( attack )

                # Set attacking character and attacked character.
                self.attacking = self.enemyCharacter
                self.attacked = self.allyCharacter

            self.currentAttack = attack

        # Triggers the hit AnimationChain of the attacked character.
        def checkHit(self):

            # Check whether the current Animation of attacking Character has a trigger and whether it's gone off.
            if self.attacking.getChain().checkTrigger():

                # Trigger hit AnimationChain of attacked.
                self.attacked.hit( self.currentAttack )

                # Reset attacking and attacked characters.
                # TODO: This will probably be done elsewhere, once the Battle has been split into phases.
                self.attacking = None
                self.attacked = None
                self.currentAttack = None

        # Renders all displayables held. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            # Check if someone is attacking. If so, check if they should trigger a hit.
            if self.attacking is not None:
                self.checkHit()

            # Prepare a render. It is the size of the whole screen.
            render = renpy.Render(config.screen_width, config.screen_height)

            # Places every displayable held into the render.
            for chain in self.getChildrenChains():

                # print("placing {}".format(chain))

                t = Transform(child = chain)
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

        # Honestly not sure what this does, but it needs to return all displayables rendered.
        def visit(self):
            return self.getChildrenChains()


# # Defines the BattleManager.
default m = BattleManager( ally = allyCharacter, enemy = enemyCharacter )