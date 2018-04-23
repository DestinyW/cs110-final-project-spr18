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
    
        self.mainmenu = background.Background("GUI/menu.png", [0, 0])
    
    def game_intro(self):               #Set up game intro screen. still missing buttons. BG WONT WORK
        intro = True
        while intro:
            #self.screen.blit(self.background, [0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill([255, 255, 255])   #Fill screen with white
            self.screen.blit(self.mainmenu.image, self.mainmenu.rect) #put BG over white, under other objects.
        
        #pygame.draw.rect(self.screen, red, (306, 145, 191, 68))    #start of trying to figure out buttons
    
        pygame.display.update()

    #def game_rules1(self):              #Set up instructions screen 1
    #pass
    
    #def game_rules1(self):
    #pass
    

    """This is the Main Loop of the Game"""
    def mainLoop(self):
        self.game_intro()
        #game_rules1()
        #game.rules2()



def main():
    main_window = Controller()
    main_window.mainLoop()
main()
