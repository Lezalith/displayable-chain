init python:

    class Animation():

        def __init__(self, image, transform, duration):

            self.image = image
            self.transform = transform
            self.duration = duration

            self.displayable = At( self.image, self.transform )


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


define stateSize = Transform( xysize = (200, 200) )

define idleState = At( Solid("ff0"), stateSize)
define moveState = At( Solid("f70"), stateSize)
define attackState = At( Solid("f00"), stateSize)


define idle = Animation(idleState, idleTrans, 0)
define moveForward = Animation(moveState, moveForwardTrans, 1.0)
define attack = Animation(attackState, attackTrans, 0.6)
define moveBack = Animation(moveState, moveBackTrans, 1.0)


init python:

    class AnimationChain(renpy.Displayable):

        def __init__(self, idleAnimation, moveForwardAnimation, attackAnimation, moveBackAnimation, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(AnimationChain, self).__init__(**kwargs)

            self.currentChild = Null()
            self.currentAnimation = None

            # The children.
            self.idleAnimation = idleAnimation
            self.moveForwardAnimation = moveForwardAnimation
            self.attackAnimation = attackAnimation
            self.moveBackAnimation = moveBackAnimation

            # 0 - idle, 1 - moving forward, 2 - attacking, 3 - moving back
            self.state = None

            self.st = 0
            self.stOffset = 0

            # Chains the images if True.
            self.chain = True

        def updateChild(self):

            self.currentChild = At( self.currentAnimation.image, self.currentAnimation.transform )

        def idle(self):

            self.currentAnimation = self.idleAnimation
            self.changeState(0)

            self.updateChild()


        def moveForward(self):

            self.currentAnimation = self.moveForwardAnimation
            self.changeState(1)

            self.updateChild()

        def attack(self):

            self.currentAnimation = self.attackAnimation
            self.changeState(2)

            self.updateChild()

        def moveBack(self):

            self.currentAnimation = self.moveBackAnimation
            self.changeState(3)

            self.updateChild()

        def changeState(self, state):

            self.stOffset = self.st
            self.state = state

        def render(self, width, height, st, at):

            self.st = st

            # Togglable for test purposes
            if self.chain:

                st = st - self.stOffset

                # Check if moving forward
                if self.state == 1:

                    # Check if trans finished
                    if st > self.currentAnimation.duration:

                        self.attack()

                elif self.state == 2:

                    # Check if trans finished
                    if st > self.currentAnimation.duration:

                        self.moveBack()

                elif self.state == 3:

                    # Check if trans finished
                    if st > self.currentAnimation.duration:

                        self.idle()

            renpy.redraw(self, 0)

            t = self.currentChild
            render = renpy.Render(width, height)
            render.place(t)
            return render

        def event(self, ev, x, y, st):

            # Pass the event to our child.
            return self.currentChild.event(ev, x, y, st)

        def visit(self):
            return [ self.currentChild ]



default ourFancyChain = AnimationChain( idle, moveForward, attack, moveBack )


screen chainScreen():

    vbox:

        hbox:
            spacing 20

            textbutton "Idle" action Function(ourFancyChain.idle)
            textbutton "Move to attack" action Function(ourFancyChain.moveForward)
            textbutton "Attack" action Function(ourFancyChain.attack)
            textbutton "Move back" action Function(ourFancyChain.moveBack)

        hbox:
            spacing 20

            textbutton "Toggle Chain" action ToggleVariable("ourFancyChain.chain", true_value = True, false_value = False)
            text "Chained: [ourFancyChain.chain]"

    add ourFancyChain


# The game starts here.

label start:

    call screen chainScreen

    return