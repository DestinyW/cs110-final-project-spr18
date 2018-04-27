import pygame
import time
import sys
#from src import dog
#from src import frisbee
#from src import hurdle
#from src import score
from src import background
from src import button

class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.button = pygame.Surface(self.screen.get_size()).convert()

        """Load sprites"""
        #self.dog = dog.Dog("Conan", 50, 50, "assets/GSDogRun1.png")    #will this interfere with the running animation?
        #self.walls = pygame.sprite.Group()
        #self.frisbees = pygame.sprite.Group()

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
        self.menu = button.Button("assets/InstMenu.png", 10, 650, "menu")
        self.next = button.Button("assets/Inst1Next.png", 610, 650, "next")
        #buttons for the second instruction page
        self.Instback = button.Button("assets/Inst2Back.png", 300, 650, "back")
        self.Instplay = button.Button("assets/Inst2Play.png", 610, 650, "play")
        #buttons for the end screens
        self.EndAgain = button.Button("assets/EndAgain.png", 50, 695, "again")
        self.EndMenu = button.Button("assets/EndMenu.png", 550, 670, "menu")

        #self.all_sprites = pygame.sprite.Group((self.dog)+(self.frisbees)+(self.walls))

        # members used to track time
        self.font = pygame.font.SysFont('monospace', 15)
        self.minute = 5
        self.seconds = 0


    def gameIntro(self):
        """
        Set up game intro screen
        """
        button_group = pygame.sprite.Group([self.InstructionsMM,self.PlayMM,self.quitMM])
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    #button to  instructions page
                    mouse = pygame.mouse.get_pos()
                    if self.InstructionsMM.rect.collidepoint(mouse):
                        retval = self.gameRules1()
                        if retval:
                            return
                    if self.quitMM.rect.collidepoint(mouse):
                        pygame.quit()
                        quit()
                    if self.PlayMM.rect.collidepoint(mouse):
                        # return value for gameplay function
                        return

            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.mainmenu.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)

            pygame.display.flip()

    def gameRules1(self):              #Set up instructions screen 1
        """
            Set up the first instructions page
        """
        button_group = pygame.sprite.Group([self.menu,self.next])
        rules1 = True
        while rules1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    #button to  instructions page
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

    def gameWon(self):
        """
        set up the "You Won" Page
        """
        button_group = pygame.sprite.Group([self.EndAgain,self.EndMenu])
        winner = True
        while winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       #setting up buttons
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        return 1
                    if self.EndMenu.rect.collidepoint(mouse):
                        self.gameIntro()
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.winner.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)
            pygame.display.flip()

    def gameLost(self):
        """
        set up the "You Lost" Page
        """
        button_group = pygame.sprite.Group([self.EndAgain, self.EndMenu])
        loser = True
        while loser:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   #setting up buttons
                    mouse = pygame.mouse.get_pos()
                    if self.EndAgain.rect.collidepoint(mouse):
                        return 1
                    if self.EndMenu.rect.collidepoint(mouse):
                        self.gameIntro()
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.loser.image, (0,0)) #put BG over white, under other objects.
            button_group.draw(self.screen)
            pygame.display.flip()

    def timer(self):
        #starting work on the timer
        if self.seconds == 0:
            self.minute -= 1
        self.seconds = (self.seconds - 1) % 60
        digit_str = ""
        if self.seconds < 10:
            digit_str = "0"
        new_time = str(self.minute)+":"+digit_str+str(self.seconds)

        #blit here?

    def mainLoop(self):
        """
        This is the main loop of the game
        """
        self.gameIntro()
        #self.all_sprites = pygame.sprite.Group([self.walls, self.dog])
        while True:
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.gamescreen.image, (0,0)) #put BG over white, under other objects

            #check for collisions
            #trip = pygame.sprite.spritecollide(self.dog, self.walls, True)
            #if(trips):
                #if(health>0):  #does this go here or in a Health Class. How do I display health on screen?
                    #self.healthDown()
                #else:
                    #self.gameLost()
      
            #pygame.time.set_timer(pygame.USEREVENT,1000)      
            
            pygame.display.flip()

def main():
    main_window = Controller()
    main_window.mainLoop()
main()
