from graphics import *
from gamemap import Map
from interfaces import Interface
from food import Food
from characters import Character
from random import randrange
from time import *

class Pacman:

    def __init__(self):
        self.window = GraphWin("Pacman", 550, 500)
        self.window.setBackground('black')
        
        self.scoreLabel = Text(Point(500, 235), 'Score')
        self.scoreLabel.setTextColor('white')
        self.scoreLabel.draw(self.window)

        self.scoreNumber = 0
        self.scoreNum_Label = Text(Point(500, 255), self.scoreNumber)
        self.scoreNum_Label.setTextColor('white')
        self.scoreNum_Label.draw(self.window)

        self.game_map = Map(self.window)     # This line calls the Map class inside gamemap.py
        self.game_map.createMap()

        self.map_boundaries = Map(self.window)

        
        self.click = Text(Point(250, 100), "Click anywhere to start")
        self.click.setTextColor('white')
        self.click.draw(self.window)
        
        self.window.getMouse()
        self.click.undraw()
        
        self.f = Food(self.window)
        self.food = self.f.drawFood()
        
        self.pac = Character(Point(250,445), 10, self.window)
        self.pac.drawPacman()

        self.ghosts = self.createGhosts() 
        
        while True:        
            self.moveCharacters()
            
                

    def createGhosts(self): # Create the ghosts
        self.g1 = Character(Point(60, 365), 10, self.window)
        self.g2 = Character(Point(440, 365), 10, self.window)
        self.g3 = Character(Point(250, 365), 10, self.window)
        self.g4 = Character(Point(250, 245), 10, self.window)

        self.g = [self.g1, self.g2, self.g3, self.g4]

        for i in self.g:
            i.drawGhost()

        return self.g
    # end ghosts

    def moveCharacters(self): # This function moves the characters of the game
                                                                            # Pacman's movement depends on the keys pressed by user
                                                                            # The ghosts' movement is set randomly depending on
                                                                            # their current positions
        for self.gh in self.ghosts:                                                                    
        
            slpNum = .05
            #map_boundaries = Map(window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
            instruction = randrange(1,8)   
            
            if instruction == 1: # move right or down
                if keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost() # This function is called after every character movement to determine if pacman came in
                                            # contact with one of the ghosts, indicating that the player lost
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingRight and not keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                    
            elif instruction == 3: # move left or down
                if keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingLeft and not keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()            
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                    
            elif instruction == 4: # move right or up
                if keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingRight and not keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()            
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)

            elif instruction == 2: # move left or up
                if keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingLeft and not keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()            
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)

            elif instruction == 5: # move down or right
                if keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingDown and not keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost()
            
                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)

            elif instruction == 7: # move up or right
                if keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingUp and not keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingRight:
                    sleep(slpNum)
                    self.gh.move(5,0)
                    self.checkLost()
            
                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                    
            elif instruction == 6: # move down or left
                if keepGoingDown:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingDown and not keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(0,5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()
            
                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)

            elif instruction == 8: # move up or left
                if keepGoingUp:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingUp and not keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(0,-5)
                    self.checkLost()

                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)
                while keepGoingLeft:
                    sleep(slpNum)
                    self.gh.move(-5,0)
                    self.checkLost()
            
                    key = self.window.checkKey()
                    self.handleKey(key)
                    self.eatFood()
                    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.gh)

        #return self.scoreNum_Label, self.scoreNumber
    # end moveCharacters

    def checkLost(self): # Checks if one of the ghosts touched pacman
        ghX = self.gh.getCenter().getX()
        ghY = self.gh.getCenter().getY()
        pacX = self.pac.getCenter().getX()
        pacY = self.pac.getCenter().getY()
        
        if ghX == pacX and ghY == pacY:
            self.loser()

    # end checkLost

    def handleKey(self, k): # This function handles pacman's movement depending on the flags returned by function 'boundaries'
                                    # and the key pressed by the player

        #map_boundaries = Map(window)
        keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown =  self.map_boundaries.setBoundaries(self.pac)
        
        if k == "Right":
            if keepGoingRight:
                self.pac.move(5, 0)
                self.checkLost()
            else:
                self.pac.move(0, 0)
                self.checkLost()

        elif k == "Left":
            if keepGoingLeft:
                self.pac.move(-5, 0)
                self.checkLost()
            else:
                self.pac.move(0, 0)
                self.checkLost()

        elif k == "Up":
            if keepGoingUp:
                self.pac.move(0, -5)
                self.checkLost()
            else:
                self.pac.move(0, 0)
                self.checkLost()

        elif k == "Down":
            if keepGoingDown:
                self.pac.move(0, 5)
                self.checkLost()
            else:
                self.pac.move(0,0)
                self.checkLost()
        
    # end handleKey

    def eatFood(self): # Handles the eaten food
        pacX = self.pac.getCenter().getX()
        pacY = self.pac.getCenter().getY()

        for i in self.food:
            if pacX == (i.getCenter().getX()) and pacY == (i.getCenter().getY()) and (i.id):
                i.undraw()
                self.scoreNum_Label.undraw()
                self.updateScore()
                self.checkWinner()
            
        #return self.scoreNum_Label, self.scoreNumber
    # end eatFood

    def updateScore(self): # Updates the score
        self.scoreNumber = self.scoreNumber + 1
        self.scoreNum_Label = Text(Point(500, 255), self.scoreNumber)
        self.scoreNum_Label.setTextColor('white')
        self.scoreNum_Label.draw(self.window)
        
        #return self.scoreNum_Label, self.num
    # end updateScore

    def checkWinner(self): # Checks if a player won by eating all foods
        if self.scoreNumber == 119:
            self.winner()

    # end checWinner

    def winner(self): # Output if player wins
        self.window.close()

        menu = Interface("You're a winner!", 400, 400)      # This line calls the Interface class inside interfaces.py
        ans = menu.winnerWindow()
        if ans == 1:
            Pacman()
        else:
            exit(Pacman)
    # end winner

    def loser(self): # Output if player loses
        self.window.close()

        menu = Interface("You're a loser!", 400, 400)       # This line calls the Interface class inside interfaces.py
        ans = menu.loserWindow()
        if ans == 1:
            Pacman()
        else:
            exit(Pacman)
    # end loser

def mainMenu(): # Main menu of the game; start option and exit option
            menu = Interface("Welcome", 400, 400)        # This line calls the Interface class inside interfaces.py
            ans = menu.mainMenu()
            if ans == 1:
                Pacman()
            else:
                exit(Pacman)
# Begin game
mainMenu()
