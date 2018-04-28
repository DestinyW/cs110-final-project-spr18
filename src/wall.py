import pygame
import random

# model
class Wall(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image_file):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load(image_file).convert_alpha()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # set other attributes
        self.name = name + str(id(self))
        self.speed = random.randrange(8,14)    
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
    
    def reset_pos(self):
        self.rect.x = random.randrange(-1,-2)
        self.rect.y = random.randrange(self.screen_height - self.rect.width)

    def update(self):
        self.rect.x -= 1
        # resets any hurdles that slides off the screen
        if self.rect.x > self.screen_width + 10:
            self.reset_pos()
