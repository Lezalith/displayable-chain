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
transform enterTrans():

    xalign 0.3 yalign 0.5 xoffset -600 alpha 0.0
    linear 1.0 xoffset 0 alpha 1.0

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

image enterState = Composite(
    (200, 200),
    (0, 0), Solid("ffff7e"),
    (0, 0), Text("entering", size = 40, color = "00f"))

image idleState = Composite(
    (200, 200),
    (0, 0), Solid("ff0"),
    (0, 0), Text("idle", size = 40, color = "00f"))

image moveState = Composite(
    (200, 200),
    (0, 0), Solid("f70"),
    (0, 0), Text("moving", size = 40, color = "00f"))

image attackState = Composite(
    (200, 200),
    (0, 0), Solid("f00"),
    (0, 0), Text("attacking", size = 40, color = "00f"))


# Animation definitions, put together from Transforms and Images defined above.
define enter = Animation("enterState", enterTrans, 1.0)
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
default ourFancyChain = AnimationChain( enter, idle, moveForward, attack, moveBack )


# Testing screen.
screen chainScreen():

    vbox:

        # Buttons
        hbox:
            spacing 20

            textbutton "Spawn" action Function(ourFancyChain.spawn)
            textbutton "Attack" action Function(ourFancyChain.moveForward)

        # State info
        # Um... Why does this not update correctly?
        text "Current state: [ourFancyChain.state]"

    # adding our CDD.
    add ourFancyChain


# The game starts here.
label start:

    # Jump right to the testing screen.
    call screen chainScreen

    return
