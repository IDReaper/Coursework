# msdie.py

"""msdie.py
Provide a simple class for modeling an n-sided die."""

from random import randrange

class MSDie:

    """Simulate the operation of an n-sided die."""

    def __init__ (self, sides):
        """Create an n-sided class. Default to a 6-sided die."""
        self.sides = sides
        self.value = 1

    def roll (self):
        """Roll the die."""
        self.value = randrange (1, self.sides+1)

    def getValue (self):
        """Retrieve the face value of the die."""
        return self.value

    def setValue (self, value):
        """Cheating, force the die to the given value."""
        self.value = value

def main ():
    x = input("Enter sides: ")
    die = MSDie(x)
    roll = input("Roll how many times?: ")
    for i in range(roll):
        die.roll()
        print die.getValue()
