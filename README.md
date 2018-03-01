* Cover Page
    * A cover page containing your group member names, project title, course number, and semester
    * Github URL
    * Project Demo Presentation as Google Slide URL
Example:
# Project Title
## CS 110 Final Project
### Spring, 2018

[https://github.com/<repo>](#)

[link to demo presentation slides](#)

### Team: Indigo
#### Team Names: Natalie Anselmi, Maggie Chen, and Destiny Walcott

***

## Project Description
This game (name TBD) is a side scrolling fetch game. The player picks one of <6> dog breeds, and then has to catch frisbees. Frisbees are automatically launched across the screen and come in 5 different colors, each with a different point value (tentatively: Black = - 25, White = 0, Red = 10, Blue = 20, Green = 40). The player controls their dog with the arrow keys and uses the spacebar to jump and catch frisbees. There is <a time limit> to reach <a total number of points> per level, and <5> levels total.

***    

## User Interface Design  
2.1 Main Menu/Start Screen
This screen is the first thing that the user sees. It gives the user the option to play the game by clicking "start", to leave the game by clicking "quit", or to view the instructions by clicking "instructions".

(GUI concept)

2.2 Instructions Screen
This screen will display a short description of the game and show the user how to play the game. From this screen, the user will be able to play the game by clicking "continue", return to the main menu by clicking "main menu", or leave the game by clicking "quit".

(GUI concept)

2.3 Breed Choice
This screen will display pictures <6> dog breeds. Each dog box would include  Hovering the mouse over each breed box shows a floating text box displaying:  
   * Strengths (ex: fast runner, etc) TBD
   * Weaknesses (ex: low jumper, etc) TBD

(GUI concept)

2.4 The Game Menu
This is where gameplay takes place (rolling screen on a loop). Frisbees are launched from the right of the screen and the player will use the arrow keys to move within the field. As the ground scrolls in later levels, obstacles will appear. The player will have to use the spacebar to jump and get frisbees and clear obstacles. If the dog fails to jump over an obstacle, the dog trips and can’t move for <3> seconds. 

Possibilities of increasing difficulty: Moving obstacles that approach the dog, decreasing the time limit every level

(GUI concept)

2.5 End Game Menu
2.5.1 Failure
If the player fails to get the required number of points within the time limit they are shown a screen that says “GAME OVER!” with 3 small buttons beneath it:  Main Menu, Breed Choice, and Play Again
2.5.2 Success
If the player completes all 5 levels they are shown a screen that says “WINNER!” and displays their score. There are also 2 buttons: Play again and Main Menu

(GUI concept)

***
## Program Design
* You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python.
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Decide upon a class interface for the classes in your project.
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example).
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* You should have a list of each of your classes with a description.

***
3.1 Non-Standard Libraries and Modules Used
TBD

3.2 Class and File Relationships
TBD

3.3 List of Classes
TBD

***
## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.
    * Example:
### Software Lead - [Maggie Chen]

Worked as integration specialist by helping organize the code for the main game into the proper MVC format, which allowed all portions of the code to be run from a single file. He worked very closely with the back end to develop the high-score database functionality, as well as establish the win- and fail-states for the main game. He also lead the implementation of the ‘sprite’ and ‘group’ classes of pygame into the back end code.

### Front End Specialist - [Natalie Anselmi]

Front-end lead conducted significant research on using pygame to create visual aspects such as buttons and on-screen text. She used this information to design and program a consistent UI to help the player navigate the title screen, the instructions page, and the “GAME OVER” screen. In addition to implementing the wide majority of the visual element for the UI, she also collaborated with the Software Lead to create a jukebox function that played music and to add sound effects to the menu navigation buttons.

### Back End Specialist - [Destiny Walcott]

The back end specialist helped with the “Model” portion of BLOCKBUSTERS by writing the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He also made headway in major game mechanics such as the basic paddle movement and advanced functionality such as the screen-wrap function for the paddle as it approached the ends of the screen. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file, as well as develop our high-score database.

## Testing
* Describe your testing strategy for your project.
    * Example
* TBD

### Menu Testing

First, we run Controller()  and ensure the main menu opens normally, the musical score begins playing and that hovering the mouse over each button changes the color to the “highlighted” shade. Next, we click the Instructions button to ensure the INSTRUCTIONS menu opens, and the buttons are highlighted when hovered over as well. We also check to see if the music playback continues and that the sound effect is played when the button is pressed.

We then press the MAIN MENU button and return, checking that the same functionality with button hover, music and sound effects as before are present. Afterwards, we test that both of the QUIT buttons on the Main Menu and Instructions Menu properly close the game.We then test the PLAY buttons on the Instructions and Main Menu pages to make sure that the Game screen opens properly both times. We then move


### Game Testing

When the Game screen boots up , we test if spacebar starts the game and launches the ball, so we test to see if this remains true. From there, in the middle of play, we will test the single-press and holding of both the left and right arrow buttons to make sure movement works in single presses and continues to move when a key is held. We then move all the way to the left and right of the screen to see if it causes the paddle to appear on the other side - our wrap-around function.

From here, we conduct normal playtesting to ensure that the collisions, the speed of the ball, and the dynamic bounding and angles are all working together meaningfully and without any obvious error, especially in regards to the ball reflecting off of the corners and edges of the paddle. We also check to make sure the music plays throughout and that the destruction of a brick does in fact increase the score.

We then try to reach a win state, to check if it resets the game with an increase in ball speed, without resetting the score. If successful, we then purposefully reach three consecutive fail-states, one to test each of the GAME OVER screens’ three buttons - Play Again, Main Menu, and Quit - with the same functionality as before. Finally, we check that the “X” button on the window does in fact close the window. This concludes the testing protocol.

* A copy of your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
