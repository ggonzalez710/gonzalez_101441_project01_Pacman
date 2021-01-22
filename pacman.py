"""
This program has 15 functions. Here they are in order of appearance:

mainMenu(): # Main menu of the game; start option and exit option
runGame(): # Function that starts and runs the game
map(window): # Creates game map
pacman(window): # Create the pacman
ghosts(window): # Create the ghosts
boundaries(obj, window): # This function sets the boundaries of the map for the formal parameter 'obj'
                             # 4 flags are returned; they indicate whether the object can or cannot move
                             # in a specific direction
moveCharacters(gh, window, pac, scoreNum_Label, scoreNumber, food): # This function moves the characters of the game
                                                                        # Pacman's movement depends on the keys pressed by user
                                                                        # The ghosts' movement is set randomly depending on
                                                                        # their current positions
checkLost(gh, pac, window): # Checks if one of the ghosts touched pacman

handleKey(k, pac, window, gh): # This function handles pacman's movement depending on the flags returned by function 'boundaries'
                                   # and the key pressed by the player
pacFood(window): # Creates the food that pacman eats
eatFood(pac, scoreNum_Label, scoreNumber, window, food): # Handles the eaten food
updateScore(num, window): # Updates the score
checkWinner(score, window): # Checks if a player won by eating all foods
winner(window): # Output if player wins
loser(window): # Output if player loses
"""

from graphics import *
from random import randrange
from time import *

def mainMenu(): # Main menu of the game; start option and exit option
    menu = GraphWin("Welcome", 400, 400)
    menu.setBackground('black')

    start = Rectangle(Point(150, 170), Point(250, 190))
    start.setFill('yellow')
    sLabel = Text(Point(200, 180), "Start")
    sLabel.setOutline('blue')
    
    ex = Rectangle(Point(150, 210), Point(250, 230))
    ex.setFill('yellow')
    eLabel = Text(Point(200, 220), "Exit")
    eLabel.setOutline('blue')

    start.draw(menu)
    ex.draw(menu)
    sLabel.draw(menu)
    eLabel.draw(menu)

    pt = menu.getMouse()
    if 170 <= pt.getY() <= 190:
        menu.close()
        runGame()
    elif 210 <= pt.getY() <= 230:
        menu.close()
        exit(pacman)
    while (not 170 <= pt.getY() <= 190) and (not 210 <= pt.getY() <= 230):
        pt = menu.getMouse()
        if 170 <= pt.getY() <= 190:
            menu.close()
            runGame()
        elif 210 <= pt.getY() <= 230:
            menu.close()
            exit(pacman)
# end mainMenu

def runGame(): # Function that starts and runs the game
    window = GraphWin("Pacman", 550, 500)
    window.setBackground('black')
    
    scoreLabel = Text(Point(500, 235), 'Score')
    scoreLabel.setTextColor('white')
    scoreLabel.draw(window)

    scoreNumber = 0
    scoreNum_Label = Text(Point(500, 255), scoreNumber)
    scoreNum_Label.setTextColor('white')
    scoreNum_Label.draw(window)

    map(window)
    
    click = Text(Point(250, 100), "Click anywhere to start")
    click.setTextColor('white')
    click.draw(window)
    
    window.getMouse()
    click.undraw()
    
    food = pacFood(window)
    pac = pacman(window)
    gh = ghosts(window)
    
    while True:        
        scoreNum_Label, scoreNumber = moveCharacters(gh[0], window, pac, scoreNum_Label, scoreNumber, food)
        scoreNum_Label, scoreNumber = moveCharacters(gh[1], window, pac, scoreNum_Label, scoreNumber, food)
        scoreNum_Label, scoreNumber = moveCharacters(gh[2], window, pac, scoreNum_Label, scoreNumber, food)
        scoreNum_Label, scoreNumber = moveCharacters(gh[3], window, pac, scoreNum_Label, scoreNumber, food)
        
# end runGame

