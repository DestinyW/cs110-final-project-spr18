import pygame
#from classes import dog
#from classes import frisbee
#from classes import hurdle
#from classes import score
#from classes import timer
from classes import background
from classes import button

#The ONLY thing this code does so far is open a pygame window....
class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.button = pygame.Surface(self.screen.get_size()).convert()
        
        self.mainmenu = background.Background("GUI/MainMenu.png", [0, 0])
        self.instructions1 = background.Background("GUI/Inst1BG.png", [0, 0])
        self.instructions2 = background.Background("GUI/Inst2BG.png", [0, 0])
    
        self.InstructionsMM = button.Button("GUI/InstructionsMM.png", 306, 470, "rules")


    def game_intro(self):               #Set up game intro screen. still missing buttons.
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:    #button to  instructions page
                    mouse = pygame.mouse.getpos
                        if InstructionsMM.collidrect(mouse):
                            game_rules1()

            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.mainmenu.image, (0,0)) #put BG over white, under other objects.
            
            pygame.display.flip()

    def game_rules1(self):              #Set up instructions screen 1
        rules1 = True
        while rules1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.instructions1.image, (0,0)) #put BG over white, under other objects.
            
            pygame.display.flip()

    def game_rules1(self):
        rules2 = True
        while rules2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.instructions2.image, (0,0)) #put BG over white, under other objects.
            
            pygame.display.flip()


    def mainLoop(self):
        """This is the Main Loop of the Game"""
        self.game_intro()


def main():
    main_window = Controller()
    main_window.mainLoop()
main()
