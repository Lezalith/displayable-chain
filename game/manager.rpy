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

        def checkForCollision(self):

            # Ally attacking
            if self.allyChain.state == 2:

                # So that the hit is only triggered once.
                if not self.enemyChain.hitReset:
                    self.enemyChain.triggerHit()

            # Enemy attacking
            elif self.enemyChain.state == 2:

                # So that the hit is only triggered once.
                if not self.allyChain.hitReset:
                    self.allyChain.triggerHit()

        def render(self, width, height, st, at):

            self.checkForCollision()

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


# # Defines the Manager.
# default m = Manager( ally = AnimationChain( enter, idle, moveForward, attack, moveBack, hit ),
#                     enemy = AnimationChain( enterEnemy, idleEnemy, moveForwardEnemy, attackEnemy, moveBackEnemy, hitEnemy ) )