init -30 python:

    # Ren'Py actually has an Animation displayable, which this overrides,
    # but I really don't think we will miss the original.
    #
    # Animation holds information about one state the Character be in.
    # image is the image of the state
    # transform is the transform of the state
    # duration is for how long the state sticks around - it has to be calculated manually, and is ignored ignored for idle state 
    class Animation():

        def __init__(self, image, transform, duration, triggers = False):

            self.image = image
            self.transform = transform
            self.duration = duration

            # Whether it triggers an animation.
            self.triggers = triggers

            ##### TODO: NOT GONNA WORRY ABOUT THIS RIGHT NOW #####
            # Delay before this animation starts.
            self.delay = None
            # Delay before the animations this one triggers start.
            self.delays = None
            ######################################################

        def getChild(self):

            return At( self.image, self.transform )


init -20 python:

    enter = Animation("enterState", enterTrans, 1.0)
    enter2 = Animation("enterState", enterTrans, 1.0)
    idle = Animation("idleState", idleTrans, 0)
    moveForward = Animation("moveState", moveForwardTrans, 1.0)
    attack = Animation("attackState", attackTrans, 0.6, triggers = True)
    moveBack = Animation("moveState", moveBackTrans, 1.0)
    hit = Animation("hitState", hitTrans, 0.6)


    enterEnemy = Animation("enterStateEnemy", enterTransEnemy, 1.0)
    idleEnemy = Animation("idleStateEnemy", idleTransEnemy, 0)
    moveForwardEnemy = Animation("moveStateEnemy", moveForwardTransEnemy, 1.0)
    attackEnemy = Animation("attackStateEnemy", attackTransEnemy, 0.6, triggers = True)
    moveBackEnemy = Animation("moveStateEnemy", moveBackTransEnemy, 1.0)
    hitEnemy = Animation("hitStateEnemy", hitTransEnemy, 0.6)


init -20 python:

    # A chain of animations.
    class AnimationChain(renpy.Displayable):

        def __init__(self, *args, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(AnimationChain, self).__init__(**kwargs)

            self.animations = args

            # print(self.animations)

            # Default displayable.
            self.defaultChild = Null()
            
            # Index of current animation in self.animations.
            # -1 shows self.defaultChild
            self.pointer = -1

            # Current Animation from self.animations[self.pointer]
            self.currentAnimation = None

            # Current displayable displayed.
            self.currentChild = self.defaultChild

            # Modifies st. This is how the chaining works - reset of st allows new transition to follow.
            self.st = 0.0
            self.stOffset = 0.0

            # Causes the chain to begin next time render is called.
            self.setToBegin = False

            # When chain finishes, True makes it stay on the last animation, and False puts it back on self.defaultChild.
            # TODO: How does return None in render function fit into this? 
            self.endOnLast = True

        # Makes chain begin on next render call.
        def beginChain(self):

            print("Chain about to begin.")

            self.setToBegin = True

        # Actual start of the chain.
        def firstAnimation(self):

            self.stOffset = self.st

            print("pointer set to 0 at st of {}".format(self.st))

            self.pointer = 0
            self.updateAnimation()

        # Resets the chain back to self.defaultChild
        def reset(self):

            self.pointer = -1
            self.st = 0.0
            self.stOffset = 0.0

        # Updates currentChild and currentAnimation.
        def updateAnimation(self):

            print("Updating animation. Pointer: {}".format(self.pointer))

            self.currentAnimation = self.animations[ self.pointer ]
            self.currentChild = self.currentAnimation.getChild()

            # Could be used to update stats on screen.
            # renpy.restart_interaction()

        def advance(self):

            # Unless the next pointer would go outside the list...
            if self.pointer + 1 < len( self.animations ):

                # Advance the pointer...
                self.pointer += 1

                self.stOffset = self.st

                print("advancing to {} at st of {}".format(self.pointer, self.st))

                # ...and update the animation used.
                self.updateAnimation()

            else:
                # This was the last animation.


                # If this chain was given endOnLast = False, reset the chain.
                if not self.endOnLast :
                    print("reseting")
                    self.reset()

        def checkTrigger(self):

            if self.currentAnimation is not None:

                return self.currentAnimation.triggers

            return False

        # Returns a displayable that is to be displayed. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            print("render. Current pointer: {}".format(self.pointer))

            # Render where we place stuff to show.
            render = renpy.Render(width, height)

            # Records the st, for when stOffset needs to be updated.
            self.st = st

            # This triggers this function again after it finishes.
            # This could be under an "if not self.pointer == -1",
            # but that causes self.st to update one interaction too late.
            renpy.redraw(self, 0)

            # Starts the chain.
            if self.setToBegin is True:

                self.setToBegin = False
                self.firstAnimation()

            # Using self.defaultChild when the chain has not started (or was reset).
            if self.pointer == -1:

                # print("placing def child")

                t = self.defaultChild
                render.place(t)
                return render

            # print("not placing def child")

            # print("st: {}, offset: {}, result: {}, duration: {}".format(st, self.stOffset, self.st - self.stOffset, self.currentAnimation.duration))

            # This makes st ignore time spent with previous states,
            # making it seem like changing a state shows a new image.
            st = self.st - self.stOffset

            # If animation's duration has elapsed...
            if st > self.currentAnimation.duration:

                # ...advance the pointer.
                self.advance()

            # Rendering the current child.
            t = self.currentChild
            render.place(t)
            return render

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our child.
            return self.currentChild.event(ev, x, y, st)

        # Honestly not sure what this does.
        def visit(self):
            return [ self.currentChild ]

default allySpawnChain = AnimationChain( enter, idle )
default allyAttackChain = AnimationChain( moveForward, attack, moveBack, idle )
default allyHitChain = AnimationChain( hit, idle )

default enemySpawnChain = AnimationChain( enterEnemy, idleEnemy )
default enemyAttackChain = AnimationChain( moveForwardEnemy, attackEnemy, moveBackEnemy, idleEnemy )
default enemyHitChain = AnimationChain( hitEnemy, idleEnemy)
