# Commented possibly better than other files.
# At the time of writing this line, this code works standalone perfectly.

# Transform that the notice uses.
transform noticeDisappear():

    # Top middle screen, visible
    align (0.5, 0.25) alpha 1.0

    # Going up and disappearing
    linear 3.0 yoffset -250 alpha 0.0

init -15 python:

    # Displayable.
    class NoticeManager(renpy.Displayable):

        # When defined.
        # noticeDuration is a float number, for how long the notices stay on screen.
        def __init__(self, noticeDuration, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(NoticeManager, self).__init__(**kwargs)

            # For how long a notice is on screen.
            self.noticeDuration = noticeDuration

            # Children (notices) currently registered.
            self.currentChildren = []

            # Current st, recorded in the render function. 
            self.st = 0.0

            # A dictionary.
            # keys are children from self.currentChildren.
            # values are st of when that child was shown (notice was added).
            self.noticesTimes = {}

        # Adds a new notice.
        # Kwargs given are passed to Text.
        def addNotice(self, text, **kwargs):

            # Adds a new Text object to the current children.
            # Text creates a text displayable.
            # At makes it use the noticeDisappear transform.
            self.currentChildren.append( At( Text(text, **kwargs), noticeDisappear) )

            # Register the st of when this notice was added.
            # -1 to get the last item on the list, since we just appended it.
            self.noticesTimes[self.currentChildren[-1]] = self.st

        # Triggered with every interaction and renpy.redraw.
        def render(self, width, height, st, at):

            # Update the st variable.
            self.st = st

            # Checks for notices that should be removes.
            self.checkForRemovals()

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

        # Checks whether any notices have gone past noticeDuration, and remove them if so.
        def checkForRemovals(self):

            # List of items to remove once the for loop is done.
            # We shouldn't remove/append stuff while iterating over it.
            removedKeys = []

            # Checking all the notices...
            for notice in self.noticesTimes.keys():

                # If the current time >= time when this was shown + noticeDuration: 
                if self.st >= self.noticesTimes[notice] + self.noticeDuration:

                    # Remove the child.
                    self.currentChildren.remove(notice)

                    # Set the key to be deleted.
                    removedKeys.append(notice)

            # Get rid of keys belonging to deleted notices.
            # Theoretically no harm in keeping them there, but it's good to keep clean after oneself.
            for key in removedKeys:
                del self.noticesTimes[key]

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