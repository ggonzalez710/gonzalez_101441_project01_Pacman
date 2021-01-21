# gonzalez_101441_project01_Pacman

# Game Description
My game is the classic arcade game 'Pacman'. To win you must eat all of the food (white dots) inside the map; you lose if one of the red circles eat you.

# Main Algorithm Explanation
The main algorithm of the game takes place in the function 'moveCharacters'. This function receives 6 parameters:
    Parameter 1: A circle object named gh; this object is the 'ghost' that chases pacman
    Parameter 2: The window where the game is taking place
    Parameter 3: A circle object named pac; this object is pacman
    Parameter 4: A text object named scoreNum_Label; this is the label that shows the player's current score number
    Parameter 5: An integer variable named scoreNumber; this variable holds the number for the player's current score
    Parameter 6: An array called food where pacman's food (white circles) is stored.
    
The function begins with a function call to 'boundaries'. This function takes either a ghost's or pacman's current location and sets the object's boundaries
depending on what rectangle of the map the object is at. It returns 4 flags (keepGoingRight, keepGoingLeft, keepGoingUp, keepGoingDown) that indicate in
which direction the object can move.

Next in the function is the movement of the ghosts. There are 8 possible instructions for the ghosts' movement, so a random number is generated to indicate
the instruction to be carried out. Once the instruction is chosen, the movement flags are used to see whether the ghost can actually move in the instructed 
direction. Each time a ghost moves, the function 'checkLost' is called; this function is tasked with checking if a ghost touched pacman. After the 
'checkLost' function call, a key 
