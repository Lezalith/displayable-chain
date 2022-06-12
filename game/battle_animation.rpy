init -50 python:

    # Ren'Py actually has an Animation displayable, which this overrides,
    # but I don't really think anybody would miss the original - It's outdated and not even documented anymore.
    #
    # Animation holds information about one state the AnimationChain can be in.
    #
    # Arguments:
    # image is the image/displayable of the state
    # transform is the transform of the state
    # duration is for how long the state sticks around - it has to be calculated manually!
    # trigger is False by default. True marks it for Manager to trigger an action.
    # triggerDelays is a list of delays of triggering trigger action.

    class BattleAnimation():

        def __init__(self, image, transform, duration, trigger = False, triggerDelays = [], filmstrip = False):

            # Info about the Animation
            self.image = image
            self.transform = transform
            self.duration = float(duration)

            # Info about triggers - marks for Manager to do stuff.
            self.trigger = trigger
            self.triggerDelays = triggerDelays

            # TODO: Filmstrip.
            self.filmstrip = filmstrip
            # If True, "image" should be a file, and putTogetherStrip is used at getChild. (???)

            if len(self.triggerDelays) == 0 and self.trigger:
                raise Exception("Animation has a trigger but no trigger delays.")

            # Pointing at the current delay from self.triggerDelays.
            self.delayPointer = 0

        def putTogetherStrip(self):

            return anim.Filmstrip(self.image, framesize = (120, 80), gridsize = (6, 1), delay = 0.1, loop = False)

        # Returns the Animation, self.image at self.transform.
        def getChild(self):

            # print("Getting pointer, now at: {}".format(self.delayPointer))

            return At( self.image, self.transform )

        # Reset of triggers.
        def reset(self):

            # print("Animation got reset.")

            self.delayPointer = 0

            if self.filmstrip:
                self.image = self.putTogetherStrip()

        # If the pointer can advance.
        # False if it would go outside of the triggerDelays list.
        # This is also used to check if Animation has gone past all the triggers.
        def canAdvance(self):

            return self.delayPointer < len(self.triggerDelays)

        # Advance the pointer to the next trigger.
        def advancePointer(self):

            self.delayPointer += 1

            # print("Advancing the pointer to {}".format(self.delayPointer))

        # Delay that is coming up next.
        def getCurrentDelay(self):

            # print("A delay was checked. My pointer is {}.".format(self.delayPointer))

            return self.triggerDelays[self.delayPointer]