def map(window): # Creates game map
                 # See Map Layout to understand where each rectangle is positioned
    # Bottom Half
    b1 = Rectangle(Point(50, 435), Point(450, 455))
    b2 = Rectangle(Point(450, 395), Point(430, 455))
    b3 = Rectangle(Point(450, 395), Point(370, 415))
    b4 = Rectangle(Point(370, 415), Point(390, 355))
    b5 = Rectangle(Point(70, 455), Point(50, 395))
    b6 = Rectangle(Point(50, 395), Point(130, 415))
    b7 = Rectangle(Point(130, 415), Point(110, 255))
    b8 = Rectangle(Point(110, 355), Point(390, 375))
    b9 = Rectangle(Point(290, 445), Point(270, 395))
    b10 = Rectangle(Point(270, 395), Point(310, 415))
    b11 = Rectangle(Point(310, 415), Point(290, 375))
    b12 = Rectangle(Point(210, 445), Point(230, 395))
    b13 = Rectangle(Point(230, 395), Point(190, 415))
    b14 = Rectangle(Point(190, 415), Point(210, 375))
    b15 = Rectangle(Point(410, 405), Point(430, 355))
    b16 = Rectangle(Point(410, 355), Point(450, 375))
    b17 = Rectangle(Point(450, 375), Point(430, 255))
    b18 = Rectangle(Point(290, 375), Point(270, 315))
    b19 = Rectangle(Point(270, 315), Point(450, 335))
    b20 = Rectangle(Point(70, 415), Point(90, 355))
    b21 = Rectangle(Point(90, 355), Point(50, 375))
    b22 = Rectangle(Point(50, 375), Point(70, 255))
    b23 = Rectangle(Point(210, 375), Point(230, 315))
    b24 = Rectangle(Point(50, 315), Point(230, 335))
    b25 = Rectangle(Point(290, 335), Point(310, 235))
    b26 = Rectangle(Point(290, 255), Point(430, 275))
    b27 = Rectangle(Point(390, 335), Point(370, 255))
    b28 = Rectangle(Point(210, 335), Point(190, 235))
    b29 = Rectangle(Point(50, 255), Point(210, 275))
    b30 = Rectangle(Point(190, 275), Point(310, 295))
    b31 = Rectangle(Point(190, 235), Point(310, 255))

    b1.setFill('blue')
    b2.setFill('blue')
    b3.setFill('blue')
    b4.setFill('blue')
    b5.setFill('blue')
    b6.setFill('blue')
    b7.setFill('blue')
    b8.setFill('blue')
    b9.setFill('blue')
    b10.setFill('blue')
    b11.setFill('blue')
    b12.setFill('blue')
    b13.setFill('blue')
    b14.setFill('blue')
    b15.setFill('blue')
    b16.setFill('blue')
    b17.setFill('blue')
    b18.setFill('blue')
    b19.setFill('blue')
    b20.setFill('blue')
    b21.setFill('blue')
    b22.setFill('blue')
    b23.setFill('blue')
    b24.setFill('blue')
    b25.setFill('blue')
    b26.setFill('blue')
    b27.setFill('blue')
    b28.setFill('blue')
    b29.setFill('blue')
    b30.setFill('blue')
    b31.setFill('blue')
    
    b1.setOutline('blue')
    b2.setOutline('blue')
    b3.setOutline('blue')
    b4.setOutline('blue')
    b5.setOutline('blue')
    b6.setOutline('blue')
    b7.setOutline('blue')
    b8.setOutline('blue')
    b9.setOutline('blue')
    b10.setOutline('blue')
    b11.setOutline('blue')
    b12.setOutline('blue')
    b13.setOutline('blue')
    b14.setOutline('blue')
    b15.setOutline('blue')
    b16.setOutline('blue')
    b17.setOutline('blue')
    b18.setOutline('blue')
    b19.setOutline('blue')
    b20.setOutline('blue')
    b21.setOutline('blue')
    b22.setOutline('blue')
    b23.setOutline('blue')
    b24.setOutline('blue')
    b25.setOutline('blue')
    b26.setOutline('blue')
    b27.setOutline('blue')
    b28.setOutline('blue')
    b29.setOutline('blue')
    b30.setOutline('blue')
    b31.setOutline('blue')

    b1.draw(window)
    b2.draw(window)
    b3.draw(window)
    b4.draw(window)
    b5.draw(window)
    b6.draw(window)
    b7.draw(window)
    b8.draw(window)
    b9.draw(window)
    b10.draw(window)
    b11.draw(window)
    b12.draw(window)
    b13.draw(window)
    b14.draw(window)
    b15.draw(window)
    b16.draw(window)
    b17.draw(window)
    b18.draw(window)
    b19.draw(window)
    b20.draw(window)
    b21.draw(window)
    b22.draw(window)
    b23.draw(window)
    b24.draw(window)
    b25.draw(window)
    b26.draw(window)
    b27.draw(window)
    b28.draw(window)
    b29.draw(window)
    b30.draw(window)
    b31.draw(window)
