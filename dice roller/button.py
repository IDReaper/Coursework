# button.py

from myro import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate ()
    and deactivated () methods. The clicked (p) method
    returns true if the button is active and p is inside it."""

    def __init__ (self, win, center, width, height, label):
        """Creates a rectangular button. e.g.:
        qb = Button (myWin, centerPoint, width, height, 'Quit')"""

        w2 = width / 2.0
        h2 = height / 2.0
        x = center.getX ()
        y = center.getY ()

        self.xmin = x - w2
        self.xmax = x + w2
        self.ymin = y - h2
        self.ymax = y + h2

        p1 = Point (self.xmin, self.ymin)
        p2 = Point (self.xmax, self.ymax)

        self.rect = Rectangle (p1, p2)
        self.rect.setFill ('lightgray')
        self.rect.draw (win)

        self.label = Text (center, label)
        self.label.draw (win)

        self.deactivate ()

    def activate (self):
        """Sets this button to 'active'."""
        self.label.setFill ('black')
        self.rect.setWidth (2)
        self.active = True

    def deactivate (self):
        """Sets this button to 'inactive'."""
        self.label.setFill ('darkgrey')
        self.rect.setWidth (1)
        self.active = False

    def getLabel (self):
        """Returns the label string of this button."""
        return self.label.getText ()

    def clicked (self, p):
        """Returns true if button active and p is inside"""
        return self.active and \
               self.xmin <= p.getX () <= self.xmax and \
               self.ymin <= p.getY () <= self.ymax

def main ():
    win = GraphWin ('Button', 500, 400)
    qb = Button (win, Point (250, 200), 100, 50, 'Quit')
    qb.activate ()
    eb = Button (win, Point (100, 100), 100, 50, 'Exit')
