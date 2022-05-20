init -30 python:

    # Ren'Py actually has an Animation displayable, which this overrides,
    # but I really don't think we will miss the original.
    #
    # Animation holds information about one state the Character be in.
    # image is the image of the state
    # transform is the transform of the state
    # duration is for how long the state sticks around - it has to be calculated manually, and is ignored ignored for idle state 
    class Animation():

        def __init__(self, image, transform, duration):

            self.image = image
            self.transform = transform
            self.duration = duration


init -20 python:

    # A chain of animations.
    #
    # It currently has four states - idle, moving forward, attacking and moving back.
    # 
    # moveForward() starts the chain. 
    class AnimationChain(renpy.Displayable):

        def __init__(self, enterAnimation, idleAnimation, moveForwardAnimation, attackAnimation, moveBackAnimation, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(AnimationChain, self).__init__(**kwargs)

            # Current Animation.
            self.currentAnimation = None
            # -1 - entering, 0 - idle, 1 - moving forward, 2 - attacking, 3 - moving back
            self.state = None

            # Current displayable displayed.
            self.currentChild = Null()

            # All possible animations.
            self.enterAnimation = enterAnimation
            self.idleAnimation = idleAnimation
            self.moveForwardAnimation = moveForwardAnimation
            self.attackAnimation = attackAnimation
            self.moveBackAnimation = moveBackAnimation

            # Modifies st. This is how the chaining works.
            self.st = 0
            self.stOffset = 0

        # Updates the child. Called when the currentAnimation is changed.
        def setAnimation(self, anim):

            self.currentAnimation = anim
            self.currentChild = At( self.currentAnimation.image, self.currentAnimation.transform )

        def spawn(self):

            self.setAnimation( self.enterAnimation )
            self.changeState(-1)

        # Sets the state to idle.
        def idle(self):

            self.setAnimation( self.idleAnimation )
            self.changeState(0)

        # Sets the state to moving forward.
        def moveForward(self):

            self.setAnimation( self.moveForwardAnimation )
            self.changeState(1)

        # Sets the state to attacking.
        def attack(self):

            self.setAnimation( self.attackAnimation )
            self.changeState(2)

        # Sets the state to moving back.
        def moveBack(self):

            self.setAnimation( self.moveBackAnimation )
            self.changeState(3)

        # Changes the state and updates stOffset.
        def changeState(self, state):

            self.stOffset = self.st
            self.state = state
            print("State of {} is now {}.".format(self, self.state))

            renpy.restart_interaction()

        # Displayable that is displayed. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            # Records the st, for when stOffset needs to be updated.
            self.st = st

            # This makes st ignore time spent with previous states,
            # making it seem like a changing a state shows a new image.
            st = st - self.stOffset

            # Check if entering
            if self.state == -1:

                # If the transform has finished
                if st > self.currentAnimation.duration:

                    # Enter the idle state.
                    self.idle()

            # Check if moving forward
            elif self.state == 1:

                # If the transform has finished
                if st > self.currentAnimation.duration:

                    # Enter the attack state.
                    self.attack()

            # Check if attacking
            elif self.state == 2:

                # If the transform has finished
                if st > self.currentAnimation.duration:

                    # Enter the moving back state.
                    self.moveBack()

            # Check if moving back
            elif self.state == 3:

                # If the transform has finished
                if st > self.currentAnimation.duration:

                    # Return back to the idle state.
                    self.idle()

            # Trigger this function again.
            # This could be under an "if not self.state == 0",
            # but that causes self.st to update one interaction too late.
            renpy.redraw(self, 0)

            # Rendering the current child.
            t = self.currentChild
            render = renpy.Render(width, height)
            render.place(t)
            return render

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our child.
            return self.currentChild.event(ev, x, y, st)

        # Honestly not sure what this does.
        def visit(self):
            return [ self.currentChild ]


# Defines our CDD.
# default ourFancyChain = AnimationChain( enter, idle, moveForward, attack, moveBack )


init -10 python:

    class Manager(renpy.Displayable):

        def __init__(self, ally, enemy, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Manager, self).__init__(**kwargs)

            self.allyChain = ally
            self.enemyChain = enemy

        def start(self):

            self.allyChain.spawn()
            self.enemyChain.spawn()

        def render(self, width, height, st, at):

            render = renpy.Render(config.screen_width, config.screen_height)

            t = Transform(child = self.allyChain)
            render.place(t)
            t = Transform(child = self.enemyChain)
            render.place(t)

            return render

        def event(self, ev, x, y, st):

            # Pass the event to our childen.
            self.allyChain.event(ev, x, y, st)
            self.enemyChain.event(ev, x, y, st)

        def visit(self):
            return [ self.allyChain, self.enemyChain ]


# Defines the Manager.
default m = Manager( ally = AnimationChain( enter, idle, moveForward, attack, moveBack ),
                    enemy = AnimationChain( enterEnemy, idleEnemy, moveForwardEnemy, attackEnemy, moveBackEnemy ) )


# Testing screen.
screen chainScreen():

    vbox:

        # Buttons
        hbox:
            spacing 20

            textbutton "Spawn" action Function(m.start), Function(m.start)
            textbutton "Ally Attack" action Function(m.allyChain.moveForward)
            textbutton "Enemy Attack" action Function(m.enemyChain.moveForward)

        # State info
        text "Current Ally state: [m.allyChain.state]"
        text "Current Enemy state: [m.enemyChain.state]"

        # Add info on currentAnimation and/or currentChild?

    # adding our CDD.
    add m


# The game starts here.
label start:

    # Jump right to the testing screen.
    call screen chainScreen

    return
