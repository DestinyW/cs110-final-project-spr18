# Go, Fetch!
## CS 110 Final Project
### Spring, 2018

[GitHub URL](https://github.com/binghamtonuniversity-cs110/final-project-spr18-indigo.git)

[Presentation Slides](https://docs.google.com/presentation/d/1dSbB4_zx-twQYZmc-nDS_sP8jjsDZP-aItV4xw6damw/edit?usp=sharing)

[GUI Concept](https://docs.google.com/presentation/d/1G4KUCHR8m9GNecY2GC9WtDUEP6b0_4xmQeJQMB2PxTA/edit?usp=sharing)

### Team: Indigo
#### Team Members: Natalie Anselmi, Maggie Chen, and Destiny Walcott

***

## 1. Project Description
In "Go, Fetch!" the player controls a dog to catch frisbees. Frisbees are automatically launched on one plane across the screen and come in 4 different colors, each with a different point value (White = - 10, Yellow = +1, Purple = +10, Red = +20). The player controls their dog with the up, down, left, and right arrow keys to catch frisbees and avoid walls. Each time the player hits a wall the dog loses 1 health (10 health points), if the dog reaches 0 health the player loses. The game takes 2 minutes (120 seconds) to play. If at the end of 2 minutes the dog still has health then the player wins.

***    

## 2. User Interface Design  
#### 2.1 Main Menu/Start Screen
This screen is the first thing that the user sees. It gives the user the option to play the game by clicking "Play", to leave the game by clicking "Quit", or to view the instructions by clicking "Instructions".

Original GUI Concept

![](charts/MMOld.png?raw=true)


#### 2.2 Instructions Screen
These 2 screens display a short description of the game and show the user how to play the game. From the first instructions page the player can hit "Menu" to return to the Main Menu or "Next" to go on to the next page. From the second instructions page the player can hit "Menu" to return to the Main Menu, "Back" to go to the first instructions page, or "Play" to begin the game.

Original GUI Concept

![](charts/I1Old.png?raw=true)
![](charts/I2Old.png?raw=true)


#### 2.3 The Game Screen
This is where the gameplay takes place. Frisbees are launched from the right of the screen and the player will use the arrow keys to move within the field. The player must move to collect frisbees and avoid walls. Each time the dog fails to avoid a wall, its health  decreases by 1. Health is displayed in the upper right hand corner, and score is displayed right below it. The timer is displayed in the top left corner.

Original GUI Concept

![](charts/GSOld.png?raw=true)


#### 2.4 The Game Over Menu
##### 2.4.1 Failure
If the player runs out of health within the time limit then gameplay ends and they are shown a screen that says “GAME OVER!”. There are 2 buttons: "Menu" which returns the player to the Main Menu and "Again" which starts the game again.

![](charts/FailOld.png?raw=true)

##### 2.4.2 Success
If the player still has health at the end of the time limit they are shown a screen that says “Good job!”. There are 2 buttons: "Menu" which returns the player to the Main Menu and "Again" which starts the game again.

![](charts/WinOld.png?raw=true)

##### 2.4.3 Final GUI Concept
![](charts/MMCurrent.png?raw=true)
![](charts/I1Current.png?raw=true)
![](charts/I2Current.png?raw=true)
![](charts/GSCurrent.png?raw=true)
![](charts/WinCurrent.png?raw=true)
![](charts/FailCurrent.png?raw=true)

***
## 3. Program Design
#### 3.1 Non-Standard Libraries and Modules Used
- [Pygame](https://www.pygame.org/): A free set of Python modules that is designed for developing game applications. It includes various features including computer graphics and sound libraries.

#### 3.2 Class and File Relationships
![](charts/ClassDiagram.png?raw=true)

#### 3.3 List of Classes
- Dog: A class that defines the player as a "dog" - it is an "active" object in gameplay. The dog will be able to move up and down the screen using the UP and DOWN arrows to catch frisbees and avoid walls.

- Frisbee: A class that defines an "active" subject in gameplay - primary point system. Frisbees will be "launched" from the right of the screen. They come in 4 different colors, each with a different point value (White = - 30, Yellow = 0, Purple = +10, Red = +20).

- Wall: A class that defines the obstacles in gameplay. The dog can avoid the walls by moving up and down. If the dog fails to avoid a wall, it will lose 1 health (10 bars maximum), and a result of 0 causes failure and ends the game.

- Score: A class that tracks the number of points the player gains during the gameplay. It also records and display the highest scores on game over menu.

- Background: A class that defines the screen of the game, which is different as the program progresses.

- Button: A class that sets the position of each button onto the screen of the game.

- Cloud: A class that defines cloud objects. Clouds are passive and do not interact with anything, they simply scroll across the screen.

- Controller: A class that initializes all of the imported pygame modules, load the sprites, handle the events, and contain the main loop. (includes timer and health)

***
## 4. Tasks and Responsibilities
#### 4.1 Software Lead - [Maggie Chen]
The software lead is responsible for the overall project management in terms of ensuring the quality and functionality of the code. She also makes sure that there is proper communication between the front-end and back-end specialists so that conflicts may be resolved in an effective manner. Moreover, she also schedules periodic meetings with the group to collaboratively discuss the progress and technical issues. She's also responsible in creating and updating the proposal, presentation slides, and test files for the program.

#### 4.2 Front End Specialist - [Natalie Anselmi]
The front end specialist is responsible for designing the look of GUI, coding the main loop, and handling events in the controller. She is also responsible for the User Interface Design.

#### 4.3 Back End Specialist - [Destiny Walcott]
The back end specialist is responsible for writing the major classes and data for the program. She also collaborates with the front end specialist to write the initial codes of the program. She also creates the class diagram that shows the classes and their relationships with each other.

***
## 5. Testing
#### 5.1 Testing Strategy
##### 5.1.1 Menu Testing

First, we run the Controller file which properly opens up the game along with the accompanying background music. Then, we click the "Instructions" button to open up the instructions page. We then test the functionality of the "Next" and "Back" buttons to ensure that they navigate between the two instructions pages. Next, we click the "Menu" button to return to the original Main Menu screen. From there, we start the gameplay by clicking "Play".

Later on, we check additional buttons including the "Again" and "Quit" buttons. The "Again" button on both the "WINNER!" and "YOU LOSE!" screens properly returns to the gameplay. Lastly, the "Quit" button in Main Menu properly closes the game entirely.

##### 5.1.2 Game Testing

When the gameplay begins, we test the 4 arrow keys to ensure its functionality. Pressing and holding down the UP, DOWN, LEFT, and RIGHT arrows allow the dog to move around the green field to catch frisbees and avoid walls. The dog is also contained within the green field and does not fall off the edges.

The gameplay runs for 4 minutes (240 seconds) in total. The dog has to catch as many colored frisbees (approaching from the right) as possible. The dog starts off with a maximum of 10 health bars, but loses 1 health every time it hits a wall. The health status will change to the color red once it reaches 3 bars. Moreover, the score is updated and displayed according to the colored frisbees the dog catches.

When we reach a fail state, a screen with "YOU LOSE!" opens up and shows a list of the top 10 scores. However, in a win state, a screen with "WINNER!" opens up and shows a list of the top 10 scores. Finally, we return to the Main Menu screen where the "Quit" button is to complete testing.

#### 5.2 Acceptance Test Procedure
[ATP Link](https://docs.google.com/document/d/1mRwjm5VlQiFG5ITpi4t685rkpe00hen6QSnsbdL7kWU/edit?usp=sharing)