# end map

def pacman(window): # Create the pacman
    pac = Circle(Point(250,445), 10)
    pac.setFill('yellow')
    pac.draw(window)

    return pac
# end pacman

def ghosts(window): # Create the ghosts
    g1 = Circle(Point(60, 365), 10)
    g1.setFill('red')
    g1.draw(window)

    g2 = Circle(Point(440, 365), 10)
    g2.setFill('red')
    g2.draw(window)

    g3 = Circle(Point(250, 365), 10)
    g3.setFill('red')
    g3.draw(window)

    g4 = Circle(Point(250, 245), 10)
    g4.setFill('red')
    g4.draw(window)

    g = [g1, g2, g3, g4]

    return g
# end ghosts

def boundaries(obj, window): # This function sets the boundaries of the map for the formal parameter 'obj'
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

def moveCharacters(gh, window, pac, scoreNum_Label, scoreNumber, food): # This function moves the characters of the game
                                                                        # Pacman's movement depends on the keys pressed by user
                                                                        # The ghosts' movement is set randomly depending on
                                                                        # their current positions
                                                                        
    
    slpNum = .05
    
    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
    instruction = randrange(1,8)   
    
    if instruction == 1: # move right or down
        if keepGoingRight:
            sleep(slpNum)
            gh.move(5,0)
            checkLost(gh, pac, window) # This function is called after every character movement to determine if pacman came in
                                       # contact with one of the ghosts, indicating that the player lost
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
            while keepGoingRight and not keepGoingDown:
                sleep(slpNum)
                gh.move(5,0)
                checkLost(gh, pac, window)

                key = window.checkKey()
                handleKey(key, pac, window, gh)
                scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
                keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
            while keepGoingDown:
                sleep(slpNum)
                gh.move(0,5)
                checkLost(gh, pac, window)

                key = window.checkKey()
                handleKey(key, pac, window, gh)
                scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
                keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
            
    elif instruction == 3: # move left or down
        if keepGoingLeft:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingLeft and not keepGoingDown:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingDown:
            sleep(slpNum)
            gh.move(0,5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)            
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
            
    elif instruction == 4: # move right or up
        if keepGoingRight:
            sleep(slpNum)
            gh.move(5,0)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingRight and not keepGoingUp:
            sleep(slpNum)
            gh.move(5,0)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingUp:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)            
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)

    elif instruction == 2: # move left or up
        if keepGoingLeft:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingLeft and not keepGoingUp:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingUp:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)            
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)

    elif instruction == 5: # move down or right
        if keepGoingDown:
            sleep(slpNum)
            gh.move(0,5)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingDown and not keepGoingRight:
            sleep(slpNum)
            gh.move(0,5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingRight:
            sleep(slpNum)
            gh.move(5,0)
            checkLost(gh, pac, window)
    
            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)

    elif instruction == 7: # move up or right
        if keepGoingUp:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingUp and not keepGoingRight:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingRight:
            sleep(slpNum)
            gh.move(5,0)
            checkLost(gh, pac, window)
    
            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
            
    elif instruction == 6: # move down or left
        if keepGoingDown:
            sleep(slpNum)
            gh.move(0,5)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingDown and not keepGoingLeft:
            sleep(slpNum)
            gh.move(0,5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingLeft:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)
    
            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)

    elif instruction == 8: # move up or left
        if keepGoingUp:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingUp and not keepGoingLeft:
            sleep(slpNum)
            gh.move(0,-5)
            checkLost(gh, pac, window)

            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)
        while keepGoingLeft:
            sleep(slpNum)
            gh.move(-5,0)
            checkLost(gh, pac, window)
    
            key = window.checkKey()
            handleKey(key, pac, window, gh)
            scoreNum_Label, scoreNumber = eatFood(pac, scoreNum_Label, scoreNumber, window, food)
            keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(gh, window)

    return scoreNum_Label, scoreNumber
