# characters.py

# This class handles the creation of the game characters

from graphics import *

class Character:
    def __init__(self, center, radius, win):
        self.win = win
        self.center = center
        self.radius = radius
    
    def drawGhost(self):
        self.circle = Circle(self.center, self.radius)
        self.circle.setFill('red')
        self.circle.draw(self.win)

    def drawPacman(self):
        self.circle = Circle(self.center, self.radius)
        self.circle.setFill('yellow')
        self.circle.draw(self.win)

    def getCenter(self):
        return self.circle.getCenter()
    
    def move(self, x, y):
        self.circle.move(x, y)
