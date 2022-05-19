init python:

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


# Transforms used by the AnimationChain
transform idleTrans():

    xalign 0.3 yalign 0.5

transform moveForwardTrans():

    xalign 0.3 yalign 0.5
    linear 1.0 xalign 0.7

transform attackTrans():

    xalign 0.7 yalign 0.5
    linear 0.3 xoffset 50
    linear 0.3 xoffset 0

transform moveBackTrans():

    xalign 0.7 yalign 0.5
    linear 1.0 xalign 0.3


# Images definitions
define stateSize = Transform( xysize = (200, 200) )

image idleState = At( Solid("ff0"), stateSize)
image moveState = At( Solid("f70"), stateSize)
image attackState = At( Solid("f00"), stateSize)


# Animation definitions, put together from Transforms and Images defined above.
define idle = Animation("idleState", idleTrans, 0)
define moveForward = Animation("moveState", moveForwardTrans, 1.0)
define attack = Animation("attackState", attackTrans, 0.6)
define moveBack = Animation("moveState", moveBackTrans, 1.0)


init python:

    # A chain of animations.
    #
    # It currently has four states - idle, moving forward, attacking and moving back.
    # 
    # moveForward() starts the chain. 
    class AnimationChain(renpy.Displayable):

        def __init__(self, idleAnimation, moveForwardAnimation, attackAnimation, moveBackAnimation, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(AnimationChain, self).__init__(**kwargs)

            # Current Animation.
            self.currentAnimation = None
            # 0 - idle, 1 - moving forward, 2 - attacking, 3 - moving back
            self.state = None

            # Current displayable displayed.
            self.currentChild = Null()

            # All possible animations.
            self.idleAnimation = idleAnimation
            self.moveForwardAnimation = moveForwardAnimation
            self.attackAnimation = attackAnimation
            self.moveBackAnimation = moveBackAnimation

            # Modifies st. This is how the chaining works.
            self.st = 0
            self.stOffset = 0

            # Chains the images if True.
            # At least for now, I'm keeping the ability to play out the states manually.
            self.chain = True

        # Updates the child. Called when the currentAnimation is changed.
        def setAnimation(self, anim):

            self.currentAnimation = anim
            self.currentChild = At( self.currentAnimation.image, self.currentAnimation.transform )

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

        # Displayable that is displayed. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            # Records the st, for when stOffset needs to be updated.
            self.st = st

            # Keeping the chain process togglable for now.
            if self.chain:

                # This makes st ignore time spent with previous states,
                # making it seem like a changing a state shows a new image.
                st = st - self.stOffset

                # Check if moving forward
                if self.state == 1:

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
default ourFancyChain = AnimationChain( idle, moveForward, attack, moveBack )


# Testing screen.
screen chainScreen():

    vbox:

        # Buttons that change states
        hbox:
            spacing 20

            textbutton "Idle" action Function(ourFancyChain.idle)
            textbutton "Move to attack" action Function(ourFancyChain.moveForward)
            textbutton "Attack" action Function(ourFancyChain.attack)
            textbutton "Move back" action Function(ourFancyChain.moveBack)

        # Button that toggles chaining on and off.
        hbox:
            spacing 20

            textbutton "Toggle Chain" action ToggleVariable("ourFancyChain.chain", true_value = True, false_value = False)
            text "Chained: [ourFancyChain.chain]"

    # adding our CDD.
    add ourFancyChain


# The game starts here.
label start:

    # Jump right to the testing screen.
    call screen chainScreen

    return
