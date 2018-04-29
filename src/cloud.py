import pygame
import random

# model
class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load(image_file).convert_alpha()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # set other attributes
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.speed = random.randrange(1,4)

    def update(self):
        self.rect.x -= self.speed

