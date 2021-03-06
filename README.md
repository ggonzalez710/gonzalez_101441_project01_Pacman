# gonzalez_101441_project01_Pacman

# Game Description
My game is the classic arcade game 'Pacman'. To win you must eat all of the food (white dots) inside the map; you lose if one of the red circles eat you.

# Main Algorithm Explanation
<br>The main algorithm of the game takes place in the function 'runGame'. Function 'runGame' first draws the map, pacman's food, pacman and the ghosts.
It then enters a while loop where a function called 'moveCharacters' is continually called 4 times in a row (since there are 4 ghosts).  

<br>The function 'moveCharacters' receives 6 parameters:
<br>Parameter 1: A circle object named gh; this object is the 'ghost' that chases pacman
<br>Parameter 2: The window where the game is taking place
<br>Parameter 3: A circle object named pac; this object is pacman
<br>Parameter 4: A text object named scoreNum_Label; this is the label that shows the player's current score number
<br>Parameter 5: An integer variable named scoreNumber; this variable holds the number for the player's current score
<br>Parameter 6: An array called food where pacman's food (white circles) is stored.
    
<br>Function 'moveCharacters' begins with a function call to 'boundaries'. This function takes either a ghost's or pacman's current location and sets the object's boundaries
depending on what rectangle of the map the object is at. It returns 4 flags (keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown) that indicate in
which directions the object can move.

<br>Next in the function is the movement of the ghosts. There are 8 possible instructions for the ghosts' movement, so a random number is generated to indicate
the instruction to be carried out. Once the instruction is chosen, the movement flags are used to see whether the ghost can actually move in the instructed 
direction. Each time a ghost moves, the function 'checkLost' is called; this function is tasked with checking if a ghost touched pacman. Then the boundaries 
are checked again and a while loop is executed (if the movement flag is true) so that the ghost will continually move in a certain direction until it reaches 
a boundary of the map or it encounters an opening to go through. Next in the while loop, the ghost is instructed to move and after each movement the function 
'checkLost' is called, followed by a function call to 'handleKey'; function 'handleKey' is called to handle the player's entered key and move the pacman.
After calling 'handleKey', the function 'eatFood' is called to check if pacman ate one of the foods, and if so, then the score is updated; inside 'eatFood', 
the function 'checkWinner' is called to check if a player ate all of map's food and won the game.
