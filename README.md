# Fetch Game
## CS 110 Final Project
### Spring, 2018

[GitHub URL](https://github.com/binghamtonuniversity-cs110/final-project-spr18-indigo.git)

[Demo Presentation Slides (TBD)](#)

[GUI Concept](https://docs.google.com/presentation/d/1G4KUCHR8m9GNecY2GC9WtDUEP6b0_4xmQeJQMB2PxTA/edit?usp=sharing)

### Team: Indigo
#### Team Names: Natalie Anselmi, Maggie Chen, and Destiny Walcott

***

## 1. Project Description
In "Go, Fetch!" the player controls a dog to catch frisbees. Frisbees are automatically launched on one plane across the screen and come in 4 different colors, each with a different point value (White = - 30, Yellow = 0, Purple = +10, Red = +20). The player controls their dog with the up and down arrow keys to catch frisbees and avoild walls. Each time the player hits a wall the dog loses 1 health, if the dog reaches 0 health the player loses. The game takes 4 minutes to play, if at the end of 3 minutes the dog still has health then the player wins.

***    

## 2. User Interface Design  
#### 2.1 Main Menu/Start Screen
This screen is the first thing that the user sees. It gives the user the option to play the game by clicking "Play", to leave the game by clicking "Quit", or to view the instructions by clicking "Instructions".


#### 2.2 Instructions Screen
These 2 screens display a short description of the game and show the user how to play the game. From the first instructions page the player can hit "Menu" to return to the Main Menu or "Next" to go on to the next page. From the second instructions page the player can hit "Menu" to return to the Main Menu, "Back" to go to the first instrucions page, or "Play" to begin the game.


#### 2.3 The Game Screen
This is where gameplay takes place. Frisbees are launched from the right of the screen and the player will use the arrow keys to move within the field. The player must moves to get frisbees and avoid walls. Each time the dog fails to avoid a wall, its health bar will decrease by 1. 


#### 2.4 The Game Over Menu
##### 2.4.1 Failure
If the player runs out of health within the time limit then gameplay ends and they are shown a screen that says “GAME OVER!”. There are 2 buttons: "Menu" which returns the player to the Main Menu and "Again" which starts the game again.

##### 2.4.2 Success
If the player still has health at the end of the time limit they are shown a screen that says “Good job!”. There are 2 buttons: "Menu" which returns the player to the Main Menu and "Again" which starts the game again.


***
## 3. Program Design
#### 3.1 Non-Standard Libraries and Modules Used
pygame

#### 3.2 Class and File Relationships
TBD

#### 3.3 List of Classes
Dog
Disk
Wall
Timer
Health Bar
Background
Button

***
## 4. Tasks and Responsibilities
#### 4.1 Software Lead - [Maggie Chen]
The software lead is responsible for the overall project management in terms of ensuring the quality and functionality of the code. She also makes sure that there is proper communication between the front-end and back-end specialists so that conflicts may be resolved in an effective manner. Moreover, she also schedules periodic meetings with the group to collaboratively discuss the progress and technical issues. She's also responsible in creating and updating the proposal, presentation slides, and test files for the program.

#### 4.2 Front End Specialist - [Natalie Anselmi]
Designing the look of GUI, coding the main loop, and handling events in the controller. Responsible for the User Interface Design.

#### 4.3 Back End Specialist - [Destiny Walcott]
TBD

***
## 5. Testing
TBD

[Acceptance Test Procedure](https://docs.google.com/document/d/1mRwjm5VlQiFG5ITpi4t685rkpe00hen6QSnsbdL7kWU/edit?usp=sharing)
