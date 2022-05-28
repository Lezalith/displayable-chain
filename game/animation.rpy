init -30 python:

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
    # triggerDelay is the delay of triggering trigger action.

    class Animation():

        def __init__(self, image, transform, duration, trigger = False, triggerDelay = 0.0):

            # Info about the Animation
            self.image = image
            self.transform = transform
            self.duration = duration

            # Info about triggers - marks for Manager to do stuff.
            self.trigger = trigger
            self.triggerDelay = triggerDelay

        # Returns the Animation, self.image at self.transform.
        def getChild(self):

            return At( self.image, self.transform )

image attackGif:
    xysize (200, 200) align (0.5, 0.5)
    "images/attack/attack1.png"
    pause 0.1
    "images/attack/attack2.png"
    pause 0.1
    "images/attack/attack3.png"
    pause 0.1
    "images/attack/attack4.png"
    pause 0.1