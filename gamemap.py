# gamemap.py

# game map for pacman

# See Map Layout to understand where each rectangle is positioned

from graphics import *
from characters import Character

class Map:

    def __init__(self, win):
        self.win = win
        

    def createMap(self):
        # Bottom Half

        self.b1 = Rectangle(Point(50, 435), Point(450, 455))
        self.b2 = Rectangle(Point(450, 395), Point(430, 455))
        self.b3 = Rectangle(Point(450, 395), Point(370, 415))
        self.b4 = Rectangle(Point(370, 415), Point(390, 355))
        self.b5 = Rectangle(Point(70, 455), Point(50, 395))
        self.b6 = Rectangle(Point(50, 395), Point(130, 415))
        self.b7 = Rectangle(Point(130, 415), Point(110, 255))
        self.b8 = Rectangle(Point(110, 355), Point(390, 375))
        self.b9 = Rectangle(Point(290, 445), Point(270, 395))
        self.b10 = Rectangle(Point(270, 395), Point(310, 415))
        self.b11 = Rectangle(Point(310, 415), Point(290, 375))
        self.b12 = Rectangle(Point(210, 445), Point(230, 395))
        self.b13 = Rectangle(Point(230, 395), Point(190, 415))
        self.b14 = Rectangle(Point(190, 415), Point(210, 375))
        self.b15 = Rectangle(Point(410, 405), Point(430, 355))
        self.b16 = Rectangle(Point(410, 355), Point(450, 375))
        self.b17 = Rectangle(Point(450, 375), Point(430, 255))
        self.b18 = Rectangle(Point(290, 375), Point(270, 315))
        self.b19 = Rectangle(Point(270, 315), Point(450, 335))
        self.b20 = Rectangle(Point(70, 415), Point(90, 355))
        self.b21 = Rectangle(Point(90, 355), Point(50, 375))
        self.b22 = Rectangle(Point(50, 375), Point(70, 255))
        self.b23 = Rectangle(Point(210, 375), Point(230, 315))
        self.b24 = Rectangle(Point(50, 315), Point(230, 335))
        self.b25 = Rectangle(Point(290, 335), Point(310, 235))
        self.b26 = Rectangle(Point(290, 255), Point(430, 275))
        self.b27 = Rectangle(Point(390, 335), Point(370, 255))
        self.b28 = Rectangle(Point(210, 335), Point(190, 235))
        self.b29 = Rectangle(Point(50, 255), Point(210, 275))
        self.b30 = Rectangle(Point(190, 275), Point(310, 295))
        self.b31 = Rectangle(Point(190, 235), Point(310, 255))

        self.b = []
        self.b.append(self.b1)
        self.b.append(self.b2)
        self.b.append(self.b3)
        self.b.append(self.b4)
        self.b.append(self.b5)
        self.b.append(self.b6)
        self.b.append(self.b7)
        self.b.append(self.b8)
        self.b.append(self.b9)
        self.b.append(self.b10)
        self.b.append(self.b11)
        self.b.append(self.b12)
        self.b.append(self.b13)
        self.b.append(self.b14)
        self.b.append(self.b15)
        self.b.append(self.b16)
        self.b.append(self.b17)
        self.b.append(self.b18)
        self.b.append(self.b19)
        self.b.append(self.b20)
        self.b.append(self.b21)
        self.b.append(self.b22)
        self.b.append(self.b23)
        self.b.append(self.b24)
        self.b.append(self.b25)
        self.b.append(self.b26)
        self.b.append(self.b27)
        self.b.append(self.b28)
        self.b.append(self.b29)
        self.b.append(self.b30)
        self.b.append(self.b31)

        for i in self.b:
            i.setFill('blue')
            i.setOutline('blue')
            i.draw(self.win)


    def setBoundaries(self, obj): # This function sets the boundaries of the map for the formal parameter 'obj'
                             # 4 flags are returned; they indicate whether the object can or cannot move
                             # in a specific direction
                             
        objX = obj.getCenter().getX()
        objY = obj.getCenter().getY()
        
        keepGoingRight = True
        keepGoingLeft = True
        keepGoingUp = True
        keepGoingDown = True

        #b1 boundaries
        if (60 <= objX <= 440) and objY == 445:
            keepGoingDown = False
            keepGoingUp = False
            
            if objX == 60 or objX == 220 or objX == 280 or objX == 440:
                keepGoingUp = True
            if objX == 60:
                keepGoingLeft = False
            if objX == 440:
                keepGoingRight = False

        #b2 boundaries
        if (405 <= objY < 445) and objX == 440:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 405:
                keepGoingUp = False
                keepGoingLeft = True
        #b3 boundaries
        if (380 <= objX <= 440) and objY == 405:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 380 or objX == 420:
                keepGoingUp = True
            if objX == 380:
                keepGoingLeft = False
            if objX == 440:
                keepGoingRight = False
                keepGoingDown = True

        #b4 boundaries
        if (365 <= objY < 405) and objX == 380:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 365:
                keepGoingUp = False
                keepGoingLeft = True

        #b5 boundaries
        if (405 <= objY < 445) and objX == 60:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 405:
                keepGoingUp = False
                keepGoingRight = True

        #b6 boundaries
        if (60 <= objX <= 120) and objY == 405:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 80 or objX == 120:
                keepGoingUp = True
            if objX == 60:
                keepGoingLeft = False
                keepGoingDown = True
            if objX == 120:
                keepGoingRight = False

        #b7 boundaries
        if (265 <= objY < 405) and objX == 120:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 265:
                keepGoingUp = False
                keepGoingLeft = True
                keepGoingRight = True
            if objY == 325:
                keepGoingLeft = True
                keepGoingRight = True
            if objY == 365:
                keepGoingRight = True

        #b8 boundaries
        if (120 <= objX <= 380) and objY == 365:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 200 or objX == 300 or objX == 380:
                keepGoingDown = True
            if objX == 220 or objX == 280:
                keepGoingUp = True
            if objX == 120:
                keepGoingDown = True
                keepGoingUp = True
        #b9 boundaries
        if (405 <= objY < 445) and objX == 280:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 405:
                keepGoingUp = False
                keepGoingRight = True

        #b10 boundaries
        if (280 <= objX <= 300) and objY == 405:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 280:
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 300:
                keepGoingUp = True
                keepGoingRight = False

        #b11 boundaries
        if (365 <= objY < 405) and objX == 300:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 365:
                keepGoingUp = False
                keepGoingLeft = True
                keepGoingRight = True

        #b12 boundaries
        if (405 <= objY < 445) and objX == 220:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 405:
                keepGoingUp = False
                keepGoingLeft = True

        #b13 boundaries
        if (200 <= objX <= 220) and objY == 405:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 220:
                keepGoingDown = True
                keepGoingRight = False
            if objX == 200:
                keepGoingUp = True
                keepGoingLeft = False

        #b14 boundaries
        if (365 <= objY < 405) and objX == 200:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 365:
                keepGoingUp = False
                keepGoingLeft = True
                keepGoingRight = True

        #b15 boundaries
        if (365 <= objY < 405) and objX == 420:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 365:
                keepGoingUp = False
                keepGoingRight = True

        #b16 boundaries
        if (420 <= objX <= 440) and objY == 365:
            keepGoingUp = False
            keepGoingDown = False

            if objX == 420:
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 440:
                keepGoingUp = True
                keepGoingRight = False

        #b17 boundaries
        if (265 <= objY < 365) and objX == 440:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 265:
                keepGoingUp = False
                keepGoingLeft = True
            if objY == 325:
                keepGoingLeft = True

        #b18 boundaries
        if (325 <= objY < 365) and objX == 280:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 325:
                keepGoingUp = False
                keepGoingRight = True

        #b19 boundaries
        if (280 <= objX <= 440) and objY == 325:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 300 or objX == 380:
                keepGoingUp = True
            if objX == 280:
                keepGoingLeft = False
                keepGoingDown = True
            if objX == 440:
                keepGoingRight = False
                keepGoingUp = True
                keepGoingDown = True

        #b20 boundaries
        if (365 <= objY < 405) and objX == 80:
            keepGoingLeft = False
            keepGoingRight = False
            
            if objY == 365:
                keepGoingUp = False
                keepGoingLeft = True

        #b21 boundaries
        if (60 <= objX <= 80) and objY == 365:
            keepGoingUp = False
            keepGoingDown = False

            if objX == 60:
                keepGoingLeft = False
                keepGoingUp = True
            if objX == 80:
                keepGoingRight = False
                keepGoingDown = True

        #b22 boundaries
        if (265 <= objY < 365) and objX == 60:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 325:
                keepGoingRight = True
            if objY == 265:
                keepGoingUp = False
                keepGoingRight = True

        #b23 boundaries
        if (325 <= objY < 365) and objX == 220:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 325:
                keepGoingUp = False
                keepGoingLeft = True

        #b24 boundaries
        if (60 <= objX <= 220) and objY == 325:
            keepGoingUp = False
            keepGoingDown = False

            if objX == 120:
                keepGoingUp = True
                keepGoingDown = True
            if objX == 200:
                keepGoingUp = True
            if objX == 60:
                keepGoingUp = True
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 220:
                keepGoingDown = True
                keepGoingRight = False

        #b25 boundaries
        if (245 <= objY < 325) and objX == 300:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 285:
                keepGoingLeft = True
            if objY == 265:
                keepGoingRight = True
            if objY == 245:
                keepGoingUp = False
                keepGoingLeft = True

        #b26 boundaries
        if (300 <= objX <= 440) and objY == 265:
            keepGoingUp = False
            keepGoingDown = False

            if objX == 300:
                keepGoingUp = True
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 380:
                keepGoingDown = True
            if objX == 440:
                keepGoingDown = True
                keepGoingRight = False

        #b27 boundaries
        if (265 <= objY < 325) and objX == 380:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 265:
                keepGoingUp = False
                keepGoingLeft = True
                keepGoingRight = True

        #b28 boundaries
        if (245 <= objY < 325) and objX == 200:
            keepGoingLeft = False
            keepGoingRight = False

            if objY == 285:
                keepGoingRight = True
            if objY == 265:
                keepGoingLeft = True
            if objY == 245:
                keepGoingUp = False
                keepGoingRight = True

        #b29 boundaries
        if (60 <= objX <= 200) and objY == 265:
            keepGoingUp = False
            keepGoingDown = False

            if objX == 60:
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 120:
                keepGoingDown = True
            if objX == 200:
                keepGoingUp = True
                keepGoingDown = True
                keepGoingRight = False

        #b30 boundaries
        if (200 <= objX <= 300) and objY == 285:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 200:
                keepGoingUp = True
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 300:
                keepGoingUp = True
                keepGoingDown = True
                keepGoingRight = False

        #b31 boundaries
        if (200 <= objX <= 300) and objY == 245:
            keepGoingDown = False
            keepGoingUp = False

            if objX == 200:
                keepGoingDown = True
                keepGoingLeft = False
            if objX == 300:
                keepGoingDown = True
                keepGoingRight = False

        return keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown
    # end boundaries