# end moveCharacters

def checkLost(gh, pac, window): # Checks if one of the ghosts touched pacman
    ghX = gh.getCenter().getX()
    ghY = gh.getCenter().getY()
    pacX = pac.getCenter().getX()
    pacY = pac.getCenter().getY()
    
    if ghX == pacX and ghY == pacY:
        loser(window)

# end checkLost

def handleKey(k, pac, window, gh): # This function handles pacman's movement depending on the flags returned by function 'boundaries'
                                   # and the key pressed by the player
    keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown = boundaries(pac, window)
    
    if k == "Right":
        if keepGoingRight:
            pac.move(5, 0)
            checkLost(gh, pac, window)
        else:
            pac.move(0, 0)
            checkLost(gh, pac, window)

    elif k == "Left":
        if keepGoingLeft:
            pac.move(-5, 0)
            checkLost(gh, pac, window)
        else:
            pac.move(0, 0)
            checkLost(gh, pac, window)

    elif k == "Up":
        if keepGoingUp:
            pac.move(0, -5)
            checkLost(gh, pac, window)
        else:
            pac.move(0, 0)
            checkLost(gh, pac, window)

    elif k == "Down":
        if keepGoingDown:
            pac.move(0, 5)
            checkLost(gh, pac, window)
        else:
            pac.move(0,0)
            checkLost(gh, pac, window)
    
# end handleKey

