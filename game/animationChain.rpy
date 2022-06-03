init -20 python:

    # A chain of Animations.
    #
    # Arguments are Animations in the order they should be chained together.

    class AnimationChain(renpy.Displayable):

        def __init__(self, *args, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(AnimationChain, self).__init__(**kwargs)

            # List of all Animation objects.
            self.animations = args
            # print(self.animations)

            # Default displayable, when no Animation from self.animations is used.
            self.defaultChild = Null()
            
            # Index of current animation in self.animations.
            # -1 shows self.defaultChild.
            self.pointer = -1

            # Current Animation from self.animations[self.pointer].
            # None if self.pointer is -1.
            self.currentAnimation = None

            # Rendered child of this Displayable.
            self.currentChild = self.defaultChild

            # Monitors st and resets it whenever an Animation used is changed.
            # This is how the chaining works - reset of st makes the next transition think it was just shown.
            self.st = 0.0
            self.stOffset = 0.0

            # Causes the chain to start next time render is called.
            # (Explained near beginChain below)
            self.setToBegin = False

            # When chain finishes, True makes it stay on the last animation, and False puts it back on self.defaultChild.
            # TODO: How does return None in render function fit into this? 
            self.finished = False

        # Makes chain start on next render call.
        # If we were to trigger it right away (run triggerChain instead), self.stOffset would not update correctly.
        def beginChain(self):

            self.setToBegin = True

            self.finished = False

            # print("Chain about to begin.")

        # Actually starts the chain.
        def triggerChain(self):

            self.getChainDuration()

            # Simulates st starting from 0.
            self.stOffset = self.st

            # print("chain reset at st of {}".format(self.st))

            self.finished = False

            # Point at the first Animation in self.animations and updates self.currentChild.
            self.pointer = 0
            self.updateAnimation()

        # Updates currentAnimation and currentChild.
        def updateAnimation(self):

            # print("Updating animation. Pointer: {}".format(self.pointer))

            self.currentAnimation = self.animations[ self.pointer ]
            self.currentAnimation.reset()
            
            self.currentChild = self.currentAnimation.getChild()

            # Could be used to update stats on screen.
            # renpy.restart_interaction()

        def getChainDuration(self):

            duration = sum([animation.duration for animation in self.animations])

            print("Duration of current chain: {}".format(duration))

            return duration




        # Advances the Chain to the next Animation on the self.animations list.
        def advance(self):

            # Unless the next pointer would go outside the list:
            if self.pointer + 1 < len( self.animations ):

                # print("advancing to {} at st of {}".format(self.pointer, self.st))

                # Simulates st starting from 0.
                self.stOffset = self.st

                # Advance the pointer...
                self.pointer += 1

                # ...and update the animation used.
                self.updateAnimation()

            # This was the last Animation in the list.
            else:
                self.finished = True

        # Checks for a trigger inside of self.currentAnimation.
        def checkTrigger(self):

            # If there is a currentAnimation (None if the Chain is not active):
            if self.currentAnimation is not None:

                print("Animation is not None")

                # If that Animation has a trigger:
                if self.currentAnimation.trigger:

                    print("Animation has a trigger.")

                    # If the Animation has any more triggers remaining:
                    if self.currentAnimation.canAdvance():

                        print("The animation can advance.")

                        # If our st has gone past the delay of the current trigger:
                        if self.st - self.stOffset > self.currentAnimation.getCurrentDelay():

                            print("Triggering a hit at {}.".format(self.st))

                            self.currentAnimation.advancePointer()

                            # Triggers the thing.
                            return True

            # Nothing triggers.
            return False

        # Returns a displayable that is to be displayed. Called with every renpy.redraw.
        def render(self, width, height, st, at):

            # print("render of {}. Current pointer: {}".format(self, self.pointer))

            # Render where we place stuff to show.
            render = renpy.Render(width, height)

            # Records the st, for when stOffset needs to be updated.
            self.st = st

            # This triggers this function again after it finishes.
            # This could be under an "if not self.pointer == -1",
            # but that causes self.st to update one frame too late.
            renpy.redraw(self, 0)

            # Triggers the chain if it is set to begin..
            if self.setToBegin is True:

                self.setToBegin = False
                self.triggerChain()

            # Use self.defaultChild when the chain has not started (or was reset).
            if self.pointer == -1:

                # print("placing def child")

                # Add the defaultChild inside the render and return it.
                t = self.defaultChild
                render.place(t)
                return render

            # print("not placing def child")

            # Simulates st starting from 0.
            st = self.st - self.stOffset

            # If current Animation's duration has elapsed...
            if st > self.currentAnimation.duration:

                # ...advance the Chain.
                self.advance()

            # Add currentChild inside the render and return it.
            t = self.currentChild
            render.place(t)
            return render

        # Triggered when an event happens - mouse movement, key press...
        def event(self, ev, x, y, st):

            # Pass the event to our child.
            return self.currentChild.event(ev, x, y, st)

        # Honestly not sure what this does, but it needs to return all displayables rendered.
        def visit(self):
            return [ self.currentChild ]

# Chains used by Ally Character.
default allySpawnChain = AnimationChain( enter, idle )
default allyAttackChain = AnimationChain( moveForward, attack, moveBack, idle )
default allyHitChain = AnimationChain( hit, idle )

default allyAttackHeavyChain = AnimationChain( moveForward, attackHeavy, attackHeavy, moveBack, idle )
default allyAttackFastChain = AnimationChain( moveForward, attackFast, moveBack, idle )

default allyDeathChain = AnimationChain( death )

default allySpellChain = AnimationChain( death, spellAnimation, enter, idle )


# Chains used by Enemy Character.
default enemySpawnChain = AnimationChain( enterFancyEnemy, idleEnemy )
default enemyAttackChain = AnimationChain( moveForwardEnemy, attackEnemy, moveBackEnemy, idleEnemy )
default enemyHitChain = AnimationChain( hitEnemy, idleEnemy)
default enemyHitFancyChain = AnimationChain( hitFancyEnemy, idleEnemy)
default enemyDeathChain = AnimationChain( deathEnemy )
