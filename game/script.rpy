


# init -20 python:

#     # A chain of animations.
#     #
#     # It currently has four states - idle, moving forward, attacking and moving back.
#     # 
#     # moveForward() starts the chain. 
#     class AnimationChain(renpy.Displayable):

#         def __init__(self, enterAnimation, idleAnimation, moveForwardAnimation, attackAnimation, moveBackAnimation, hitAnimation, **kwargs):

#             # Pass additional properties on to the renpy.Displayable
#             # constructor.
#             super(AnimationChain, self).__init__(**kwargs)

#             # Current Animation.
#             self.currentAnimation = None
#             # -1 - entering, 0 - idle, 1 - moving forward, 2 - attacking, 3 - moving back, 4 - hit
#             self.state = None

#             # Current displayable displayed.
#             self.currentChild = Null()

#             # All possible animations.
#             self.enterAnimation = enterAnimation
#             self.idleAnimation = idleAnimation
#             self.moveForwardAnimation = moveForwardAnimation
#             self.attackAnimation = attackAnimation
#             self.moveBackAnimation = moveBackAnimation
#             self.hitAnimation = hitAnimation

#             # Setting this to True starts the process of getting hit,
#             # and it is reset to False when the process ends.
#             self.hitReset = False

#             # Modifies st. This is how the chaining works.
#             self.st = 0
#             self.stOffset = 0

#         # Updates the child. Called when the currentAnimation is changed.
#         def setAnimation(self, anim):

#             self.currentAnimation = anim
#             self.currentChild = self.currentAnimation.getChild()

#         def spawn(self):

#             self.setAnimation( self.enterAnimation )
#             self.changeState(-1)

#         # Sets the state to idle.
#         def idle(self):

#             self.setAnimation( self.idleAnimation )
#             self.changeState(0)

#         # Sets the state to moving forward.
#         def moveForward(self):

#             self.setAnimation( self.moveForwardAnimation )
#             self.changeState(1)

#         # Sets the state to attacking.
#         def attack(self):

#             self.setAnimation( self.attackAnimation )
#             self.changeState(2)

#         # Sets the state to moving back.
#         def moveBack(self):

#             self.setAnimation( self.moveBackAnimation )
#             self.changeState(3)

#         def gotHit(self):

#             self.setAnimation( self.hitAnimation )
#             self.changeState(4)

#         # Changes the state and updates stOffset.
#         def changeState(self, state):

#             self.stOffset = self.st
#             self.state = state
#             print("State of {} is now {}.".format(self, self.state))

#             renpy.restart_interaction()

#         def triggerHit(self):

#             # So that this doesn't keep on triggering.
#             self.hitReset = True

#             self.gotHit()


#         # Displayable that is displayed. Called with every renpy.redraw.
#         def render(self, width, height, st, at):

#             # Records the st, for when stOffset needs to be updated.
#             self.st = st

#             # This makes st ignore time spent with previous states,
#             # making it seem like a changing a state shows a new image.
#             st = st - self.stOffset

#             # Check if entering
#             if self.state == -1:

#                 # If the transform has finished
#                 if st > self.currentAnimation.duration:

#                     # Enter the idle state.
#                     self.idle()

#             # Check if moving forward
#             elif self.state == 1:

#                 # If the transform has finished
#                 if st > self.currentAnimation.duration:

#                     # Enter the attack state.
#                     self.attack()

#             # Check if attacking
#             elif self.state == 2:

#                 # If the transform has finished
#                 if st > self.currentAnimation.duration:

#                     # Enter the moving back state.
#                     self.moveBack()

#             # Check if moving back OR got hit
#             elif self.state == 3 or self.state == 4:

#                 # If the transform has finished
#                 if st > self.currentAnimation.duration:

#                     # Reset the blocking var.
#                     self.hitReset = False

#                     # Return back to the idle state.
#                     self.idle()

#             # Trigger this function again.
#             # This could be under an "if not self.state == 0",
#             # but that causes self.st to update one interaction too late.
#             renpy.redraw(self, 0)

#             # Rendering the current child.
#             t = self.currentChild
#             render = renpy.Render(width, height)
#             render.place(t)
#             return render

#         # Triggered when an event happens - mouse movement, key press...
#         def event(self, ev, x, y, st):

#             # Pass the event to our child.
#             return self.currentChild.event(ev, x, y, st)

#         # Honestly not sure what this does.
#         def visit(self):
#             return [ self.currentChild ]


# Defines our CDD.
# default ourFancyChain = AnimationChain( enter, idle, moveForward, attack, moveBack )




# # Defines the Manager.
# default m = Manager( ally = AnimationChain( enter, idle, moveForward, attack, moveBack, hit ),
#                     enemy = AnimationChain( enterEnemy, idleEnemy, moveForwardEnemy, attackEnemy, moveBackEnemy, hitEnemy ) )



# The game starts here.
label start:

    # Jump right to the testing screen.
    call screen chainScreen

    return
