import json
import pygame
import random
import sys
from src import background
from src import button
from src import cloud
from src import dog
from src import frisbee
from src import timer
from src import wall

class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        pygame.mixer.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Go, Fetch!")
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.button = pygame.Surface(self.screen.get_size()).convert()
        #sound effects
        self.button_sound = pygame.mixer.Sound("sound/Click.wav")
        self.victory_sound = pygame.mixer.Sound("sound/TaDa.wav")
        self.failure_sound = pygame.mixer.Sound("sound/WahWah.wav")

        """Load sprites"""
        self.dog = dog.Dog(300, 400, "assets/GSDogRun1.png")
        self.walls = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        #Set up the frisbees
        self.frisbees = pygame.sprite.Group()
        for i in range(2):
            self.addFrisbee()

        """load background images"""
        self.mainmenu = background.Background("assets/MainMenu.png", [0, 0])
        self.instructions1 = background.Background("assets/Inst1.png", [0, 0])
        self.instructions2 = background.Background("assets/Inst2.png", [0, 0])
        self.gamescreen = background.Background("assets/GameBG.png", [0, 0])
        self.winner = background.Background("assets/WinBG.png", [0, 0])
        self.loser = background.Background("assets/LoseBG.png", [0, 0])
        
        """buttons"""
        #buttons for the main menu
        self.InstructionsMM = button.Button("assets/InstructionsMM.png", 400, 500,True)
        self.PlayMM = button.Button("assets/PlayMM.png",400,600,True)
        self.quitMM = button.Button("assets/QuitMM.png",400,700,True)
        #buttons for the first instructions page
        self.menu = button.Button("assets/InstMenu.png", 10, 680)
        self.next = button.Button("assets/Inst1Next.png", 610, 680)
        #buttons for the second instruction page
        self.Instback = button.Button("assets/Inst2Back.png", 300, 680)
        self.Instplay = button.Button("assets/Inst2Play.png", 610, 680)
        #buttons for the end screens
        self.EndAgain = button.Button("assets/EndAgain.png", 50, 695)
        self.EndMenu = button.Button("assets/EndMenu.png", 550, 670)

    #functions for continuously adding new sprites
    def addClouds(self):
        """
        Function for generating new clouds
        """
        x = random.randrange(750, 800)
        y = random.randrange(0, 190)
        new_cloud = cloud.Cloud(x, y, "assets/Clouds.png")
        self.clouds.add(new_cloud)
        return new_cloud
    def addFrisbee(self):
        """
        Function for generating new frisbees
        """
        x = random.randrange(750, 800)
        y = random.randrange(310, 630)
        frisbee_number = random.randint(0,3)   #calls on one of the 4 frisbee types
        if(frisbee_number == 0):  #names frisbee according to image called
            name = "Purple"
        elif(frisbee_number == 1):
            name = "Red"
        elif(frisbee_number == 2):
            name = "Yellow"
        elif(frisbee_number == 3):
            name = "White"
        new_frisbee = frisbee.Frisbee(name, x, y, frisbee_number)
        self.frisbees.add(new_frisbee)
        return new_frisbee
    def addWalls(self):
        """
        Function for generating new walls
        """
        x = random.randrange(750, 800)
        y = random.randrange(370, 615)
        new_wall = wall.Wall(x, y, "assets/Wall.png")
        self.walls.add(new_wall)
        return new_wall

    #functions for different screens
    def gameIntro(self):
        """
        Set up game intro screen
        """
        button_group = pygame.sprite.Group([self.InstructionsMM,self.PlayMM,self.quitMM]) #buttons
        intro = True
        pygame.mixer.music.load("sound/IntroMusic.wav")
        pygame.mixer.music.play(-1)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #set up button events
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if self.InstructionsMM.rect.collidepoint(mouse): #button to  instructions page
                        self.button_sound.play() #play button sound
                        retval = self.gameRules1()
                        if retval:
                            return
                    if self.quitMM.rect.collidepoint(mouse): #quit game
                        pygame.quit()
                        quit()
                    if self.PlayMM.rect.collidepoint(mouse): #start game       
                        self.button_sound.play() #play button sound
                        return  # return value for gameplay function

            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.mainmenu.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)   #Add buttons
            pygame.display.flip()

    def gameRules1(self):
        """
        Set up the first instructions page
        """
        button_group = pygame.sprite.Group([self.menu,self.next]) #buttons
        rules1 = True
        while rules1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #set up button events
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if self.menu.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        return
                    if self.next.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        retval = self.gameRules2()
                        if retval == 0:
                            return False
                        if retval == 1:
                            return True
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.instructions1.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)
            pygame.display.flip()

    def gameRules2(self):
        """
        Set up the second instructions page
        """
        button_group = pygame.sprite.Group([self.menu, self.Instback, self.Instplay])
        rules2 = True
        while rules2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #button to  instructions page
                    mouse = pygame.mouse.get_pos()
                    if self.menu.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        return 0
                    if self.Instplay.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        return 1
                    if self.Instback.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        return 2
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.instructions2.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)
            pygame.display.flip()

    def gameWon(self, score):
        """
        set up the "You Won" Page
        """
        button_group = pygame.sprite.Group([self.EndAgain,self.EndMenu])
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        winner = True
        pygame.mixer.music.stop() #stop gameplay music
        self.victory_sound.play() #play victory noise
        while winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #setting up buttons. left click only
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        self.button_sound.play()  #play button sound
                        return True
                    if self.EndMenu.rect.collidepoint(mouse):
                        self.button_sound.play() #play button sound
                        return False
            self.screen.fill([255, 255, 255]) #Fill screen with white
            self.screen.blit(self.winner.image, (0,0)) #put BG over white, under other objects.
            textsurfaceScore = myfont.render("Score: " + str(score), True, (255,255,255))
            self.screen.blit(textsurfaceScore,(300, 250))
            button_group.draw(self.screen)
            pygame.display.flip()

    def gameLost(self, score):
        """
        Set up the "You Lost" Page
        """
        button_group = pygame.sprite.Group([self.EndAgain, self.EndMenu])
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        loser = True
        pygame.mixer.music.stop() #stop gameplay music
        self.failure_sound.play()  #play failure noise
        while loser:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #setting up buttons
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        self.button_sound.play()
                        return True
                    if self.EndMenu.rect.collidepoint(mouse):
                        self.button_sound.play()
                        return False
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.loser.image, (0,0)) #put BG over white, under other objects.
            textsurfaceScore = myfont.render("Score: " + str(score), True, (255,255,255))
            self.screen.blit(textsurfaceScore,(295, 270))
            button_group.draw(self.screen)
            pygame.display.flip()

