# Commented possibly better than other files.
# At the time of writing this line, this code works standalone perfectly.

# Transform that the notice uses.
transform noticeDisappear():

    # Top middle screen, visible
    align (0.5, 0.25) alpha 1.0

    # Going up and disappearing
    linear 4.0 yoffset -400 alpha 0.0

init -15 python:

    # Displayable.
    class NoticeManager(renpy.Displayable):

        # When defined.
        # noticeDuration is a float number, for how long the notices stay on screen.
        def __init__(self, noticeDuration, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(NoticeManager, self).__init__(**kwargs)

            # Children (notices) currently registered.
            self.currentChildren = []

            # Records the st 
            self.noticesTimes = {}

        # Adds a new notice.
        # Kwargs given are passed to Text.
        def addNotice(self, text, **kwargs):

            # Adds a new Text object to the current children.
            # Text creates a text displayable.
            # At makes it use the noticeDisappear transform.
            self.currentChildren.append( At( Text(text, **kwargs), noticeDisappear) )

        # Triggered with every interaction and renpy.redraw.
        def render(self, width, height, st, at):

            # Run this function again once possible.
            # This is so that Transforms can update (move).
            renpy.redraw(self, 0)

            # Create a render (canvas).
            render = renpy.Render(width, height)

            # For every child (notice) currently registered:
            for shownChild in self.currentChildren:

                # Place the child onto the render (canvas).
                render.place(shownChild)

            # Show the render.
            return render

        # Triggered on events - keypresses, mouse movements...
        def event(self, ev, x, y, st):

            # Pass the event to our children.
            # This object doesn't do anything on events, but children might.

            for child in self.currentChildren:
                child.event(ev, x, y, st)

        # Honestly not sure what this does.
        # It has to return a list of all the children shown.
        def visit(self):
            return [ child for child in self.currentChildren ]

# NoticeManager is defined inside a screen.