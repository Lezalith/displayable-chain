init python:
    class TestChar(renpy.Displayable):

        def __init__(self, idleState, moveState, attackState, idleTrans, moveForwardTrans, attackTrans, moveBackTrans, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(TestChar, self).__init__(**kwargs)

            self.currentChild = Null()
            self.currentTrans = Transform()

            # The children.
            self.idleChild = idleState
            self.moveChild = moveState
            self.attackChild = attackState

            self.idleTrans = idleTrans
            self.moveForwardTrans = moveForwardTrans
            self.attackTrans = attackTrans
            self.moveBackTrans = moveBackTrans

            # 0 - idle, 1 - moving forward, 2 - attacking, 3 - moving back
            self.state = None

            self.st = 0
            self.stOffset = 0

            # Chains the images if True.
            self.chain = True

        def idle(self):

            self.currentChild = At( self.idleChild, self.idleTrans )
            self.changeState(0)

        def moveForward(self):

            self.currentChild = At( self.moveChild, self.moveForwardTrans )
            self.changeState(1)

        def attack(self):

            self.currentChild = At( self.attackChild, self.attackTrans )
            self.changeState(2)

        def moveBack(self):

            self.currentChild = At( self.moveChild, self.moveBackTrans )
            self.changeState(3)

        def changeState(self, state):

            self.stOffset = self.st
            self.state = state

            # renpy.redraw(self, 0)

        def render(self, width, height, st, at):

            self.st = st

            # Togglable for test purposes
            if self.chain:

                st = st - self.stOffset

                # Check if moving forward
                if self.state == 1:

                    # Check if trans finished
                    if st > 1.3:

                        self.attack()

                elif self.state == 2:

                    # Check if trans finished
                    if st > 0.8:

                        self.moveBack()

                elif self.state == 3:

                    # Check if trans finished
                    if st > 1.3:

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


define stateSize = Transform( xysize = (200, 200) )

define idleState = At( Solid("ff0"), stateSize)
define moveState = At( Solid("f70"), stateSize)
define attackState = At( Solid("f00"), stateSize)

default testDisp = TestChar( idleState, moveState, attackState, idleTrans, moveForwardTrans, attackTrans, moveBackTrans )


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


screen testScreen():

    vbox:

        hbox:
            spacing 20

            textbutton "Idle" action Function(testDisp.idle)
            textbutton "Move to attack" action Function(testDisp.moveForward)
            textbutton "Attack" action Function(testDisp.attack)
            textbutton "Move back" action Function(testDisp.moveBack)

        hbox:
            spacing 20

            textbutton "Toggle Chain" action ToggleVariable("testDisp.chain", true_value = True, false_value = False)
            text "Chained: [testDisp.chain]"

    add testDisp


# The game starts here.

label start:

    call screen testScreen

    return