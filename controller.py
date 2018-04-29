import pygame
import random
import sys
from src import dog
from src import frisbee
from src import wall
from src import background
from src import button
from src import timer
from src import cloud

class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        pygame.mixer.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.button = pygame.Surface(self.screen.get_size()).convert()

        """Load sprites"""
        self.dog = dog.Dog("Fido", 300, 400, "assets/GSDogRun1.png") 
        #set up the walls
        self.walls = pygame.sprite.Group()
        for i in range(1):
            self.addWalls()
        #Set up the frisbees
        self.frisbees = pygame.sprite.Group()
        for i in range(2):
            self.addFrisbee()
        #Set up clouds
        self.clouds = pygame.sprite.Group()
        for i in range(1):
            self.addClouds()

        #load background images
        self.mainmenu = background.Background("assets/MainMenu.png", [0, 0])
        self.instructions1 = background.Background("assets/Inst1.png", [0, 0])
        self.instructions2 = background.Background("assets/Inst2.png", [0, 0])
        self.gamescreen = background.Background("assets/GameBG.png", [0, 0])
        self.winner = background.Background("assets/WinBG.png", [0, 0])
        self.loser = background.Background("assets/LoseBG.png", [0, 0])  
        
        #buttons
        #buttons for the main menu
        self.InstructionsMM = button.Button("assets/InstructionsMM.png", 400, 500, "rules",True)
        self.PlayMM = button.Button("assets/PlayMM.png",400,600,"play",True)
        self.quitMM = button.Button("assets/QuitMM.png",400,700,"quit",True)
        #buttons for the first instructions page
        self.menu = button.Button("assets/InstMenu.png", 10, 680, "menu")
        self.next = button.Button("assets/Inst1Next.png", 610, 680, "next")
        #buttons for the second instruction page
        self.Instback = button.Button("assets/Inst2Back.png", 300, 680, "back")
        self.Instplay = button.Button("assets/Inst2Play.png", 610, 680, "play")
        #buttons for the end screens
        self.EndAgain = button.Button("assets/EndAgain.png", 50, 695, "again")
        self.EndMenu = button.Button("assets/EndMenu.png", 550, 670, "menu")

    #functions for continuously adding new sprites
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
        new_frisbee = frisbee.Frisbee(name, x, y, frisbee_number)  #generates frisbee
        self.frisbees.add(new_frisbee)
        return new_frisbee
    def addWalls(self):
        """
        function for generating new walls
        """
        x = random.randrange(750, 800)
        y = random.randrange(350, 630)
        new_wall = wall.Wall(x, y, "assets/Wall.png")   #generates wall
        self.walls.add(new_wall)    #adds wall
        return new_wall
    def addClouds(self):
        """
        Function for generating new clouds
        """
        x = random.randrange(750, 800)
        y = random.randrange(0, 200)
        new_cloud = cloud.Cloud(x, y, "assets/Clouds.png")   #generates cloud
        self.clouds.add(new_cloud)    #adds cloud
        return new_cloud

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
                    if self.InstructionsMM.rect.collidepoint(mouse):     #button to  instructions page
                        retval = self.gameRules1()
                        if retval:
                            return
                    if self.quitMM.rect.collidepoint(mouse):   #quit game
                        pygame.quit()
                        quit()
                    if self.PlayMM.rect.collidepoint(mouse):       #start game       
                        # return value for gameplay function
                        return

            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.mainmenu.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)   #Add buttons
            pygame.display.flip()

    def gameRules1(self):
        """
        Set up the first instructions page
        """
        button_group = pygame.sprite.Group([self.menu,self.next])     #buttons
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
                        return
                    if self.next.rect.collidepoint(mouse):   
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
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    #button to  instructions page
                    mouse = pygame.mouse.get_pos()
                    if self.menu.rect.collidepoint(mouse):
                        return 0
                    if self.Instplay.rect.collidepoint(mouse):
                        return 1
                    if self.Instback.rect.collidepoint(mouse):
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
        pygame.mixer.music.stop()   #stop gameplay music
        while winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       #setting up buttons. left click only
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        return True
                    if self.EndMenu.rect.collidepoint(mouse):
                        return False
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.winner.image, (0,0)) #put BG over white, under other objects.
            textsurfaceScore = myfont.render("Score: " + str(score), True, (255,255,255))
            self.screen.blit(textsurfaceScore,(310, 250))
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
        while loser:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   #setting up buttons
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        return True
                    if self.EndMenu.rect.collidepoint(mouse):
                        return False
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.loser.image, (0,0)) #put BG over white, under other objects.
            textsurfaceScore = myfont.render("Score: " + str(score), True, (255,255,255))
            self.screen.blit(textsurfaceScore,(295, 270))
            button_group.draw(self.screen)
            pygame.display.flip()

    def mainLoop(self):
        """
        This is the main loop of the game
        """
        status = True
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        t = timer.Timer(240)   #set up a 240 sec (4 min) timer
        health = 10      #set health to 10
        score = 0        #set score to 0
        self.all_sprites = pygame.sprite.Group([self.walls, self.frisbees, self.dog])
        pygame.key.set_repeat(1,50)
        pygame.time.set_timer(pygame.USEREVENT,5000)   #timer for frisbees
        pygame.time.set_timer(pygame.USEREVENT+1,10000)#timer for walls
        pygame.time.set_timer(pygame.USEREVENT+2,10000)#timer for clouds
        pygame.mixer.music.load("sound/GPMusic.wav")   #play music during gameplay
        pygame.mixer.music.play(-1)
        while t.time_remaining() > 0:
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.gamescreen.image, (0,0)) #put BG over white, under other objects
            textsurfaceTime = myfont.render(str(t.time_remaining()), True, (0,0,0))
            textsurfaceScore = myfont.render("Score: " + str(score), True, (0,0,0))
            if(health>=4):
                textsurfaceHealth = myfont.render("Health: " + str(health), True, (0,0,0))   
            else:
                textsurfaceHealth = myfont.render("Health: " + str(health), True, (220,20,60))   #Health turns red if 3 or lower
            
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
                if event.type == pygame.USEREVENT:            #generate frisbees
                    self.all_sprites.add(self.addFrisbee())
                if event.type == pygame.USEREVENT+1:            #generate walls
                    self.all_sprites.add(self.addWalls())
                if event.type == pygame.USEREVENT+2:       #generate clouds
                    self.all_sprites.add(self.addClouds())
            #check for collisions
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
            self.dog.update()
            self.walls.update()
            self.frisbees.update()
            self.clouds.update()
            pygame.display.flip()
        return self.gameWon(score)

def main():
    main_window = Controller()
    while True:
        main_window.gameIntro()
        while main_window.mainLoop():
            pass
main()
