import pygame
import random

#model
class Hurdle(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load('hurdle.png').convert_alpha()
        self.image.set_colorkey(COLOR)
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # set other attributes
        self.name = name + str(id(self))
        self.speed = 4

    # def rest_pos(self):
    #     self.rect.x = random.randrange(-1,-2)
    #     self.rect.y = random.randrange(HEIGHT - 2)

    def update(self):
        # self.rect.x += 1
        # self.rect.x += 1
        # """resets any hurdles that slides off the screen
        #     on the left back to the right"""
        # if self.rect.x < WIDTH:
        #     self.rest_pos()

        random_x = random.randrange(-1,2)
        # random_y = random.randrange(-1,2)
        self.rect.x += random_x
        # self.rect.y += random_y
        print("'Update me,' says " + self.name)
