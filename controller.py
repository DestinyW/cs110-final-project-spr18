import pygame
from classes import dog
from classes import frisbee
from classes import hurdle
from classes import score
from classes import timer
from classes import background

class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """Load the sprites that we need"""
    
    def game_intro():               #Set up game intro screen. still missing buttons.
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == gygame.QUIT:
                    pygame.quit()
                gameDisplay.fill(white)   #Fill screen with white
                screen.blit(BackGround.image, BackGround.rect) #put BG over white, under other objects.
            background = Background('MainMenuBG.png', [0,0])     #load BG image
    
    def game_rules():

    def mainLoop(self):
        """This is the Main Loop of the Game"""
        game_intro()
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.dog.moveUp()
        
            #check for collisions
            catch = pygame.sprite.spritecollide(self.dog, self.frisbee, True)
            
            trip = pygame.sprite.spritecollide(self.dog, self.hurdle, True)
            
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


def main():
    main_window = Controller()
    main_window.mainLoop()
main()