#    def highScores(self, score):
#        fptr = open("scores.txt", "r")
#        score_list = []
#        for line in fptr:
#            score_list.append(int(line))
#        fprt.close()
#        if current_score > score_list[4]:
#            score_list.append(current_score)
#            score_list = score_list.sort()   #check syntax
#            score_list.pop()
#        fptr_out = open("scores.txt","w")
#        for score in score_list:
#            fprt_out.write(score)
#        fprt_out.close()
        

    def mainLoop(self):
        """
        This is the main loop of the game
        """
        status = True
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        t = timer.Timer(120) #set up a 120 sec (2 min) timer
        health = 10 #set health to 10
        score = 0   #set score to 0
        self.all_sprites = pygame.sprite.Group([self.walls, self.frisbees, self.dog, self.clouds])
        pygame.key.set_repeat(1,50)
        pygame.time.set_timer(pygame.USEREVENT,4500)    #timer for frisbees
        pygame.time.set_timer(pygame.USEREVENT+1,13000) #timer for new wall every 13 sec
        pygame.time.set_timer(pygame.USEREVENT+2,10000) #timer for new cloud every 10 sec
        pygame.mixer.music.load("sound/GPMusic.wav")    #play music during gameplay
        pygame.mixer.music.play(-1)
        while t.time_remaining() > 0:
            self.screen.fill([255, 255, 255]) #Fill screen with white
            self.screen.blit(self.gamescreen.image, (0,0)) #put BG over white, under other objects
            textsurfaceTime = myfont.render(str(t.time_remaining()), True, (0,0,0))
            textsurfaceScore = myfont.render("Score: " + str(score), True, (0,0,0))
            if(health>=4):
                textsurfaceHealth = myfont.render("Health: " + str(health), True, (0,0,0)) 
            else:
                textsurfaceHealth = myfont.render("Health: " + str(health), True, (220,20,60)) #Health turns red if 3 or lower
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.dog.moveUp()
                    elif(event.key == pygame.K_DOWN):
                        self.dog.moveDown()
                    elif(event.key == pygame.K_LEFT):
                        self.dog.moveLeft()
                    elif(event.key == pygame.K_RIGHT):
                        self.dog.moveRight()
    
                if event.type == pygame.USEREVENT:   #generate frisbees
                    self.all_sprites.add(self.addFrisbee())
                if event.type == pygame.USEREVENT+1: #generate walls
                    self.all_sprites.add(self.addWalls())
                if event.type == pygame.USEREVENT+2: #generate clouds
                    self.all_sprites.add(self.addClouds())
            """check for collisions"""
            #Collide with wall
            trips = pygame.sprite.spritecollide(self.dog, self.walls, True)
            if(trips):
                if(health>1):  
                    health -= 1
                elif(health==1):
                    health = 0
                    return self.gameLost(score)    #Lose the game if you run out of health
            #collide with frisbee
            catch = pygame.sprite.spritecollide(self.dog, self.frisbees, True)
            for item in catch:
                if(item.name == "White"):
                    score -= 10
                elif(item.name == "Red"):
                    score += 20
                elif(item.name == "Purple"):
                    score += 10
                elif(item.name == "Yellow"):
                    score += 1
            
            self.all_sprites.draw(self.screen)
            self.screen.blit(textsurfaceTime,(0,0))
            self.screen.blit(textsurfaceHealth,(640,0))
            self.screen.blit(textsurfaceScore,(640,35))
            self.all_sprites.update()
            pygame.display.flip()
        return self.gameWon(score)

def main():
    main_window = Controller()
    while True:
        main_window.gameIntro()
        while main_window.mainLoop():
            pass
main()
