import pygame
import random

# model
class Frisbee(pygame.sprite.Sprite):
    def __init__(self, name, x, y, frisbee_number):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        if(frisbee_number == 0):
            image_file = "assets/Purple.png"
        elif(frisbee_number == 1):
            image_file = "assets/Red.png"
        elif(frisbee_number == 2):
            image_file = "assets/Yellow.png"
        elif(frisbee_number == 3):
            image_file = "assets/White.png"
        self.image = pygame.image.load(image_file).convert_alpha()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # set other attributes
        self.name = name
        self.speed = random.randrange(3,10)
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

    def update(self):
        self.rect.x -= self.speed