def pacFood(window): # Creates the food that pacman eats
    #b1
    f1 = Circle(Point(280, 445), 1.5)
    f1.setFill('white')
    f2 = f1.clone()
    f2.move(20, 0)
    f3 = f2.clone()
    f3.move(20, 0)
    f4 = f3.clone()
    f4.move(20, 0)
    f5 = f4.clone()
    f5.move(20, 0)
    f6 = f5.clone()
    f6.move(20, 0)
    f7 = f6.clone()
    f7.move(20, 0)
    f8 = f7.clone()
    f8.move(20, 0)
    f9 = f8.clone()
    f9.move(20, 0)
    
    #b2
    f10 = f9.clone()
    f10.move(0, -20)
    f11 = f10.clone()
    f11.move(0, -20)

    #b3
    f12 = f11.clone()
    f12.move(-20, 0)
    f13 = f12.clone()
    f13.move(-20, 0)
    f14 = f13.clone()
    f14.move(-20, 0)

    #b4
    f15 = f14.clone()
    f15.move(0, -20)
    f16 = f15.clone()
    f16.move(0, -20)

    #b8
    f17 = f16.clone()
    f17.move(-20, 0)
    f18 = f17.clone()
    f18.move(-20, 0)
    f19 = f18.clone()
    f19.move(-20, 0)
    f20 = f19.clone()
    f20.move(-20, 0)
    f21 = f20.clone()
    f21.move(-20, 0)
    f22 = f21.clone()
    f22.move(-20, 0)
    f23 = f22.clone()
    f23.move(-20, 0)
    f24 = f23.clone()
    f24.move(-20, 0)
    f25 = f24.clone()
    f25.move(-20, 0)
    f26 = f25.clone()
    f26.move(-20, 0)
    f27 = f26.clone()
    f27.move(-20, 0)
    f28 = f27.clone()
    f28.move(-20, 0)
    f29 = f28.clone()
    f29.move(-20, 0)

    #b7
    f30 = f29.clone()
    f30.move(0, 20)
    f31 = f30.clone()
    f31.move(0, 20)

    #b6
    f32 = f31.clone()
    f32.move(-20, 0)
    f33 = f32.clone()
    f33.move(-20, 0)
    f34 = f33.clone()
    f34.move(-20, 0)

    #b5
    f35 = f34.clone()
    f35.move(0, 20)
    f36 = f35.clone()
    f36.move(0, 20)

    #b1
    f37 = f36.clone()
    f37.move(20, 0)
    f38 = f37.clone()
    f38.move(20, 0)
    f39 = f38.clone()
    f39.move(20, 0)
    f40 = f39.clone()
    f40.move(20, 0)
    f41 = f40.clone()
    f41.move(20, 0)
    f42 = f41.clone()
    f42.move(20, 0)
    f43 = f42.clone()
    f43.move(20, 0)
    f44 = f43.clone()
    f44.move(20, 0)

    #b9, b10, b11
    f45 = f1.clone()
    f45.move(0, -20)
    f46 = f45.clone()
    f46.move(0, -20)
    f47 = f46.clone()
    f47.move(20, 0)
    f48 = f47.clone()
    f48.move(0, -20)

    #b12, b13, b14
    f49 = f44.clone()
    f49.move(0, -20)
    f50 = f49.clone()
    f50.move(0, -20)
    f51 = f50.clone()
    f51.move(-20, 0)
    f52 = f51.clone()
    f52.move(0, -20)

    #b15, b16, b17
    f53 = f12.clone()
    f53.move(0, -20)
    f54 = f53.clone()
    f54.move(0, -20)
    f55 = f54.clone()
    f55.move(20, 0)
    f56 = f55.clone()
    f56.move(0, -20)
    f57 = f56.clone()
    f57.move(0, -20)
    f58 = f57.clone()
    f58.move(0, -20)
    f59 = f58.clone()
    f59.move(0, -20)
    f60 = f59.clone()
    f60.move(0, -20)

    #b19, b18
    f61 = f57.clone()
    f61.move(-20, 0)
    f62 = f61.clone()
    f62.move(-20, 0)
    f63 = f62.clone()
    f63.move(-20, 0)
    f64 = f63.clone()
    f64.move(-20, 0)
    f65 = f64.clone()
    f65.move(-20, 0)
    f66 = f65.clone()
    f66.move(-20, 0)
    f67 = f66.clone()
    f67.move(-20, 0)
    f68 = f67.clone()
    f68.move(-20, 0)
    f69 = f68.clone()
    f69.move(0, 20)

    #b26
    f70 = f60.clone()
    f70.move(-20, 0)
    f71 = f70.clone()
    f71.move(-20, 0)
    f72 = f71.clone()
    f72.move(-20, 0)
    f73 = f72.clone()
    f73.move(-20, 0)
    f74 = f73.clone()
    f74.move(-20, 0)
    f75 = f74.clone()
    f75.move(-20, 0)
    f76 = f75.clone()
    f76.move(-20, 0)
    #b25
    f77 = f76.clone()
    f77.move(0, -20)
    f78 = f76.clone()
    f78.move(0, 20)
    f79 = f78.clone()
    f79.move(0, 20)
    #b27
    f80 = f72.clone()
    f80.move(0, 20)
    f81 = f80.clone()
    f81.move(0, 20)

    #b31
    f82 = f77.clone()
    f82.move(-20, 0)
    f83 = f82.clone()
    f83.move(-20, 0)
    f84 = f83.clone()
    f84.move(-20, 0)
    f85 = f84.clone()
    f85.move(-20, 0)
    f86 = f85.clone()
    f86.move(-20, 0)

    #b30
    f87 = f78.clone()
    f87.move(-20, 0)
    f88 = f87.clone()
    f88.move(-20, 0)
    f89 = f88.clone()
    f89.move(-20, 0)
    f90 = f89.clone()
    f90.move(-20, 0)
    f91 = f90.clone()
    f91.move(-20, 0)

    #b28
    f92 = f86.clone()
    f92.move(0, 20)
    f93 = f92.clone()
    f93.move(0, 40)
    f94 = f93.clone()
    f94.move(0, 20)
    #b23
    f95 = f94.clone()
    f95.move(20, 0)
    f96 = f95.clone()
    f96.move(0, 20)

    #b29
    f97 = f92.clone()
    f97.move(-20, 0)
    f98 = f97.clone()
    f98.move(-20, 0)
    f99 = f98.clone()
    f99.move(-20, 0)
    f100 = f99.clone()
    f100.move(-20, 0)
    f101 = f100.clone()
    f101.move(-20, 0)
    f102 = f101.clone()
    f102.move(-20, 0)
    f103 = f102.clone()
    f103.move(-20, 0)

    #b24
    f104 = f94.clone()
    f104.move(-20, 0)
    f105 = f104.clone()
    f105.move(-20, 0)
    f106 = f105.clone()
    f106.move(-20, 0)
    f107 = f106.clone()
    f107.move(-20, 0)
    f108 = f107.clone()
    f108.move(-20, 0)
    f109 = f108.clone()
    f109.move(-20, 0)
    f110 = f109.clone()
    f110.move(-20, 0)

    #b7
    f111 = f29.clone()
    f111.move(0, -20)
    f112 = f111.clone()
    f112.move(0, -40)
    f113 = f112.clone()
    f113.move(0, -20)

    #b22
    f114 = f103.clone()
    f114.move(0, 20)
    f115 = f114.clone()
    f115.move(0, 20)
    f116 = f115.clone()
    f116.move(0, 40)
    f117 = f116.clone()
    f117.move(0, 20)
    #b21
    f118 = f117.clone()
    f118.move(20, 0)
    f119 = f118.clone()
    f119.move(0, 20)

    #draw food
    f1.draw(window)
    f2.draw(window)
    f3.draw(window)
    f4.draw(window)
    f5.draw(window)
    f6.draw(window)
    f7.draw(window)
    f8.draw(window)
    f9.draw(window)
    f10.draw(window)
    f11.draw(window)
    f12.draw(window)
    f13.draw(window)
    f14.draw(window)
    f15.draw(window)
    f16.draw(window)
    f17.draw(window)
    f18.draw(window)
    f19.draw(window)
    f20.draw(window)
    f21.draw(window)
    f22.draw(window)
    f23.draw(window)
    f24.draw(window)
    f25.draw(window)
    f26.draw(window)
    f27.draw(window)
    f28.draw(window)
    f29.draw(window)
    f30.draw(window)
    f31.draw(window)
    f32.draw(window)
    f33.draw(window)
    f34.draw(window)
    f35.draw(window)
    f36.draw(window)
    f37.draw(window)
    f38.draw(window)
    f39.draw(window)
    f40.draw(window)
    f41.draw(window)
    f42.draw(window)
    f43.draw(window)
    f44.draw(window)
    f45.draw(window)
    f46.draw(window)
    f47.draw(window)
    f48.draw(window)
    f49.draw(window)
    f50.draw(window)
    f51.draw(window)
    f52.draw(window)
    f53.draw(window)
    f54.draw(window)
    f55.draw(window)
    f56.draw(window)
    f57.draw(window)
    f58.draw(window)
    f59.draw(window)
    f60.draw(window)
    f61.draw(window)
    f62.draw(window)
    f63.draw(window)
    f64.draw(window)
    f65.draw(window)
    f66.draw(window)
    f67.draw(window)
    f68.draw(window)
    f69.draw(window)
    f70.draw(window)
    f71.draw(window)
    f72.draw(window)
    f73.draw(window)
    f74.draw(window)
    f75.draw(window)
    f76.draw(window)
    f77.draw(window)
    f78.draw(window)
    f79.draw(window)
    f80.draw(window)
    f81.draw(window)
    f82.draw(window)
    f83.draw(window)
    f84.draw(window)
    f85.draw(window)
    f86.draw(window)
    f87.draw(window)
    f88.draw(window)
    f89.draw(window)
    f90.draw(window)
    f91.draw(window)
    f92.draw(window)
    f93.draw(window)
    f94.draw(window)
    f95.draw(window)
    f96.draw(window)
    f97.draw(window)
    f98.draw(window)
    f99.draw(window)
    f100.draw(window)
    f101.draw(window)
    f102.draw(window)
    f103.draw(window)
    f104.draw(window)
    f105.draw(window)
    f106.draw(window)
    f107.draw(window)
    f108.draw(window)
    f109.draw(window)
    f110.draw(window)
    f111.draw(window)
    f112.draw(window)
    f113.draw(window)
    f114.draw(window)
    f115.draw(window)
    f116.draw(window)
    f117.draw(window)
    f118.draw(window)
    f119.draw(window)
    
    f = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25,
         f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45, f46, f47, f48,
         f49, f50, f51, f52, f53, f54, f55, f56, f57, f58, f59, f60, f61, f62, f63, f64, f65, f66, f67, f68, f69, f70, f71,
         f72, f73, f74, f75, f76, f77, f78, f79, f80, f81, f82, f83, f84, f85, f86, f87, f88, f89, f90, f91, f92, f93, f94,
         f95, f96, f97, f98, f99, f100, f101, f102, f103, f104, f105, f106, f107, f108, f109, f110, f111, f112, f113, f114,
         f115, f116, f117, f118, f119]

    return f
