init -10 python:

    class Manager(renpy.Displayable):


        def __init__(self, ally, enemy, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Manager, self).__init__(**kwargs)

            self.allyCharacter = ally
            self.enemyCharacter = enemy

        def start(self):

            self.allyCharacter.enter()
            self.enemyCharacter.enter()

            renpy.redraw(self, 0)

        def getChildrenChains(self):

            return [self.allyCharacter.getChain(), self.enemyCharacter.getChain()]

        # def checkForCollision(self):

        #     # Ally attacking
        #     if self.allyChain.state == 2:

        #         # So that the hit is only triggered once.
        #         if not self.enemyChain.hitReset:
        #             self.enemyChain.triggerHit()

        #     # Enemy attacking
        #     elif self.enemyChain.state == 2:

        #         # So that the hit is only triggered once.
        #         if not self.allyChain.hitReset:
        #             self.allyChain.triggerHit()

        def attack(self, type):

            # ally attacking
            if type == "ally":
                self.allyCharacter.attack()

            # enemy attacking
            elif type == "enemy":
                self.enemyCharacter.attack()

        def render(self, width, height, st, at):

            # self.checkForCollision()

            render = renpy.Render(config.screen_width, config.screen_height)

            for chain in self.getChildrenChains():

                print("placing {}".format(chain))

                t = Transform(child = chain)
                render.place(t)

            return render

        def event(self, ev, x, y, st):

            # self.allyChain.event(ev, x, y, st)
            # self.enemyChain.event(ev, x, y, st)

            # Pass the event to our childen.
            for disp in self.getChildrenChains():

                if disp is not None:
                    disp.event(ev, x, y, st)

        def visit(self):
            return self.getChildrenChains()


# # Defines the Manager.
default m = Manager( ally = allyCharacter, enemy = enemyCharacter )