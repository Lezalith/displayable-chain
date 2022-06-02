transform noticeDisappear():

    align (0.5, 0.15) alpha 1.0

    linear 3.0 yoffset -200 alpha 0.0

# Calculated from the transform.
define noticeDuration = 3.0

init -15 python:

    class NoticeManager(renpy.Displayable):

        def __init__(self, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(NoticeManager, self).__init__(**kwargs)

            # Notices currently shown.
            self.currentChildren = []

        def addNotice(self, text):

            self.currentChildren.append( At(Text(text), noticeDisappear) )

        def render(self, width, height, st, at):

            renpy.redraw(self, 0)

            render = renpy.Render(width, height)

            for shownChild in self.currentChildren:

                render.place(shownChild)

            return render

        def event(self, ev, x, y, st):

            # Pass the event to our child.

            for child in self.currentChildren:
                child.event(ev, x, y, st)

        def visit(self):
            return [ child for child in self.currentChildren ]

# NoticeManager is defined inside the battle screen.