#end pacFood

def eatFood(pac, scoreNum_Label, scoreNumber, window, food): # Handles the eaten food
    pacX = pac.getCenter().getX()
    pacY = pac.getCenter().getY()

    for i in food:
        if pacX == (i.getCenter().getX()) and pacY == (i.getCenter().getY()) and (i.id):
            i.undraw()
            scoreNum_Label.undraw()
            scoreNum_Label, scoreNumber = updateScore(scoreNumber, window)
            checkWinner(scoreNumber, window)
        
    return scoreNum_Label, scoreNumber
# end eatFood

def updateScore(num, window): # Updates the score
    num = num + 1
    scoreNum_Label = Text(Point(500, 255), num)
    scoreNum_Label.setTextColor('white')
    scoreNum_Label.draw(window)
    
    return scoreNum_Label, num
# end updateScore

def checkWinner(score, window): # Checks if a player won by eating all foods
    if score == 119:
        winner(window)

# end checWinner

def winner(window): # Output if player wins
    window.close()
            
    winnerWin = GraphWin("You're a winner!", 400, 400)
    winnerWin.setBackground('black')
            
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
            
    message.draw(winnerWin)
    question.draw(winnerWin)
    answerY.draw(winnerWin)
    yLabel.draw(winnerWin)
    answerN.draw(winnerWin)
    nLabel.draw(winnerWin)

    pt = winnerWin.getMouse()
    if 160 <= pt.getX() <= 180:
        winnerWin.close()
        mainMenu()
    elif 210 <= pt.getX() <= 230:
        winnerWin.close()
        exit(pacman)
    while (not 160 <= pt.getX() <= 180) and (not 210 <= pt.getX() <= 230):
        pt = winnerWin.getMouse()
        if 160 <= pt.getX() <= 180:
            winnerWin.close()
            mainMenu()
        elif 210 <= pt.getX() <= 230:
            winnerWin.close()
            exit(pacman)
# end winner

def loser(window): # Output if player loses
    window.close()
            
    loserWin = GraphWin("You're a loser!", 400, 400)
    loserWin.setBackground('black')
            
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
            
    message.draw(loserWin)
    question.draw(loserWin)
    answerY.draw(loserWin)
    yLabel.draw(loserWin)
    answerN.draw(loserWin)
    nLabel.draw(loserWin)

    pt = loserWin.getMouse()
    if 160 <= pt.getX() <= 180:
        loserWin.close()
        mainMenu()
    elif 210 <= pt.getX() <= 230:
        loserWin.close()
        exit(pacman)
    while (not 160 <= pt.getX() <= 180) and (not 210 <= pt.getX() <= 230):
        pt = loserWin.getMouse()
        if 160 <= pt.getX() <= 180:
            loserWin.close()
            mainMenu()
        elif 210 <= pt.getX() <= 230:
            loserWin.close()
            exit(pacman)
# end loser

# Begin game
mainMenu()
