# interfaces.py

# This class contains the three interfaces used during pacman:
# main menu interface 
# win interface 
# lose interface

from graphics import *

class Interface:

    def __init__(self, title, width, height):
        self.win = GraphWin(title, width, height)
        self.win.setBackground('black')
    
    def mainMenu(self):
        start = Rectangle(Point(150, 170), Point(250, 190))
        start.setFill('yellow')
        sLabel = Text(Point(200, 180), "Start")
        sLabel.setOutline('blue')
        
        ex = Rectangle(Point(150, 210), Point(250, 230))
        ex.setFill('yellow')
        eLabel = Text(Point(200, 220), "Exit")
        eLabel.setOutline('blue')

        start.draw(self.win)
        ex.draw(self.win)
        sLabel.draw(self.win)
        eLabel.draw(self.win)

        pt = self.win.getMouse()
        if 170 <= pt.getY() <= 190 and 150 <= pt.getX() <= 250:             # Start button
            self.win.close()
            return 1
        elif 210 <= pt.getY() <= 230 and 150 <= pt.getX() <= 250:           # Exit button
            self.win.close()
            return 0

        else:
            while (not 170 <= pt.getY() <= 190) or (not 210 <= pt.getY() <= 230 ) and (not 150 <= pt.getX() <= 250):
                pt = self.win.getMouse()
                if 170 <= pt.getY() <= 190 and 150 <= pt.getX() <= 250:     # Start button
                    self.win.close()
                    return 1
                elif 210 <= pt.getY() <= 230 and 150 <= pt.getX() <= 250:   # Exit button
                    self.win.close()
                    return 0

    def winnerWindow(self):
        message = Text(Point(200, 150), "Congrats! You Won!")
        message.setOutline('blue')
        
        question = Text(Point(200, 200), "Would you like to play again?")
        question.setOutline('blue')
        
        answerY = Rectangle(Point(160, 250), Point(180, 270))
        answerY.setFill('yellow')
        yLabel = Text(Point(170, 260), "Y")
        yLabel.setOutline('black')
        
        answerN = Rectangle(Point(210, 250), Point(230, 270))
        answerN.setFill('yellow')
        nLabel = Text(Point(220, 260), "N")
        nLabel.setOutline('black')
                
        message.draw(self.win)
        question.draw(self.win)
        answerY.draw(self.win)
        yLabel.draw(self.win)
        answerN.draw(self.win)
        nLabel.draw(self.win)

        pt = self.win.getMouse()
        if 160 <= pt.getX() <= 180 and 250 <= pt.getY() <= 270:
            self.win.close()
            return 1
        elif 210 <= pt.getX() <= 230 and 250 <= pt.getY() <= 270:
            self.win.close()
            return 0
        while (not 160 <= pt.getX() <= 180) or (not 210 <= pt.getX() <= 230) and (not 250 <= pt.getY() <= 270):
            pt = self.win.getMouse()
            if 160 <= pt.getX() <= 180 and 250 <= pt.getY() <= 270:
                self.win.close()
                return 1
            elif 210 <= pt.getX() <= 230 and 250 <= pt.getY() <= 270:
                self.win.close()
                return 0
    
    def loserWindow(self):
        message = Text(Point(200, 150), "Oh No! You Lost!")
        message.setOutline('red')
        
        question = Text(Point(200, 200), "Would you like to play again?")
        question.setOutline('red')
        
        answerY = Rectangle(Point(160, 250), Point(180, 270))
        answerY.setFill('yellow')
        yLabel = Text(Point(170, 260), "Y")
        yLabel.setOutline('black')
        
        answerN = Rectangle(Point(210, 250), Point(230, 270))
        answerN.setFill('yellow')
        nLabel = Text(Point(220, 260), "N")
        nLabel.setOutline('black')
                
        message.draw(self.win)
        question.draw(self.win)
        answerY.draw(self.win)
        yLabel.draw(self.win)
        answerN.draw(self.win)
        nLabel.draw(self.win)

        pt = self.win.getMouse()
        if 160 <= pt.getX() <= 180 and 250 <= pt.getY() <= 270:
            self.win.close()
            return 1
        elif 210 <= pt.getX() <= 230 and 250 <= pt.getY() <= 270:
            self.win.close()
            return 0

        while (not 160 <= pt.getX() <= 180) or (not 210 <= pt.getX() <= 230) and (not 250 <= pt.getY() <= 270):
            pt = self.win.getMouse()
            if 160 <= pt.getX() <= 180 and 250 <= pt.getY() <= 270:
                self.win.close()
                return 1
            elif 210 <= pt.getX() <= 230 and 250 <= pt.getY() <= 270:
                self.win.close()
                return 0


